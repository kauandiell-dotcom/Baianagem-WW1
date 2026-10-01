"""
Tier 1: Syntax & Brace Integrity Validator for Hearts of Iron IV Clausewitz & YAML files.

Checks:
- Balanced curly braces { and } in Clausewitz files (.txt, .gfx, .gui).
- Correct handling of comments (#) and double-quoted strings ("...").
- Exact UTF-8 BOM bytes (\\xef\\xbb\\xbf) on all localization files (.yml).
- Valid language key headers (e.g. l_english:, l_braz_por:).
- Unclosed string literals or quotes in localization.
"""

import os
import sys
import unittest
from typing import List, Tuple, Optional, Dict, Any

# Root mod path
MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class ClausewitzSyntaxError(Exception):
    """Raised when a Clausewitz syntax violation is detected."""
    def __init__(self, filepath: str, line: int, col: int, message: str, snippet: str = ""):
        self.filepath = filepath
        self.line = line
        self.col = col
        self.message = message
        self.snippet = snippet
        super().__init__(f"{filepath}:{line}:{col}: {message}\n  --> {snippet}")


def validate_clausewitz_syntax(filepath: str) -> Dict[str, Any]:
    """
    Parses a Clausewitz file (.txt, .gfx, .gui) verifying:
    - Quote balancing and escape handling
    - Brace depth ({ and }) balancing
    Returns a dict with diagnostics.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    # Read with utf-8, fallback to latin-1 / windows-1252 if BOM or special chars
    with open(filepath, "rb") as f:
        raw_bytes = f.read()

    # Detect encoding
    if raw_bytes.startswith(b"\xef\xbb\xbf"):
        content = raw_bytes[3:].decode("utf-8", errors="replace")
    else:
        try:
            content = raw_bytes.decode("utf-8")
        except UnicodeDecodeError:
            content = raw_bytes.decode("cp1252", errors="replace")

    depth = 0
    in_string = False
    escape_next = False
    brace_stack = []  # stores (line, col) of unmatched {
    string_start = (0, 0)

    lines = content.splitlines(keepends=True)
    total_open_braces = 0
    total_close_braces = 0

    for line_idx, line_text in enumerate(lines, start=1):
        col = 0
        while col < len(line_text):
            char = line_text[col]

            if in_string:
                if escape_next:
                    escape_next = False
                elif char == "\\":
                    escape_next = True
                elif char == '"':
                    in_string = False
                # ignore all other chars inside string
                col += 1
                continue

            # Outside string
            if char == "#":
                # Comment until end of line
                break
            elif char == '"':
                in_string = True
                string_start = (line_idx, col + 1)
            elif char == "{":
                depth += 1
                total_open_braces += 1
                brace_stack.append((line_idx, col + 1))
            elif char == "}":
                total_close_braces += 1
                if depth == 0:
                    snippet = line_text.strip()
                    raise ClausewitzSyntaxError(
                        filepath, line_idx, col + 1,
                        "Unexpected closing brace '}' with no matching opening brace",
                        snippet
                    )
                depth -= 1
                brace_stack.pop()

            col += 1

    if in_string:
        s_line, s_col = string_start
        snippet = lines[s_line - 1].strip() if s_line <= len(lines) else ""
        raise ClausewitzSyntaxError(
            filepath, s_line, s_col,
            "Unclosed string quote '\"' reaching end-of-file",
            snippet
        )

    if depth != 0:
        s_line, s_col = brace_stack[-1]
        snippet = lines[s_line - 1].strip() if s_line <= len(lines) else ""
        raise ClausewitzSyntaxError(
            filepath, s_line, s_col,
            f"Unmatched opening brace '{{' (unclosed at EOF, remaining depth: {depth})",
            snippet
        )

    return {
        "filepath": filepath,
        "valid": True,
        "total_lines": len(lines),
        "open_braces": total_open_braces,
        "close_braces": total_close_braces,
    }


def validate_yaml_localization(filepath: str, expected_lang_header: Optional[str] = None) -> Dict[str, Any]:
    """
    Validates a Paradox HoI4 localization YAML file:
    - Must start with UTF-8 BOM bytes (\xef\xbb\xbf)
    - Must have valid language header (e.g. l_english:, l_braz_por:)
    - Parses keys and values, ensures closed quotes
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, "rb") as f:
        raw = f.read()

    # Check UTF-8 BOM
    if not raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError(
            f"{filepath}: Missing mandatory UTF-8 BOM signature (\\xef\\xbb\\xbf). "
            f"First bytes: {raw[:4]!r}"
        )

    text = raw[3:].decode("utf-8", errors="strict")
    lines = text.splitlines()

    # Find first non-empty, non-comment line
    header_found = None
    header_line_idx = -1
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        header_found = stripped
        header_line_idx = idx
        break

    if not header_found:
        raise ValueError(f"{filepath}: Empty localization file or only comments")

    valid_headers = ["l_english:", "l_braz_por:", "l_german:", "l_french:", "l_spanish:", "l_russian:"]
    matched_header = None
    for vh in valid_headers:
        if header_found.startswith(vh):
            matched_header = vh
            break

    if not matched_header:
        raise ValueError(
            f"{filepath}:{header_line_idx}: Invalid localization header: '{header_found}'. "
            f"Expected one of: {valid_headers}"
        )

    if expected_lang_header and not header_found.startswith(expected_lang_header):
        raise ValueError(
            f"{filepath}:{header_line_idx}: Language header mismatch. "
            f"Expected '{expected_lang_header}', found '{header_found}'"
        )

    # Parse key-value pairs
    keys_found = {}
    for line_idx, line in enumerate(lines[header_line_idx:], start=header_line_idx + 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue

        # Pattern: key:0 "Value" or key: "Value"
        colon_pos = s.find(":")
        if colon_pos == -1:
            raise ValueError(f"{filepath}:{line_idx}: Malformed localization entry (no colon): {s}")

        key = s[:colon_pos].strip()
        val_part = s[colon_pos + 1:].strip()

        # May have version index like :0 "text"
        if val_part and val_part[0].isdigit():
            # strip version number
            sp_pos = val_part.find(" ")
            if sp_pos != -1:
                val_part = val_part[sp_pos + 1:].strip()

        # Check quotes around value and strip trailing comments like "Text" # comment
        if val_part and not val_part.startswith("#"):
            if val_part.startswith('"'):
                end_quote = -1
                for q_idx in range(1, len(val_part)):
                    if val_part[q_idx] == '"' and val_part[q_idx - 1] != '\\':
                        end_quote = q_idx
                        break
                if end_quote != -1:
                    trailing = val_part[end_quote + 1:].strip()
                    if trailing == "" or trailing.startswith("#"):
                        val_part = val_part[:end_quote + 1]

            if not (val_part.startswith('"') and val_part.endswith('"') and len(val_part) >= 2):
                raise ValueError(
                    f"{filepath}:{line_idx}: Value for key '{key}' is not properly double-quoted: {val_part}"
                )
            # Check for unescaped internal quotes
            inner = val_part[1:-1]
            i = 0
            while i < len(inner):
                if inner[i] == '"' and (i == 0 or inner[i - 1] != '\\'):
                    raise ValueError(
                        f"{filepath}:{line_idx}: Unescaped quote inside string for key '{key}': {val_part}"
                    )
                i += 1

        keys_found[key] = val_part

    return {
        "filepath": filepath,
        "valid": True,
        "header": matched_header,
        "key_count": len(keys_found),
        "keys": keys_found,
    }


class TestTier1Syntax(unittest.TestCase):
    """Automated Unit Tests for Tier 1: Syntax & Brace Integrity."""

    def test_sprite_definitions_gfx_syntax(self):
        """Validate syntax and brace balancing of interface/ww1_germany_goals.gfx."""
        gfx_path = os.path.join(MOD_ROOT, "interface", "ww1_germany_goals.gfx")
        if not os.path.exists(gfx_path):
            self.skipTest("ww1_germany_goals.gfx not yet implemented (Milestone 1 pending)")

        res = validate_clausewitz_syntax(gfx_path)
        self.assertTrue(res["valid"])
        self.assertEqual(res["open_braces"], res["close_braces"])
        self.assertGreater(res["open_braces"], 0)

    def test_german_focus_tree_syntax(self):
        """Validate syntax and brace balancing of common/national_focus/germany.txt."""
        focus_path = os.path.join(MOD_ROOT, "common", "national_focus", "germany.txt")
        if not os.path.exists(focus_path):
            self.skipTest("germany.txt not found")

        # If it's the placeholder comment stub, verify it parses cleanly
        res = validate_clausewitz_syntax(focus_path)
        self.assertTrue(res["valid"])
        self.assertEqual(res["open_braces"], res["close_braces"])

    def test_ideas_syntax(self):
        """Validate syntax and brace balancing of national modifier files."""
        idea_files = [
            os.path.join(MOD_ROOT, "common", "ideas", "ww1_national_modifiers.txt"),
            os.path.join(MOD_ROOT, "common", "ideas", "ww1_germany_ideas.txt"),
            os.path.join(MOD_ROOT, "common", "ideas", "MBR_Central_Powers.txt"),
        ]
        tested_any = False
        for path in idea_files:
            if os.path.exists(path):
                res = validate_clausewitz_syntax(path)
                self.assertTrue(res["valid"], f"Syntax error in {path}")
                self.assertEqual(res["open_braces"], res["close_braces"])
                tested_any = True

        if not tested_any:
            self.skipTest("No idea files found to validate")

    def test_events_syntax(self):
        """Validate syntax and brace balancing of German events file."""
        events_path = os.path.join(MOD_ROOT, "events", "ww1_germany_events.txt")
        if not os.path.exists(events_path):
            self.skipTest("events/ww1_germany_events.txt not yet implemented (Milestone 2 pending)")

        res = validate_clausewitz_syntax(events_path)
        self.assertTrue(res["valid"])
        self.assertEqual(res["open_braces"], res["close_braces"])

    def test_english_localization_bom_and_syntax(self):
        """Validate UTF-8 BOM and syntax of English localization."""
        candidates = [
            os.path.join(MOD_ROOT, "localisation", "english", "ww1_germany_l_english.yml"),
            os.path.join(MOD_ROOT, "localisation", "english", "ww1_germany_focus_l_english.yml"),
        ]
        existing = [p for p in candidates if os.path.exists(p)]
        if not existing:
            self.skipTest("English localization file not yet created (Milestone 4 pending)")

        for loc_file in existing:
            res = validate_yaml_localization(loc_file, expected_lang_header="l_english:")
            self.assertTrue(res["valid"])
            self.assertGreater(res["key_count"], 0)

    def test_portuguese_localization_bom_and_syntax(self):
        """Validate UTF-8 BOM and syntax of Brazilian Portuguese localization."""
        candidates = [
            os.path.join(MOD_ROOT, "localisation", "braz_por", "ww1_germany_l_braz_por.yml"),
            os.path.join(MOD_ROOT, "localisation", "braz_por", "ww1_germany_focus_l_braz_por.yml"),
        ]
        existing = [p for p in candidates if os.path.exists(p)]
        if not existing:
            self.skipTest("PT-BR localization file not yet created (Milestone 4 pending)")

        for loc_file in existing:
            res = validate_yaml_localization(loc_file, expected_lang_header="l_braz_por:")
            self.assertTrue(res["valid"])
            self.assertGreater(res["key_count"], 0)


def run_tier1(verbose: bool = True) -> bool:
    """Entry point for standalone Tier 1 test execution."""
    print("=" * 70)
    print("TIER 1: Syntax & Brace Integrity Audit")
    print("=" * 70)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestTier1Syntax)
    runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tier1()
    sys.exit(0 if success else 1)

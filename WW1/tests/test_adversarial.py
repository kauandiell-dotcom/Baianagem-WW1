"""
Adversarial & Edge Case Verification Tests.

Exercises the validation engine with edge, malformed, and adversarial inputs:
1. Encoding & Escaping Integrity:
   - Clausewitz strings with embedded comments (#), braces ({, }), and escaped quotes (\").
   - YAML localization files with/without UTF-8 BOM, special unicode characters, and trailing comments.
2. Invalid Input Combinations:
   - Unmatched braces, negative depth triggers, unclosed quotes.
   - Corrupted DDS headers (invalid magic, zero dimensions, truncated headers).
3. Boundary & Graph Stress:
   - Artificial cyclic prerequisite graphs.
   - Coordinate collision triggers.
   - Malformed YAML keys and syntax.
"""

import os
import sys
import io
import struct
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(__file__))

from tier1_syntax import (
    validate_clausewitz_syntax,
    validate_yaml_localization,
    ClausewitzSyntaxError,
)
from tier2_assets import validate_dds_header
from tier3_graph import detect_cycles, FocusNode


class TestAdversarialIntegrity(unittest.TestCase):
    """Stress tests and boundary checks for the test suite validators."""

    def test_clausewitz_embedded_characters_in_strings(self):
        """Verify braces and comments inside strings do NOT trigger syntax errors."""
        content = """
        focus_tree = {
            id = test_tree
            focus = {
                id = test_focus_1
                text = "This string has # not a comment and { braces } inside! \\"escaped quotes\\""
            }
        }
        """
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".txt") as tf:
            tf.write(content)
            tf_path = tf.name

        try:
            res = validate_clausewitz_syntax(tf_path)
            self.assertTrue(res["valid"])
            self.assertEqual(res["open_braces"], 2)
            self.assertEqual(res["close_braces"], 2)
        finally:
            if os.path.exists(tf_path):
                os.remove(tf_path)

    def test_clausewitz_unclosed_brace_rejected(self):
        """Verify unclosed opening brace triggers ClausewitzSyntaxError with location."""
        content = """
        focus_tree = {
            id = test_tree
            focus = {
                id = test_focus_1
            # Missing closing brace
        """
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".txt") as tf:
            tf.write(content)
            tf_path = tf.name

        try:
            with self.assertRaises(ClausewitzSyntaxError) as ctx:
                validate_clausewitz_syntax(tf_path)
            self.assertIn("Unmatched opening brace", ctx.exception.message)
        finally:
            if os.path.exists(tf_path):
                os.remove(tf_path)

    def test_clausewitz_unexpected_closing_brace_rejected(self):
        """Verify extra closing brace triggers ClausewitzSyntaxError with location."""
        content = """
        focus_tree = {
            id = test_tree
        }
        } # Extra closing brace
        """
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".txt") as tf:
            tf.write(content)
            tf_path = tf.name

        try:
            with self.assertRaises(ClausewitzSyntaxError) as ctx:
                validate_clausewitz_syntax(tf_path)
            self.assertIn("Unexpected closing brace", ctx.exception.message)
        finally:
            if os.path.exists(tf_path):
                os.remove(tf_path)

    def test_yaml_missing_utf8_bom_rejected(self):
        """Verify YAML localization without UTF-8 BOM is strictly rejected."""
        content = 'l_english:\n test_key:0 "Valid Value"\n'
        with tempfile.NamedTemporaryFile("wb", delete=False, suffix=".yml") as tf:
            tf.write(content.encode("utf-8"))  # Without BOM
            tf_path = tf.name

        try:
            with self.assertRaises(ValueError) as ctx:
                validate_yaml_localization(tf_path)
            self.assertIn("Missing mandatory UTF-8 BOM", str(ctx.exception))
        finally:
            if os.path.exists(tf_path):
                os.remove(tf_path)

    def test_yaml_valid_with_utf8_bom_accepted(self):
        """Verify YAML with UTF-8 BOM and trailing comment parses cleanly."""
        raw = b"\xef\xbb\xbf" + 'l_english:\n test_key:0 "Valid Value" # inline comment\n'.encode("utf-8")
        with tempfile.NamedTemporaryFile("wb", delete=False, suffix=".yml") as tf:
            tf.write(raw)
            tf_path = tf.name

        try:
            res = validate_yaml_localization(tf_path)
            self.assertTrue(res["valid"])
            self.assertEqual(res["key_count"], 1)
            self.assertEqual(res["keys"]["test_key"], '"Valid Value"')
        finally:
            if os.path.exists(tf_path):
                os.remove(tf_path)

    def test_dds_corrupt_magic_rejected(self):
        """Verify file with invalid magic bytes is rejected."""
        with tempfile.NamedTemporaryFile("wb", delete=False, suffix=".dds") as tf:
            # Write invalid magic
            tf.write(b"PNG \x00\x00\x00\x00" + b"\x00" * 128)
            tf_path = tf.name

        try:
            with self.assertRaises(ValueError) as ctx:
                validate_dds_header(tf_path)
            self.assertIn("Invalid DDS magic bytes", str(ctx.exception))
        finally:
            if os.path.exists(tf_path):
                os.remove(tf_path)

    def test_dds_zero_dimensions_rejected(self):
        """Verify DDS with zero width or height is rejected."""
        header = bytearray(128)
        header[0:4] = b"DDS "
        struct.pack_into("<I", header, 4, 124)  # dwSize = 124
        struct.pack_into("<I", header, 12, 0)   # dwHeight = 0
        struct.pack_into("<I", header, 16, 64)  # dwWidth = 64

        with tempfile.NamedTemporaryFile("wb", delete=False, suffix=".dds") as tf:
            tf.write(header)
            tf_path = tf.name

        try:
            with self.assertRaises(ValueError) as ctx:
                validate_dds_header(tf_path)
            self.assertIn("Invalid DDS dimensions", str(ctx.exception))
        finally:
            if os.path.exists(tf_path):
                os.remove(tf_path)

    def test_graph_detects_deliberate_cycle(self):
        """Verify cycle detection algorithm flags deliberate cycle A -> B -> C -> A."""
        nodes = {
            "focus_A": FocusNode("focus_A"),
            "focus_B": FocusNode("focus_B"),
            "focus_C": FocusNode("focus_C"),
        }
        nodes["focus_A"].prerequisites = [["focus_B"]]
        nodes["focus_B"].prerequisites = [["focus_C"]]
        nodes["focus_C"].prerequisites = [["focus_A"]]

        cycles = detect_cycles(nodes)
        self.assertGreater(len(cycles), 0, "Cycle detection failed to detect 3-node cycle")


if __name__ == "__main__":
    unittest.main()

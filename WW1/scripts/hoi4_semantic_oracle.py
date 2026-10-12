"""
HOI4 Clausewitz Semantic Oracle.
Provides definitive validation for country modifier tokens against
the official Hearts of Iron IV engine definitions.
"""
import os
import json
import re
from typing import Set, List, Dict, Tuple, Optional

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CACHE_FILE = os.path.join(MOD_ROOT, "data", "hoi4_valid_country_modifiers.json")

_VALID_MODIFIERS: Optional[Set[str]] = None


def get_valid_modifiers() -> Set[str]:
    """Returns the set of all valid Clausewitz HOI4 country modifier tokens."""
    global _VALID_MODIFIERS
    if _VALID_MODIFIERS is not None:
        return _VALID_MODIFIERS

    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            mods_list = json.load(f)
            _VALID_MODIFIERS = set(mods_list)
            return _VALID_MODIFIERS

    # Fallback to empty if cache not yet built
    _VALID_MODIFIERS = set()
    return _VALID_MODIFIERS


def is_valid_country_modifier(token: str) -> bool:
    """Checks whether a modifier key is recognized by the Clausewitz engine."""
    valid_set = get_valid_modifiers()
    return token in valid_set


def audit_modifier_dict(mod_dict: Dict[str, any]) -> List[str]:
    """Returns a list of keys in the dict that are NOT recognized country modifiers."""
    invalid = []
    for k in mod_dict.keys():
        if not is_valid_country_modifier(k):
            invalid.append(k)
    return invalid


def audit_file_modifiers(filepath: str) -> List[Tuple[int, str, str]]:
    """
    Parses a Clausewitz file and extracts all modifier = { ... } blocks,
    returning a list of (line_num, token_name, idea_or_context_id) that are invalid.
    """
    if not os.path.exists(filepath):
        return []

    errors = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    in_modifier_block = False
    brace_depth = 0
    current_context = "unknown"

    for line_idx, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        # Simple context tracking (e.g. idea_id = {)
        id_match = re.match(r"^([a-zA-Z0-9_]+)\s*=\s*\{", line)
        if id_match and not in_modifier_block:
            token = id_match.group(1)
            if token not in ("ideas", "country", "modifier", "limit", "available", "rule"):
                current_context = token

        if "modifier" in line and "{" in line:
            in_modifier_block = True
            brace_depth = 1
            continue

        if in_modifier_block:
            brace_depth += line.count("{") - line.count("}")
            if brace_depth <= 0:
                in_modifier_block = False
                continue

            # Inside modifier = { ... }, check token = value
            if "=" in line and not line.startswith("#"):
                parts = line.split("=")
                key = parts[0].strip()
                # filter out structural keywords inside modifier like custom_effect_tooltip
                if key in ("custom_effect_tooltip",):
                    continue
                if not is_valid_country_modifier(key):
                    errors.append((line_idx, key, current_context))

    return errors


if __name__ == "__main__":
    mods = get_valid_modifiers()
    print(f"Clausewitz Semantic Oracle initialized with {len(mods)} valid modifiers.")

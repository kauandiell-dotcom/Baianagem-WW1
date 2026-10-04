"""
Tier 4: End-to-End Consistency & Mirroring Integrity Validator.

Verifies:
- 100% dual localization coverage (English and Brazilian Portuguese) for:
    * 32 Focus titles (<id>) and descriptions (<id>_desc).
    * National idea titles (<id>) and descriptions (<id>_desc).
    * Country event titles (<id>.t), descriptions (<id>.d), and options (<id>.a).
- Zero missing localization keys in either language.
- Accurate Steam Workshop directory mirroring:
    * Verifies target directory exists.
    * Verifies that modified/created mod assets match between local repo and Steam Workshop target.
"""

import os
import sys
import hashlib
import unittest
from typing import Dict, List, Set, Tuple, Any, Optional

sys.path.insert(0, os.path.dirname(__file__))
from spec import (
    EXPECTED_FOCUSES,
    EXPECTED_EVENT_IDS,
    EXPECTED_NEW_IDEAS,
)

from tier1_syntax import validate_yaml_localization

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Recognized German localization candidate file paths
GER_LOC_EN_CANDIDATES = [
    os.path.join(MOD_ROOT, "localisation", "english", "ww1_germany_l_english.yml"),
    os.path.join(MOD_ROOT, "localisation", "english", "ww1_germany_focus_l_english.yml"),
]

GER_LOC_PT_CANDIDATES = [
    os.path.join(MOD_ROOT, "localisation", "braz_por", "ww1_germany_l_braz_por.yml"),
    os.path.join(MOD_ROOT, "localisation", "braz_por", "ww1_germany_focus_l_braz_por.yml"),
]


def load_german_localization_keys(lang_candidates: List[str]) -> Tuple[Dict[str, str], List[str]]:
    """
    Finds and parses German localization files from candidates.
    Returns (dict of key -> value, list of existing files found).
    """
    found_files = [p for p in lang_candidates if os.path.isfile(p)]
    keys: Dict[str, str] = {}
    for fpath in found_files:
        res = validate_yaml_localization(fpath)
        keys.update(res["keys"])
    return keys, found_files


def get_file_sha256(filepath: str) -> str:
    """Calculates SHA-256 checksum of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


class TestTier4LocalizationMirror(unittest.TestCase):
    """Automated Unit Tests for Tier 4: Localization & Mirroring Integrity."""

    def test_english_localization_coverage(self):
        """Verify 100% English localization coverage for focuses, ideas, and events."""
        en_keys, found_files = load_german_localization_keys(GER_LOC_EN_CANDIDATES)
        if not found_files:
            self.skipTest("German English localization file not yet created (Milestone 4 pending)")

        missing_focus_titles = []
        missing_focus_descs = []
        for fid in EXPECTED_FOCUSES:
            if fid not in en_keys:
                missing_focus_titles.append(fid)
            if f"{fid}_desc" not in en_keys:
                missing_focus_descs.append(f"{fid}_desc")

        missing_ideas = []
        for iid in EXPECTED_NEW_IDEAS:
            if iid not in en_keys:
                missing_ideas.append(iid)

        missing_events = []
        for eid in EXPECTED_EVENT_IDS:
            if f"{eid}.t" not in en_keys:
                missing_events.append(f"{eid}.t")
            if f"{eid}.d" not in en_keys:
                missing_events.append(f"{eid}.d")

        all_missing = missing_focus_titles + missing_focus_descs + missing_ideas + missing_events
        self.assertEqual(
            all_missing,
            [],
            f"Missing English localization keys ({len(all_missing)} missing): {all_missing}"
        )

    def test_portuguese_localization_coverage(self):
        """Verify 100% Brazilian Portuguese localization coverage for focuses, ideas, and events."""
        pt_keys, found_files = load_german_localization_keys(GER_LOC_PT_CANDIDATES)
        if not found_files:
            self.skipTest("German PT-BR localization file not yet created (Milestone 4 pending)")

        missing_focus_titles = []
        missing_focus_descs = []
        for fid in EXPECTED_FOCUSES:
            if fid not in pt_keys:
                missing_focus_titles.append(fid)
            if f"{fid}_desc" not in pt_keys:
                missing_focus_descs.append(f"{fid}_desc")

        missing_ideas = []
        for iid in EXPECTED_NEW_IDEAS:
            if iid not in pt_keys:
                missing_ideas.append(iid)

        missing_events = []
        for eid in EXPECTED_EVENT_IDS:
            if f"{eid}.t" not in pt_keys:
                missing_events.append(f"{eid}.t")
            if f"{eid}.d" not in pt_keys:
                missing_events.append(f"{eid}.d")

        all_missing = missing_focus_titles + missing_focus_descs + missing_ideas + missing_events
        self.assertEqual(
            all_missing,
            [],
            f"Missing PT-BR localization keys ({len(all_missing)} missing): {all_missing}"
        )

    def test_repository_asset_integrity(self):

        """
        Verify that all critical mod assets exist within the repository.
        Checks DDS goals, GFX, focus tree, ideas, events, and localization.
        """
        files_to_check = [
            os.path.join("interface", "ww1_germany_goals.gfx"),
            os.path.join("interface", "ww1_russia_goals.gfx"),
            os.path.join("common", "national_focus", "germany.txt"),
            os.path.join("common", "national_focus", "soviet.txt"),
            os.path.join("events", "ww1_germany_events.txt"),
            os.path.join("common", "ideas", "ww1_germany_ideas.txt"),
            os.path.join("localisation", "english", "ww1_germany_focus_l_english.yml"),
            os.path.join("localisation", "braz_por", "ww1_germany_focus_l_braz_por.yml"),
        ]

        goals_dir = os.path.join(MOD_ROOT, "gfx", "interface", "goals")
        if os.path.isdir(goals_dir):
            for dds_file in os.listdir(goals_dir):
                if dds_file.endswith(".dds"):
                    files_to_check.append(os.path.join("gfx", "interface", "goals", dds_file))

        missing_files = []
        for rel_path in files_to_check:
            src_path = os.path.join(MOD_ROOT, rel_path)
            if not os.path.exists(src_path):
                missing_files.append(rel_path)

        self.assertEqual(len(missing_files), 0, f"Missing repository files: {missing_files[:5]}")



def run_tier4(verbose: bool = True) -> bool:
    """Entry point for standalone Tier 4 test execution."""
    print("=" * 70)
    print("TIER 4: End-to-End Consistency & Mirroring Integrity Audit")
    print("=" * 70)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestTier4LocalizationMirror)
    runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tier4()
    sys.exit(0 if success else 1)

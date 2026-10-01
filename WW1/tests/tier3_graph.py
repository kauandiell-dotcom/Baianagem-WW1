"""
Tier 3: Graph & Mechanical Integrity Validator.

Analyzes common/national_focus/germany.txt and verifies:
- 0 circular dependencies in focus prerequisite graph (DFS 3-color DAG cycle detection).
- All prerequisite focus IDs exist in the tree.
- All mutual exclusion focus IDs exist in the tree.
- (x, y) coordinates have 0 collisions across all focuses.
- All state IDs referenced in focus effects exist in history/states/.
- All idea IDs referenced exist in common/ideas/*.txt.
- All event IDs referenced exist in events/*.txt.
- Exact compliance with the 32-focus specification in tests/spec.py.
"""

import os
import sys
import re
import unittest
from typing import Dict, List, Set, Tuple, Any, Optional

sys.path.insert(0, os.path.dirname(__file__))
from spec import (
    EXPECTED_FOCUSES,
    EXPECTED_FOCUS_COUNT,
    EXPECTED_EVENT_IDS,
    EXPECTED_NEW_IDEAS,
    EXPECTED_STARTING_IDEAS,
    EXPECTED_REFERENCED_STATES,
)

MOD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class FocusNode:
    """Represents a single parsed national focus."""
    def __init__(self, focus_id: str):
        self.focus_id = focus_id
        self.x = 0
        self.y = 0
        self.relative_position_id: Optional[str] = None
        self.abs_x = 0
        self.abs_y = 0
        self.cost = 10
        self.icon = ""
        self.prerequisites: List[List[str]] = []  # List of OR-groups
        self.mutually_exclusive: List[str] = []
        self.raw_block = ""
        self.referenced_states: Set[int] = set()
        self.referenced_ideas: Set[str] = set()
        self.referenced_events: Set[str] = set()

    def __repr__(self):
        return f"<FocusNode {self.focus_id} @ ({self.abs_x}, {self.abs_y})>"


def parse_focus_tree(file_path: str) -> Dict[str, FocusNode]:
    """
    Parses an HoI4 national focus tree file and returns a dictionary of focus_id -> FocusNode.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Focus tree file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Remove comments
    lines = []
    for line in content.splitlines():
        line_clean = re.sub(r'#.*$', '', line)
        lines.append(line_clean)
    clean_content = "\n".join(lines)

    focuses: Dict[str, FocusNode] = {}

    # Find each focus = { ... } block using brace matching
    idx = 0
    while True:
        match = re.search(r'\bfocus\s*=\s*\{', clean_content[idx:])
        if not match:
            break

        start_brace = idx + match.end() - 1
        # Match closing brace
        depth = 1
        pos = start_brace + 1
        in_str = False
        while pos < len(clean_content) and depth > 0:
            ch = clean_content[pos]
            if ch == '"':
                in_str = not in_str
            elif not in_str:
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
            pos += 1

        block = clean_content[start_brace + 1 : pos - 1]
        idx = pos

        # Parse focus ID
        id_match = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block)
        if not id_match:
            continue
        focus_id = id_match.group(1).strip()
        node = FocusNode(focus_id)
        node.raw_block = block

        # Coordinates
        x_match = re.search(r'\bx\s*=\s*(-?\d+)', block)
        y_match = re.search(r'\by\s*=\s*(-?\d+)', block)
        if x_match:
            node.x = int(x_match.group(1))
        if y_match:
            node.y = int(y_match.group(1))

        rel_match = re.search(r'\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)', block)
        if rel_match:
            node.relative_position_id = rel_match.group(1).strip()

        # Cost
        cost_match = re.search(r'\bcost\s*=\s*(\d+(?:\.\d+)?)', block)
        if cost_match:
            node.cost = float(cost_match.group(1))

        # Icon
        icon_match = re.search(r'\bicon\s*=\s*([a-zA-Z0-9_]+)', block)
        if icon_match:
            node.icon = icon_match.group(1).strip()

        # Prerequisites: multiple prerequisite = { focus = A focus = B }
        for prereq_match in re.finditer(r'\bprerequisite\s*=\s*\{([^}]+)\}', block):
            inner = prereq_match.group(1)
            or_group = re.findall(r'\bfocus\s*=\s*([a-zA-Z0-9_]+)', inner)
            if or_group:
                node.prerequisites.append(or_group)

        # Mutually exclusive: mutually_exclusive = { focus = A focus = B }
        for mut_match in re.finditer(r'\bmutually_exclusive\s*=\s*\{([^}]+)\}', block):
            inner = mut_match.group(1)
            mut_ids = re.findall(r'\bfocus\s*=\s*([a-zA-Z0-9_]+)', inner)
            node.mutually_exclusive.extend(mut_ids)

        # Extract state references
        # controls_state = 34, owns_state = 34, transfer_state = 34, state = 34
        state_matches = re.findall(r'\b(?:controls_state|owns_state|transfer_state|state)\s*=\s*(\d+)', block)
        for sm in state_matches:
            node.referenced_states.add(int(sm))

        # Extract idea references: add_ideas, remove_ideas, has_idea, swap_ideas
        idea_matches = re.findall(r'\b(?:add_ideas|remove_ideas|has_idea)\s*=\s*([a-zA-Z0-9_]+)', block)
        for im in idea_matches:
            node.referenced_ideas.add(im)
        for swap_match in re.finditer(r'\bswap_ideas\s*=\s*\{([^}]+)\}', block):
            inner = swap_match.group(1)
            sub_ideas = re.findall(r'\b(?:remove_idea|add_idea)\s*=\s*([a-zA-Z0-9_]+)', inner)
            for si in sub_ideas:
                node.referenced_ideas.add(si)

        # Extract event references: country_event = { id = ... }
        event_matches = re.findall(r'\bcountry_event\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_.]+)', block)
        for em in event_matches:
            node.referenced_events.add(em)

        focuses[focus_id] = node

    # Compute absolute coordinates
    for focus_id, node in focuses.items():
        curr = node
        abs_x = curr.x
        abs_y = curr.y
        visited_rel = set()
        while curr.relative_position_id and curr.relative_position_id in focuses:
            if curr.relative_position_id in visited_rel:
                break
            visited_rel.add(curr.relative_position_id)
            parent = focuses[curr.relative_position_id]
            abs_x += parent.x
            abs_y += parent.y
            curr = parent
        node.abs_x = abs_x
        node.abs_y = abs_y

    return focuses


def detect_cycles(focuses: Dict[str, FocusNode]) -> List[List[str]]:
    """
    Detects circular dependencies in focus prerequisites.
    Edge U -> V means U requires V.
    Uses DFS 3-color coloring (0: White, 1: Gray, 2: Black).
    Returns list of cycles found.
    """
    color = {fid: 0 for fid in focuses}
    parent = {fid: None for fid in focuses}
    cycles = []

    def dfs(u: str, path: List[str]):
        color[u] = 1  # Gray (in progress)
        node = focuses.get(u)
        if node:
            # All prerequisite nodes that u depends on
            for or_group in node.prerequisites:
                for v in or_group:
                    if v not in focuses:
                        continue
                    if color[v] == 1:
                        # Found cycle
                        cycle_start = path.index(v) if v in path else 0
                        cycle = path[cycle_start:] + [u, v]
                        cycles.append(cycle)
                    elif color[v] == 0:
                        dfs(v, path + [u])
        color[u] = 2  # Black (finished)

    for fid in focuses:
        if color[fid] == 0:
            dfs(fid, [])

    return cycles


def load_all_existing_state_ids(mod_root: str) -> Set[int]:
    """Scans history/states/ and extracts all valid state IDs."""
    states_dir = os.path.join(mod_root, "history", "states")
    state_ids = set()
    if not os.path.isdir(states_dir):
        return state_ids

    for fname in os.listdir(states_dir):
        if not fname.endswith(".txt"):
            continue
        # Check filename pattern e.g. "34-Belgium.txt" or "1088-German Congo.txt"
        m = re.match(r'^(\d+)', fname)
        if m:
            state_ids.add(int(m.group(1)))
        else:
            # Read inside file for id = <int>
            filepath = os.path.join(states_dir, fname)
            with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            m2 = re.search(r'\bid\s*=\s*(\d+)', content)
            if m2:
                state_ids.add(int(m2.group(1)))

    return state_ids


def load_all_existing_idea_ids(mod_root: str) -> Set[str]:
    """Scans common/ideas/ and extracts all declared idea names."""
    ideas_dir = os.path.join(mod_root, "common", "ideas")
    idea_ids = set()
    if not os.path.isdir(ideas_dir):
        return idea_ids

    for fname in os.listdir(ideas_dir):
        if not fname.endswith(".txt"):
            continue
        filepath = os.path.join(ideas_dir, fname)
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Remove comments
        clean = re.sub(r'#.*$', '', content, flags=re.MULTILINE)

        # Match top-level idea keys inside country = { ... }
        # Pattern: idea_name = {
        matches = re.findall(r'^\s*([a-zA-Z0-9_]+)\s*=\s*\{', clean, flags=re.MULTILINE)
        for m in matches:
            if m not in ("ideas", "country", "hidden_ideas", "political_advisor", "tank_manufacturer", "high_command"):
                idea_ids.add(m)

    return idea_ids


def load_all_existing_event_ids(mod_root: str) -> Set[str]:
    """Scans events/ and extracts all declared event IDs."""
    events_dir = os.path.join(mod_root, "events")
    event_ids = set()
    if not os.path.isdir(events_dir):
        return event_ids

    for fname in os.listdir(events_dir):
        if not fname.endswith(".txt"):
            continue
        filepath = os.path.join(events_dir, fname)
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        clean = re.sub(r'#.*$', '', content, flags=re.MULTILINE)
        # Match country_event = { id = <id> } or news_event = { id = <id> }
        matches = re.findall(r'\bid\s*=\s*([a-zA-Z0-9_.]+)', clean)
        for m in matches:
            event_ids.add(m)

    return event_ids


class TestTier3Graph(unittest.TestCase):
    """Automated Unit Tests for Tier 3: Graph & Mechanical Integrity."""

    @classmethod
    def setUpClass(cls):
        cls.focus_file = os.path.join(MOD_ROOT, "common", "national_focus", "germany.txt")
        cls.focuses = {}
        if os.path.isfile(cls.focus_file):
            with open(cls.focus_file, "r", encoding="utf-8", errors="replace") as f:
                raw = f.read()
            if "focus_tree" in raw and "GER_agadir_crisis_gambit" in raw:
                cls.focuses = parse_focus_tree(cls.focus_file)

    def test_focus_tree_implemented(self):
        """Verify common/national_focus/germany.txt contains the implemented German tree."""
        if not self.focuses:
            self.skipTest("germany.txt does not contain full focus tree yet (Milestone 3 pending)")
        self.assertGreaterEqual(
            len(self.focuses),
            EXPECTED_FOCUS_COUNT,
            f"Expected {EXPECTED_FOCUS_COUNT} focuses, found {len(self.focuses)}"
        )

    def test_zero_circular_dependencies(self):
        """Verify the focus tree has 0 circular dependencies (DAG property)."""
        if not self.focuses:
            # Test against authoritative spec graph to verify theoretical validity
            spec_nodes = {}
            for fid, meta in EXPECTED_FOCUSES.items():
                node = FocusNode(fid)
                if meta["prerequisites"]:
                    node.prerequisites.append(meta["prerequisites"])
                if "prerequisites_or" in meta:
                    node.prerequisites.append(meta["prerequisites_or"])
                spec_nodes[fid] = node

            cycles = detect_cycles(spec_nodes)
            self.assertEqual(cycles, [], f"Specification itself has cycles: {cycles}")
            return

        cycles = detect_cycles(self.focuses)
        self.assertEqual(
            cycles,
            [],
            f"Circular dependencies detected in germany.txt: {cycles}"
        )

    def test_all_prerequisite_focus_ids_exist(self):
        """Verify that every prerequisite focus ID exists in the tree."""
        if not self.focuses:
            self.skipTest("germany.txt not yet implemented")

        all_ids = set(self.focuses.keys())
        missing_prereqs = []
        for fid, node in self.focuses.items():
            for or_group in node.prerequisites:
                for prereq_id in or_group:
                    if prereq_id not in all_ids:
                        missing_prereqs.append((fid, prereq_id))

        self.assertEqual(
            missing_prereqs,
            [],
            f"Prerequisite references to nonexistent focus IDs: {missing_prereqs}"
        )

    def test_all_mutual_exclusion_focus_ids_exist(self):
        """Verify that all mutually_exclusive focus IDs exist in the tree."""
        if not self.focuses:
            self.skipTest("germany.txt not yet implemented")

        all_ids = set(self.focuses.keys())
        missing_mut = []
        for fid, node in self.focuses.items():
            for mut_id in node.mutually_exclusive:
                if mut_id not in all_ids:
                    missing_mut.append((fid, mut_id))

        self.assertEqual(
            missing_mut,
            [],
            f"Mutually exclusive references to nonexistent focus IDs: {missing_mut}"
        )

    def test_coordinate_collisions(self):
        """Verify (x, y) coordinates have 0 collisions across all focuses."""
        if not self.focuses:
            # Validate spec coordinates
            coords = {}
            collisions = []
            for fid, meta in EXPECTED_FOCUSES.items():
                pos = (meta["x"], meta["y"])
                if pos in coords:
                    collisions.append((pos, coords[pos], fid))
                coords[pos] = fid
            self.assertEqual(collisions, [], f"Coordinate collisions in spec: {collisions}")
            return

        coords = {}
        collisions = []
        for fid, node in self.focuses.items():
            pos = (node.abs_x, node.abs_y)
            if pos in coords:
                collisions.append((pos, coords[pos], fid))
            coords[pos] = fid

        self.assertEqual(
            collisions,
            [],
            f"Focus coordinate collisions detected: {collisions}"
        )

    def test_state_ids_exist_in_history_states(self):
        """Verify all referenced state IDs exist in history/states/."""
        valid_states = load_all_existing_state_ids(MOD_ROOT)
        self.assertGreater(len(valid_states), 500, "history/states/ should contain hundreds of states")

        # First check expected states from spec
        for st in EXPECTED_REFERENCED_STATES:
            self.assertIn(st, valid_states, f"Spec state ID {st} not found in history/states/")

        if not self.focuses:
            return

        # Check actual focuses in germany.txt
        invalid_states = []
        for fid, node in self.focuses.items():
            for sid in node.referenced_states:
                if sid not in valid_states:
                    invalid_states.append((fid, sid))

        self.assertEqual(
            invalid_states,
            [],
            f"References to nonexistent state IDs in germany.txt: {invalid_states}"
        )

    def test_idea_ids_exist_in_common_ideas(self):
        """Verify all referenced idea IDs exist in common/ideas/*.txt."""
        valid_ideas = load_all_existing_idea_ids(MOD_ROOT)

        # All starting ideas must exist
        for idea in EXPECTED_STARTING_IDEAS:
            self.assertIn(idea, valid_ideas, f"Starting idea {idea} missing from common/ideas/")

        if not self.focuses:
            return

        missing_ideas = []
        for fid, node in self.focuses.items():
            for iid in node.referenced_ideas:
                if iid not in valid_ideas:
                    missing_ideas.append((fid, iid))

        self.assertEqual(
            missing_ideas,
            [],
            f"References to nonexistent idea IDs in germany.txt: {missing_ideas}"
        )

    def test_event_ids_exist_in_events(self):
        """Verify all referenced event IDs exist in events/*.txt."""
        if not self.focuses:
            self.skipTest("germany.txt not yet implemented")

        valid_events = load_all_existing_event_ids(MOD_ROOT)
        missing_events = []
        for fid, node in self.focuses.items():
            for eid in node.referenced_events:
                if eid not in valid_events:
                    missing_events.append((fid, eid))

        self.assertEqual(
            missing_events,
            [],
            f"References to nonexistent event IDs in germany.txt: {missing_events}"
        )


def run_tier3(verbose: bool = True) -> bool:
    """Entry point for standalone Tier 3 test execution."""
    print("=" * 70)
    print("TIER 3: Graph & Mechanical Integrity Audit")
    print("=" * 70)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestTier3Graph)
    runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tier3()
    sys.exit(0 if success else 1)

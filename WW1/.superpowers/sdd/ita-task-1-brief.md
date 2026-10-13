# Italy Rework Task 1: Master QA Test Suite Expansion (`tests/test_ww1_italy.py` — RED Phase)

**Files:**
- Modify: `tests/test_ww1_italy.py`

## Requirements
Expand `tests/test_ww1_italy.py` to add comprehensive assertions for the Italy Complete Rework while preserving all existing tests:

1. In `TestItalyTreeAndGraph.test_non_overlapping_coordinates_and_descending_y`:
   - Group focuses by `y = int(n.get("y", 0))` and sort by `x = int(n.get("x", 0))`. Assert that for every adjacent pair on the same `y` row, `abs(x2 - x1) >= 2` (no horizontal banner collisions).
   - In the prerequisite loop, also assert `1 <= int(n.get("y")) - int(self.foci[parent_id].get("y")) <= 3` (no long vertical prerequisite arrows spanning 4+ rows).
   - Assert `not (ROOT / "common" / "national_focus" / "italy.txt.disabled").exists()`.

2. In `TestItalyBalanceAndMechanics`, add `test_zero_shallow_focuses(self)`:
   - Parse raw `completion_reward` blocks from `common/national_focus/italy.txt` (or inspect `walk(reward)` keys).
   - Assert that every focus has at least one tangible effect beyond flat `add_political_power`, `add_stability`, `add_war_support`, `army_experience`, `navy_experience`, `air_experience`, `add_command_power`, `add_to_variable`, `set_country_flag`, `custom_effect_tooltip`, and `ita_ww1_clamp_counters`. Specifically, after stripping those flat tokens/blocks from raw `completion_reward`, the remaining body must not be empty!

3. In `TestItalyBalanceAndMechanics`, add `test_active_five_gauges_and_zero_unused_ideas(self)`:
   - Read `common/scripted_effects/ww1_italy_effects.txt` and extract the `ita_ww1_update_gauges` block.
   - Assert that `ita_ww1_update_gauges` contains `check_variable` checks for all 5 gauges (`ita_ww1_interventionism`, `ita_ww1_social_tension`, `ita_ww1_army_morale`, `ita_ww1_southern_gap`, `ita_ww1_irredentism`) and applies the dynamic gauge ideas (`ITA_ww1_neutralist_predominance`, `ITA_ww1_social_truce`, `ITA_ww1_stoic_endurance`, `ITA_ww1_southern_disparity`, `ITA_ww1_unredeemed_lands_call`, etc.).

4. In `TestItalyIdeasAndModifiers.test_ideas_volume_and_valid_modifiers`:
   - Assert that all 9 restored ideas exist in `common/ideas/ww1_italy_ideas.txt`:
     - `ITA_terre_irredente_dream`
     - `ITA_alpini_tradition`
     - `ITA_coal_iron_scarcity`
     - `ITA_southern_question_gap`
     - `ITA_sacro_egoismo_policy`
     - `ITA_isonzo_attrition_crisis_1`
     - `ITA_isonzo_attrition_crisis_2`
     - `ITA_isonzo_attrition_crisis_3`
     - `ITA_vittorio_veneto_triumph`
   - Assert that every idea defined in `common/ideas/ww1_italy_ideas.txt` is referenced at least once across `history/countries/ITA - Italy.txt`, `common/national_focus/italy.txt`, `common/decisions/ww1_italy_decisions.txt`, `common/scripted_effects/ww1_italy_effects.txt`, or `events/ww1_italy_*.txt` (0 unused ideas!).
   - Also run `from scripts.hoi4_semantic_oracle import audit_file_modifiers` on `common/ideas/ww1_italy_ideas.txt` and `common/decisions/ww1_italy_decisions.txt` and assert 0 errors.

5. In `TestItalyEventsAndDecisions`, add `test_map_state_targeted_decisions_and_zero_orphan_events(self)`:
   - Read `common/decisions/ww1_italy_decisions.txt` and assert the presence of all 9 new decisions:
     - `ITA_ww1_mezzogiorno_aqueduct_and_roads`
     - `ITA_ww1_carabinieri_anti_brigandage_sweep`
     - `ITA_ww1_southern_agrarian_credit_consortium`
     - `ITA_ww1_alpine_mine_warfare_tunnel`
     - `ITA_ww1_launch_isonzo_general_offensive`
     - `ITA_ww1_fortify_piave_and_monte_grappa`
     - `ITA_ww1_fortify_libyan_coastal_oases`
     - `ITA_ww1_integrate_irredenta_province`
     - `ITA_ww1_impresa_di_pola_raid`
   - Assert `common/decisions/ww1_italy_decisions.txt` contains at least 6 `state_target = yes` blocks.
   - Assert that `ww1_italy.50` and `ww1_italy.63` are triggered at least once across focuses, decisions, or events.

6. In `TestItalyLocalisationAndGraphics`:
   - Assert single UTF-8 BOM (`raw[:3] == b"\xef\xbb\xbf"` and `raw[3:6] != b"\xef\xbb\xbf"`) on both `ww1_italy_l_english.yml` and `ww1_italy_l_braz_por.yml`.
   - Assert that every idea in `common/ideas/ww1_italy_ideas.txt` and every decision in `common/decisions/ww1_italy_decisions.txt` has both ` {id}:0 ` and ` {id}_desc:0 ` in both `ww1_italy_l_english.yml` and `ww1_italy_l_braz_por.yml`.
   - Assert that all `texturefile` paths referenced in `interface/ww1_italy_goals.gfx`, `interface/ww1_italy_ideas.gfx`, `interface/ww1_italy_decisions.gfx`, and `interface/ww1_italy_events.gfx` (except `gfx/interface/goals/shine_overlay.dds`) exist on disk in the mod directory!

## Verification & Commit
Run `python -m unittest tests/test_ww1_italy.py -v` and confirm the new assertions fail as expected (RED phase).
Commit:
```bash
git add tests/test_ww1_italy.py
git commit -m "test(ita): expand Italy QA test suite for complete rework (RED)"
```
Write your report to `C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\.superpowers\sdd\ita-task-1-report.md`.

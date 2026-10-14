### Task 3: Western Front Opening, Fused Schlieffen & Trench Stalemate Transition

**Files:**
- Modify: `common/national_focus/germany.txt`
- Create: `common/ideas/ww1_germany_western_front_ideas.txt`
- Create: `events/ww1_germany_western_front_events.txt`
- Test: `tests/test_ww1_germany_rework.py::TestGermanyOverhaul::test_schlieffen_and_stalemate`

**Interfaces:**
- Consumes: Fused Schlieffen focus `GER_schlieffen_maneuver`
- Produces: `GER_schlieffen_momentum`, event `ww1_germany.10`, and `GER_western_trench_stalemate`

- [ ] **Step 1: Write idea definitions in `common/ideas/ww1_germany_western_front_ideas.txt`**
Define `GER_schlieffen_momentum` (+10% soft attack, +15% speed, +96h supply grace, 90 days) and `GER_western_trench_stalemate` (+15 max entrenchment, +30% entrenchment speed, +20% core/occupied defense).
Validate with `scripts.hoi4_semantic_oracle`.

- [ ] **Step 2: Fuse Belgian Ultimatum and Schlieffen in `common/national_focus/germany.txt`**
Create focus `GER_schlieffen_maneuver`, occupy Luxembourg on start, deliver Belgian ultimatum, and grant momentum idea.

- [ ] **Step 3: Implement stalemate transition event in `events/ww1_germany_western_front_events.txt`**
Event `ww1_germany.10`: triggers when `GER_schlieffen_momentum` expires without Paris captured (`NOT = { controls_state = 16 }`), removing momentum and adding `GER_western_trench_stalemate`.

- [ ] **Step 4: Run test to verify it passes**
Run: `python -m unittest tests.test_ww1_germany_rework.TestGermanyOverhaul.test_schlieffen_and_stalemate -v`
Expected: PASS.

- [ ] **Step 5: Commit**
```bash
git add common/national_focus/germany.txt common/ideas/ events/
git commit -m "feat(ger): fuse Schlieffen maneuver, add supply grace, and implement deep trench stalemate transition"
```

---


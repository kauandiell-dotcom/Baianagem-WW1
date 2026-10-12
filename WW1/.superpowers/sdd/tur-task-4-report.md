# Ottoman Rework Task 4 Report: Historical Events Overhaul, Great Arab Revolt & Libyan Resistance

## Status
- **Status:** COMPLETED
- **Commit Hash:** `fc052fc860f003ff500b68430f113e3699452014` (`fc052fc`)
- **Modified File:** `events/ww1_ottoman_events.txt`

## Summary of Changes
1. **Updated `ww1_ottoman.19` (`ww1_ottoman.19.a`):**
   - Added `country_event = { id = ww1_ottoman.31 days = 5 }` to Option A (`ww1_ottoman.19.a`) so that the Hejaz revolt triggers the territorial map-wide escalation check 5 days later.
2. **Implemented `ww1_ottoman.31` (Territorial Eruption of the Great Arab Revolt):**
   - Configured `id = ww1_ottoman.31`, `title = ww1_ottoman.31.t`, `desc = ww1_ottoman.31.d`, `picture = GFX_report_event_report_event_arab_revolt`, `is_triggered_only = yes`.
   - Checks each Arab state (`679`, `856`, `554`, `454`, `291`, `1011`) for ownership by `TUR` and absence of `TUR_vilayet_garrison_secured`, applying `damage_building = { type = infrastructure damage = 2 }` to unsecured states.
   - If both Hejaz/Holy Cities (`679` and `856`) have `TUR_vilayet_garrison_secured`, swaps `TUR_arab_unrest_smoldering` for `TUR_imperial_vilayets_pacified`, grants `+10%` stability and `25` army experience, and sets `TUR_arab_revolt_crushed_by_garrisons`.
   - Otherwise, swaps `TUR_arab_unrest_smoldering` for `TUR_arab_revolt_insurgency` (or adds `TUR_arab_revolt_insurgency`), deducts `10,000` manpower and `500` `infantry_equipment_1`, and sets `TUR_arab_insurgency_active`.
3. **Implemented `ww1_ottoman.32` (The Tripolitanian Resistance: Enver Bey & Mustafa Kemal in Libya):**
   - Configured `id = ww1_ottoman.32`, `title = ww1_ottoman.32.t`, `desc = ww1_ottoman.32.d`, `picture = GFX_report_event_news_army_in_desert`, `is_triggered_only = yes`.
   - Option A (`ww1_ottoman.32.a`): Adds `TUR_senussi_desert_brotherhood`, grants `25` army experience and `+5%` war support, constructs level 1 bunkers in states `448` and `450` if owned by `TUR`, and sets `TUR_enver_kemal_in_libya`.
   - Option B (`ww1_ottoman.32.b`): Grants `50` political power and `10,000` manpower, constructs a level 1 bunker in state `341` if owned by `TUR`, and sets `TUR_balkan_priority_over_libya`.

## Verification Summary
- **Semantic Modifier Audit:** `audit_file_modifiers('events/ww1_ottoman_events.txt')` returned `[]` (0 errors).
- **Bracket Balance:** 245 opening `{` and 245 closing `}` (balanced).

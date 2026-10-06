# Alpha integration: operations, crisis recovery and eastern negotiations

This delivery starts the WW1 redesign. It is not a complete campaign or a claim of final balance.

## Operations

The South-Western Front (Russia) and Meuse sector (Germany) now use actual objectives.
Completing the planning focus opens the relevant decisions; it does not win the battle.

- Preparation occupies 35 days, costs 30 political power and 40 command power,
  and consumes 50 support equipment from the country stockpile.
- A reserve of 40 artillery is required; those guns are not deleted as ammunition.
- Preparing diverts factory output and raises supply demand.
- The operation lasts at most 60 days. The breakthrough advantage targets the
  specified enemy country (Austria-Hungary or France), rather than every enemy.
- Success requires control of the stated regions: Stanisławów and Lwów for the
  South-Western operation; Champagne for the Meuse-sector operation.
- Success ends the concentration and supplies limited operational learning.
  Failure ends the concentration and adds a 30-day reorganization penalty.
- Peace or capitulation cancels preparation/operation and cleans up their spirits.
- This uses enemy-specific national modifiers. It does not claim that the engine
  restricts the advantage to one selected army or individual province.

French manpower is no longer subtracted by choosing the German Verdun event.
Combat determines casualties. German Michael coordination now expires after 60 days.

## Institutional and diplomatic contracts

Russian aviation-school improvements replace their preceding stages. The
reconnaissance-service improvements use a separate replacement chain.
Directly declared raw modifiers in focus rewards were removed.

Research programmes target registered technology categories. Doctrine programmes
use the current mastery system. Where a teaching focus otherwise has no immediate
XP reward, a small five-point training result also makes it useful before the first
subdoctrine is purchased; this is distinct from the removed 500-XP human startup bonus.

Ottoman officer instruction and coalition membership are separate offers with
acceptance/refusal and replies. Neither generates equipment or declares war.
The Reichstag peace resolution is a political stance, not an automatic armistice.
Zimmermann now has a Mexican reply and an American interception response; no
alliance or war is manufactured by the proposal alone.

## Crisis timing and recovery

The generic weekly callback executes once for each country. Eight national
callbacks now update only their own country, preventing world-country count from
multiplying episode counters.

A pressure episode starts mildly after sustained material/political pressure and
the war warm-up period. Escalation time is reset at onset, so a late opening cannot
jump from mild to severe in the same week. Actual pressure ending permits gradual
recovery. The recovery grace period expires; continued pressure can cause a later
episode, without permanent immunity or a victory bonus.

The 90-day relief projects reserve civilian factories and cost political effort.
Delivered relief responds to the current stage, including improvements while the
project was running. Supplies can reduce or delay severity; the final stage closes
only when its material/political cause has ceased.

Convoy threat and convoy-loss morale are native proxies for maritime pressure.
These measures do not yet constitute a dedicated food-stock or overseas-trade
simulation. Such systems remain on the full campaign roadmap.

## Eastern settlement safety

Replies go to the original requesting Russian government (FROM). This remains
correct if SOV and RUS both exist during a civil war.

German terms are bound to one interlocutor and expire after 30 days. A changed or
expired offer cannot transfer territory. A late refusal from a different government
cannot cancel the current interlocutor's terms. Weekly cleanup closes stale
authorizations after peace or disappearance.

The accepting Russian country may concede only its own German-controlled
Polish/Baltic frontier districts specified by the treaty. Unoccupied districts,
territory belonging to the other Russian government, and the Russian interior are
excluded. Both sides must consent; food and internal crises recover separately.

## Regression evidence

Run from the WW1 directory:

    python -B -m unittest tests/test_ww1_foundation.py tests/test_ww1_gameplay_contracts.py -v

The gameplay tests parse the shipped PDX scripts and execute a documented subset
of their triggers/effects. They cover material consumption; objectives;
success/failure/cancellation; once-per-country weekly timing; all eight national
pressure inputs; mild onset, escalation, recovery and recurrence; zero-equipment
division safety; 90-day relief and factory release; Russian interlocutor identity;
limited territorial cession; stale peace offers and unrelated late refusal.

These tests do not execute Clausewitz. In-game mission timing, event FROM
inheritance, native targeted-modifier behavior, graphics, doctrine UI, AI and
multiplayer still require engine verification. They also do not establish campaign
win rates or final stacking budgets.


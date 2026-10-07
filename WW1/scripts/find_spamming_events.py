import re
from pathlib import Path

ROOT = Path(".")

print("=== CHECKING ALL EVENTS FOR MISSING IS_TRIGGERED_ONLY OR MISSING TRIGGER ===")
for p in (ROOT / "events").glob("*.txt"):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    # match top-level event blocks
    raw_events = re.split(r'\n(?=(?:country_event|news_event)\s*=)', txt)
    for ev in raw_events:
        if not ("country_event" in ev or "news_event" in ev):
            continue
        m_id = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\.\-]+)', ev)
        if not m_id:
            continue
        eid = m_id.group(1)
        is_trig_only = "is_triggered_only = yes" in ev or "is_triggered_only=yes" in ev
        has_trigger = re.search(r'\btrigger\s*=\s*\{', ev)
        has_mtth = "mean_time_to_happen" in ev
        
        if not is_trig_only and not has_trigger and not has_mtth:
            print(f"[{p.name}] CRITICAL SPAM EVENT (fires every 20 days automatically): {eid}")
        elif not is_trig_only and has_trigger:
            # check trigger condition
            trig_m = re.search(r'\btrigger\s*=\s*\{(.*?)\}', ev, re.DOTALL)
            trig_content = trig_m.group(1).strip() if trig_m else ""
            print(f"[{p.name}] Natural trigger event: {eid} -> Trigger: {trig_content[:80]}")

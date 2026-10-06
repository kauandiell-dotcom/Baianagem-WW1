"""Import art for the extra AUH content from installed Workshop copies (read-only donors).

Exact paths, no generation. Writes DDS files, sprite registrations and a provenance record, and refuses
duplicates (exact pixels or near-identical thumbnails) against every other image of the extra set and the
mod's existing event pictures.
"""
from pathlib import Path
import hashlib, json, sys
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
WORKSHOP = Path('E:/SteamLibrary/steamapps/workshop/content/394360')
T, K, E = '3365515312', '2076426030', '2716194283'

EVENTS = {  # sprite key -> (mod, path under gfx/event_pictures)
    'army_bill': (T, 'AUS/report_event_conrad'),
    'balkan_league': (T, 'hoi4tgw/hoi4tgw_balkan_league'),
    'scutari': (T, 'hoi4tgw/hoi4tgw_first_balkan_war_end'),
    'redl': (T, 'AUS/report_event_alfred_redl'),
    'belvedere': (T, 'AUS/report_event_franz_ferdinand'),
    'kolubara': (T, 'AUS/report_event_picture_oskar_potiorek'),
    'carpathian_winter': (T, 'AUS/report_event_conrad_inspect_troops'),
    'gorlice': (T, 'hoi4tgw_reports/hoi4tgw_report_ww1_a'),
    'brusilov': (T, 'AUS/news_event_conrad'),
    'bread_queues': (T, 'AUS/report_event_famine1'),
    'january_strike': (T, 'AUS/jannerstreik'),
    'epiphany': (T, 'hoi4tgw_reports/hoi4tgw_report_austria_hungary'),
    'cattaro': (T, 'hoi4tgw/hoi4tgw_armistice'),
    'piave': (T, 'hoi4tgw/hoi4tgw_second_balkan_war'),
    'manifesto': (T, 'AUS/news_event_karl_abdication'),
    'harvest': (T, 'AUS/report_event_famine2'),
    'delegations_session': (T, 'hoi4tgw/hoi4tgw_second_balkan_war_end'),
    'triple_alliance': (T, 'AUS/report_event_franz_ferdinand_wilhelm_ii'),
    'bosnia_report': (T, 'AUS/report_event_marijan_varesanin'),
}
IDEAS = {  # name -> (mod, path under gfx/interface/goals)
    'inst_staff_college': (E, 'kaiserreich/generic_army_training'),
    'inst_sapper_school': (T, 'construction_engineering'),
    'inst_pilot_school': (E, 'kaiserreich/generic_air_fighter_obselete'),
    'inst_investment_board': (E, 'kaiserreich/generic_foreign_investments'),
    'subsidised_arsenals': (E, 'kaiserreich/generic_artillery_factories'),
    'replanned_deployment': (T, 'focus_planning_bonus'),
    'fortress_inspection': (E, 'kaiserreich/aus_fortress'),
    'front_crisis': (E, 'kaiserreich/generic_crisis'),
    'strike_wave': (T, 'focus_generic_protest'),
    'naval_unrest': (E, 'kaiserreich/GEA_Kaiserliche_Marine'),
    'winter_training': (E, 'kaiserreich/generic_cold_training'),
}
DECISIONS = {
    'arsenal_subsidy': (E, 'kaiserreich/arms_export'),
    'winter_manoeuvres': (E, 'kaiserreich/generic_army_grand_battleplan'),
    'inspect_fortress_belt': (T, 'focus_railway_gun'),
    'mountain_cadres': (T, 'generic_mountain_warfare'),
    'pola_review': (E, 'kaiserreich/Ecole_Naval_de_Guerre'),
    'sound_out_sofia': (T, 'focus_BUL_bulgarian_serbian_treaty'),
    'constantinople_mission': (T, 'ottoman_friendship'),
    'coronation_city_visit': (T, 'focus_HUN_coat_of_arms'),
    'governors_conference': (E, 'kaiserreich/federalist_conference'),
}

def locate(mod, folder, rel):
    base = WORKSHOP / mod / folder / rel
    for ext in ('.png', '.dds', '.tga'):
        p = base.with_suffix(ext) if base.suffix == '' else Path(str(base) + ext)
        p = Path(str(base) + ext)
        if p.is_file():
            return p
    raise FileNotFoundError(str(base))

def ahash(im):
    g = ImageOps.grayscale(im.convert('RGBA')).resize((16, 16), Image.Resampling.LANCZOS)
    px = list(g.getdata()); avg = sum(px) / len(px)
    return int(''.join('1' if p > avg else '0' for p in px), 2)

def ham(a, b):
    return bin(a ^ b).count('1')

def main():
    seen_px, seen_h, records, sprites = {}, [], [], ['spriteTypes = {']
    # existing mod event pictures
    existing = []
    for p in (ROOT / 'gfx/event_pictures').rglob('*'):
        if p.suffix.lower() in ('.dds', '.png', '.tga') and 'ww1_auh_extra' not in p.as_posix():
            try:
                existing.append((p, ahash(Image.open(p))))
            except Exception:
                pass
    problems = []
    def take(kind, name, mod, folder, rel, size, dest_dir, sprite, fit):
        src = locate(mod, folder, rel)
        im = Image.open(src).convert('RGBA')
        out = ImageOps.fit(im, size, Image.Resampling.LANCZOS) if fit else None
        if not fit:
            c = ImageOps.contain(im, size, Image.Resampling.LANCZOS)
            out = Image.new('RGBA', size); out.alpha_composite(c, ((size[0] - c.width) // 2, (size[1] - c.height) // 2))
        px = hashlib.sha256(out.tobytes()).hexdigest()
        h = ahash(out)
        if px in seen_px:
            problems.append((kind, name, 'exact duplicate of', seen_px[px]))
        for other, oh in seen_h:
            if ham(h, oh[0]) <= 8 and oh[1] == kind:
                problems.append((kind, name, 'near-duplicate of', oh[2]))
        if kind == 'event':
            for p, oh in existing:
                if ham(h, oh) <= 6:
                    problems.append((kind, name, 'near-duplicate of existing', p.relative_to(ROOT).as_posix()))
        seen_px[px] = f'{kind}:{name}'; seen_h.append((None, (h, kind, f'{kind}:{name}')))
        dest = ROOT / dest_dir / f'{name}.dds'
        dest.parent.mkdir(parents=True, exist_ok=True)
        out.save(dest)
        tex = dest.relative_to(ROOT).as_posix()
        sprites.append(f' spriteType = {{ name = "{sprite}" texturefile = "{tex}" }}')
        records.append(dict(kind=kind, name=name, sprite=sprite, donor_id=mod, source_relative=f'{folder}/{rel}',
                            source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(), texture=tex))
    # fix seen_h structure (list of (None,(hash,kind,label))) -> iterate correctly
    for name, (mod, rel) in EVENTS.items():
        take('event', name, mod, 'gfx/event_pictures', rel, (450, 250), 'gfx/event_pictures/ww1_auh_extra', f'GFX_event_AUH_ww1_{name}', True)
    for name, (mod, rel) in IDEAS.items():
        take('idea', name, mod, 'gfx/interface/goals', rel, (64, 64), 'gfx/interface/ideas/ww1_auh_extra', f'GFX_idea_AUH_ww1_{name}', False)
    for name, (mod, rel) in DECISIONS.items():
        take('decision', name, mod, 'gfx/interface/goals', rel, (64, 64), 'gfx/interface/decisions/ww1_auh_extra', f'GFX_decision_AUH_ww1_{name}', False)
    sprites.append('}')
    if problems:
        print(json.dumps(problems, ensure_ascii=False, indent=1))
        return 1
    (ROOT / 'interface/ww1_austria_hungary_extra_assets.gfx').write_text('\n'.join(sprites) + '\n', encoding='utf-8')
    (ROOT / 'docs/auh_extra_art_bindings.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'events': len(EVENTS), 'ideas': len(IDEAS), 'decisions': len(DECISIONS), 'sprites': len(records), 'duplicates': 0}))
    return 0

if __name__ == '__main__':
    sys.exit(main())

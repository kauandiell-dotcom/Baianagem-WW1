"""Importa a arte dos eventos novos da Russia e da Alemanha a partir das copias instaladas da Workshop
(doadores somente leitura). Sem geracao de imagem. Recusa duplicatas exatas ou quase iguais contra o
proprio conjunto e contra todas as imagens de evento ja existentes no mod.

Saidas: gfx/event_pictures/ww1_ger_rus/*.dds, interface/ww1_ger_rus_rework_assets.gfx,
        docs/ger_rus_art_bindings.json (origem de cada imagem).
"""
from pathlib import Path
import hashlib
import json
import sys
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
WORKSHOP = Path('E:/SteamLibrary/steamapps/workshop/content/394360')
T, K = '3365515312', '2076426030'

# chave -> (doador, caminho sob gfx/event_pictures)
EVENTS = {
    # ---------------- Russia ----------------
    'sov_lena': (T, 'RUS/ww1_russia_27'),
    'sov_putilov': (T, 'RUS/ww1_russia_28'),
    'sov_supreme_command': (T, 'RUS/ww1_russia_91'),
    'sov_great_retreat': (T, 'RUS/ww1_russia_54'),
    'sov_duma_prorogued': (T, 'RUS/ww1_russia_73'),
    'sov_rasputin_murder': (T, 'RUS/ww1_russia_62'),
    'sov_army_wavers': (T, 'RUS/ww1_russia_55'),
    'sov_stolypin_harvest': (T, 'RUS/ww1_russia_9'),
    'sov_army_programme': (T, 'RUS/ww1_russia_18'),
    'sov_bread_lines': (T, 'RUS Revolution/report_event_rus_constituent_assembly_demonstrations'),
    'sov_petrograd_uprising': (T, 'RUS Revolution/report_february_revolution'),
    'sov_abdication': (T, 'RUS Revolution/rusrevolt_2'),
    'sov_dual_power': (T, 'RUS/ww1_russia_92'),
    'sov_april_theses': (T, 'RUS Revolution/rusrevolt_7'),
    'sov_july_days': (T, 'RUS/ww1_russia_31'),
    'sov_kornilov_crisis': (T, 'RUS Revolution/rusrevolt_4'),
    'sov_october': (T, 'RUS Revolution/rusrevolt_8'),
    'sov_kornilov_power': (T, 'SRA/kornilovites'),
    'sov_assembly_election': (T, 'RUS Revolution/report_event_rus_constituent_assembly_election'),
    'sov_assembly_dispersal': (T, 'RUS Revolution/report_event_rus_constituent_assembly_dispersal'),
    'sov_sovnarkom': (T, 'SOV/ww1_soviet_28'),
    'sov_civil_war': (T, 'SOV/report_event_yaroslavl_revolt'),
    'sov_czech_legion': (T, 'SIB/czech_corps'),
    'sov_kolchak': (T, 'SIB/kolchak_gov'),
    'sov_wrangel': (T, 'SRA/wrangel_1'),
    'sov_kronstadt': (T, 'SOV/ww1_soviet_24'),
    'sov_nep': (T, 'SOV/report_event_lenin_gorki'),
    'sov_ussr': (T, 'RUS Revolution/rusrevolt_19'),
    'sov_tsar_family': (T, 'RUS Revolution/report_tsar_family'),
    'sov_church_council': (T, 'RUS Civil War/report_event_zemsky_sobor'),
    'sov_finland': (T, 'RUS/ww1_russia_56'),
    'sov_ukraine': (T, 'RUS Revolution/report_ukraine_ww1'),
    'sov_baltic': (T, 'RUS/ww1_russia_6'),
    'sov_caucasus': (T, 'RUS/ww1_russia_43'),
    'sov_poland': (T, 'RUS Revolution/report_polish_sov_ww1'),
    # ---------------- Alemanha ----------------
    'ger_elections_1912': (T, 'GER/report_event_elections_1912'),
    'ger_zabern': (T, 'GER/report_event_zabern_affair'),
    'ger_burgfrieden': (T, 'GER/report_event_wilhelm_ii_with_generals'),
    'ger_moltke': (T, 'GER/report_event_moltke'),
    'ger_lusitania': (T, 'GER/report_event_unrestricted_submarine_warfare'),
    'ger_third_ohl': (T, 'GER/report_event_ohl_hindenburg'),
    'ger_berlin_strike': (T, 'GER/report_event_berlin_strike_1916'),
    'ger_hunger': (K, 'Europe/Germany/GFX_report_event_GER_hungry_people'),
    'ger_zimmermann': (T, 'GER/report_event_zimmermann_telegram'),
    'ger_peace_resolution': (K, 'Europe/Germany/GFX_report_event_GER_reichstag'),
    'ger_hertling': (T, 'GER/report_event_hertling'),
    'ger_spring_offensive': (T, 'GER/news_event_ludendorff_offensive'),
    'ger_january_strikes': (T, 'GER/report_event_german_empire_workers_strike'),
    'ger_max_von_baden': (T, 'GER/report_event_maximilian_von_baden'),
    'ger_kiel': (T, 'GER/report_event_high_seas_fleet'),
    'ger_republic': (T, 'GER/report_event_scheidemann_proclaiming_republic'),
    'ger_abdication': (T, 'GER/report_event_wilhelm_ii_abdication'),
    'ger_ebert_groener': (T, 'GER/report_event_ebert'),
    'ger_spartacists': (T, 'GER/report_event_spartacists'),
    'ger_weimar': (T, 'GER/report_event_weimar_national_assembly'),
    'ger_kapp': (T, 'GER/report_event_freikorps'),
    'ger_rathenau': (K, 'Europe/Germany/GFX_report_event_GER_Erzberger_Funeral'),
    'ger_ruhr': (K, 'Europe/Germany/GFX_report_event_GER_Reparations'),
    'ger_inflation': (K, 'Europe/Germany/GFX_report_event_GER_Hundred_Marks'),
    'ger_volksmarine': (T, 'GER/report_event_volksmarinedivision'),
    'ger_scuttling': (T, 'GER/news_event_scuttling_of_german_fleet'),
    'ger_russian_opportunity': (T, 'RUS/ww1_russia_5'),
}


def locate(mod, rel):
    base = WORKSHOP / mod / 'gfx' / 'event_pictures' / rel
    for ext in ('.png', '.dds', '.tga'):
        p = Path(str(base) + ext)
        if p.is_file():
            return p
    raise FileNotFoundError(str(base))


def ahash(im):
    g = ImageOps.grayscale(im.convert('RGBA')).resize((16, 16), Image.Resampling.LANCZOS)
    px = list(g.getdata())
    avg = sum(px) / len(px)
    return int(''.join('1' if p > avg else '0' for p in px), 2)


def ham(a, b):
    return bin(a ^ b).count('1')


def main():
    existing = []
    for p in (ROOT / 'gfx/event_pictures').rglob('*'):
        if p.suffix.lower() in ('.dds', '.png', '.tga') and 'ww1_ger_rus' not in p.as_posix():
            try:
                existing.append((p, ahash(Image.open(p))))
            except Exception:
                pass
    seen_px, seen_h, records, sprites, problems = {}, [], [], ['spriteTypes = {'], []
    for name, (mod, rel) in EVENTS.items():
        src = locate(mod, rel)
        im = Image.open(src).convert('RGBA')
        out = ImageOps.fit(im, (450, 250), Image.Resampling.LANCZOS)
        px = hashlib.sha256(out.tobytes()).hexdigest()
        h = ahash(out)
        if px in seen_px:
            problems.append((name, 'duplicata exata de', seen_px[px]))
        for on, oh in seen_h:
            if ham(h, oh) <= 8:
                problems.append((name, 'quase igual a', on))
        for p, oh in existing:
            if ham(h, oh) <= 6:
                problems.append((name, 'quase igual a imagem existente', p.relative_to(ROOT).as_posix()))
        seen_px[px] = name
        seen_h.append((name, h))
        dest = ROOT / 'gfx/event_pictures/ww1_ger_rus' / (name + '.dds')
        dest.parent.mkdir(parents=True, exist_ok=True)
        out.save(dest)
        tex = dest.relative_to(ROOT).as_posix()
        sprites.append(f' spriteType = {{ name = "GFX_event_WW1_{name}" texturefile = "{tex}" }}')
        records.append(dict(sprite=f'GFX_event_WW1_{name}', donor_id=mod, source_relative=f'gfx/event_pictures/{rel}',
                            source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(), texture=tex))
    sprites.append('}')
    if problems:
        print(json.dumps(problems, ensure_ascii=False, indent=1))
        return 1
    (ROOT / 'interface/ww1_ger_rus_rework_assets.gfx').write_text('\n'.join(sprites) + '\n', encoding='utf-8')
    (ROOT / 'docs/ger_rus_art_bindings.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'eventos': len(EVENTS), 'duplicatas': 0}))
    return 0


if __name__ == '__main__':
    sys.exit(main())

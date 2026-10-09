# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

# Known custom historical name overrides for maximum authenticity
OVERRIDES = {
    # Austria-Hungary
    "AUH_artur_arz_von_straussenberg": "Artur Arz von Straußenberg",
    "AUH_blasius_schemua": "Blasius Schemua",
    "AUH_friedrich_von_beck_rzikowsky": "Friedrich von Beck-Rzikowsky",
    "AUH_august_urbanski": "August Urbanski von Ostrymiecz",
    "AUH_franz_von_holub": "Franz von Holub",
    "AUH_rudolf_montecuccoli": "Rudolf Montecuccoli",
    "AUH_maximilian_njegovan": "Maximilian Njegovan",
    "AUH_karl_kailer_von_kagenfels": "Karl Kailer von Kagenfels",
    "AUH_maximilian_daublebsky_von_sterneck": "Maximilian Daublebsky von Sterneck",
    "AUS_archduke_franz_ferdinand": "Erzherzog Franz Ferdinand",
    "AUH_emil_uzelac": "Emil Uzelac",
    "AUH_agenor_goluchowski": "Agenor Gołuchowski",
    "AUH_oskar_von_hranilovic_czvetassin": "Oskar von Hranilović Czvetassin",
    "AUH_alois_lexa_von_aehrenthal": "Alois Lexa von Aehrenthal",
    "AUS_istvan_tisza": "István Tisza",
    "AUH_gyula_andrassy": "Gyula Andrássy",
    "AUH_ottokar_czernin": "Ottokar Czernin",
    "AUH_gabor_ugron": "Gábor Ugron",
    "AUH_leon_von_bilinski": "Leon von Biliński",
    "AUH_eugen_hordliczka": "Eugen Hordliczka",
    "AUS_charles_i": "Karl I",
    "AUS_archduke_friedrich": "Erzherzog Friedrich",
    "AUS_svetozar_borojevic_von_bojna": "Svetozar Borojević von Bojna",
    "AUS_viktor_dankl_von_krasnik": "Viktor Dankl von Krasnik",
    "AUS_stogersteiner_von_steinstatten": "Rudolf Stöger-Steiner von Steinstätten",
    "AUS_karl_von_pflanzerbaltin": "Karl von Pflanzer-Baltin",
    "AUS_von_krobatin": "Alexander von Krobatin",
    "AUS_anton_liposcak": "Anton Lipošćak",
    "AUS_anton_haus": "Anton Haus",
    "AUS_hermann_von_spaun": "Hermann von Spaun",
    "AUS_miklos_horthy": "Miklós Horthy",

    # Belgium
    "BEL_cyriaque_gillain": "Cyriaque Gillain",
    "BEL_rucqouy": "Louis Ruquoy",
    "BEL_ridder_de_selliers_de_moranville": "Antonin de Selliers de Moranville",
    "BEL_henry_h_maglinse": "Henry Maglinse",
    "BEL_felix_wielemans": "Félix Wielemans",
    "BEL_jules_davignon": "Julien Davignon",
    "BEL_baron_beyens": "Baron Eugène Beyens",
    "BEL_geraard_cooreman": "Gerard Cooreman",
    "BEL_baron_wahis": "Baron Théophile Wahis",
    "BEL_joseph_hellebaut": "Joseph Hellebaut",
    "BEL_marcel_de_crombrugghe": "Marcel de Crombrugghe de Looringhe",
    "BEL_count_carton_de_wiart": "Henri Carton de Wiart",
    "BEL_edwart_anseele": "Edward Anseele",
    "BEL_leon_delacroix": "Léon Delacroix",
    "BEL_leman": "Gérard Leman",
    "BEL_emile_dossin_de_saintgeorges": "Émile Dossin de Saint-Georges",
    "BEL_albert_advisor": "Albert I",
    "BEL_dixmude": "Pierre de Fassignies (Dixmude)",
    "BEL_georges_moulaert": "Georges Moulaert",

    # Germany
    "GER_otto_von_lossow": "Otto von Lossow",
    "GER_wilhelm_groener": "Wilhelm Groener",
    "GER_helmuth_von_moltke": "Helmuth von Moltke d. J.",
    "GER_rudiger_von_der_goltz": "Rüdiger von der Goltz",
    "GER_walther_reinhardt": "Walther Reinhardt",
    "GER_adolf_wild_von_hohenborn": "Adolf Wild von Hohenborn",
    "GER_josias_von_heeringen": "Josias von Heeringen",
    "GER_wilhelm_heye": "Wilhelm Heye",
    "GER_von_lettowvorbeck": "Paul von Lettow-Vorbeck",
    "GER_von_quast": "Ferdinand von Quast",
    "GER_von_bothmer": "Felix von Bothmer",

    # France
    "FRA_jean_jaures": "Jean Jaurès",
    "FRA_charles_dumont": "Charles Dumont",
    "FRA_rene_viviani": "René Viviani",
    "FRA_maurice_sarrail": "Maurice Sarrail",
    "FRA_jacques_schneider": "Jacques Schneider",
    "FRA_auguste_edouard_hirschauer": "Auguste Édouard Hirschauer",
    "FRA_louis_pivet": "Louis Pivet",

    # United Kingdom
    "ENG_frederick_roberts": "Lord Frederick Roberts",
    "ENG_frederick_sykes": "Sir Frederick Sykes",
    "ENG_frederick_lambart": "Frederick Lambart, Lord Cavan",
    "ENG_garrett_o_moore_creagh": "Sir O'Moore Creagh",
    "ENG_george_macaulay_kirkpatrick": "George Macaulay Kirkpatrick",
    "ENG_st_john_brodrick": "St John Brodrick",
    "ENG_hugh_trenchard": "Hugh Trenchard",
    "ENG_charles_vaughan_lee": "Charles Vaughan-Lee",
    "ENG_jfc_fuller": "J. F. C. Fuller",
    "ENG_navy_churchill": "Winston Churchill",
    "EGY_edmund_allenby": "Edmund Allenby",

    # Italy
    "ITA_eduardo_moroni": "Edoardo Moroni",
    "ITA_antonio_salandra": "Antonio Salandra",
    "ITA_vittorio_italico_zupelli": "Vittorio Italico Zupelli",
    "ITA_camillo_corsi": "Camillo Corsi",
    "ITA_guido_buffarini_guidi": "Guido Buffarini Guidi",
    "ITA_carlo_porro": "Carlo Porro",
    "ITA_domenico_grandi": "Domenico Grandi",
    "ITA_paolo_morrone": "Paolo Morrone",
    "ITA_mario_calderara": "Mario Calderara",
    "ITA_paolo_spingardi": "Paolo Spingardi",
    "ITA_arrigo_tessari": "Arrigo Tessari",
    "ITA_felice_napoleone_canevaro": "Felice Napoleone Canevaro",
    "ITA_leone_viale": "Leone Viale",
    "ITA_giuseppe_vaccari": "Giuseppe Vaccari",
    "ITA_antonino_paterne_castello": "Antonino Paternò Castello",
    "ITA_giulio_douhet": "Giulio Douhet",
    "ITA_luigi_luzzatti": "Luigi Luzzatti",
    "ITA_luigi_pelloux": "Luigi Pelloux",
    "ITA_giampietro_pellegrini": "Giampietro Pellegrini",
    "ITA_vittorio_alfieri": "Vittorio Alfieri",
    "ITA_pier_angelo_brandimarte": "Pier Angelo Brandimarte",
    "ITA_paolo_boselli": "Paolo Boselli",
    "ITA_duca_degli_abruzzi": "Luigi Amedeo, Duca degli Abruzzi",
    "ITA_luigi_facta": "Luigi Facta",

    # Portugal
    "POR_jose_norton_de_matos": "José Norton de Matos",
    "POR_tomas_garcia_rosado": "Tomás Garcia Rosado",
    "POR_jose_carlos_de_maia": "José Carlos de Maia",
    "POR_joao_martins_de_carvalho": "João Martins de Carvalho",
    "POR_joao_jose_sinel_de_cordes": "João José Sinel de Cordes",
    "POR_antonio_caetano_macieira_junior": "António Caetano Macieira Júnior",
    "POR_joaquim_pimenta_de_castro": "Joaquim Pimenta de Castro",
    "POR_antonio_rodrigues_ribeiro": "António Rodrigues Ribeiro",
    "POR_joao_do_canto_e_castro": "João do Canto e Castro",
    "POR_antonio_maria_baptista": "António Maria Baptista",
    "POR_vitor_hugo_de_azevedo_coutinho": "Vítor Hugo de Azevedo Coutinho",
    "POR_afonso_augusto_da_costa": "Afonso Augusto da Costa",
    "POR_joao_de_sousa_barbosa": "João de Sousa Barbosa",
    "POR_antonio_teixeira_de_sousa": "António Teixeira de Sousa",
    "POR_antonio_joaquim_granjo": "António Joaquim Granjo",

    # Ottoman / Turkey
    "TUR_huseyin_hilmi": "Hüseyin Hilmi Pasha",
    "TUR_ahmed_izzet": "Ahmed Izzet Pasha",
    "TUR_mustafa_ismet": "Mustafa İsmet İnönü",
    "TUR_erich_von_falkenhayn": "Erich von Falkenhayn",
    "TUR_otto_liman_von_sanders": "Otto Liman von Sanders",
    "TUR_ethem_nejat": "Ethem Nejat",
    "TUR_huseyin_rauf": "Hüseyin Rauf Orbay",
    "TUR_ahmed_nessimy": "Ahmed Nessimy Bey",
    "TUR_djemal_pasha": "Ahmed Djemal Pasha",
    "TUR_ahmed_tevfik": "Ahmed Tevfik Pasha",
    "TUR_mehmet_nazim": "Mehmet Nâzım Bey",
    "TUR_talaat_pasha": "Mehmed Talaat Pasha",
    "TUR_mehemmed_naby": "Mehmed Naby Bey",

    # Bulgaria
    "BUL_sava_savov": "Sava Savov",
    "BUL_stefan_nerezov": "Stefan Nerezov",
    "BUL_konstantin_zhostov": "Konstantin Zhostov",
    "BUL_radko_dimitriev": "Radko Dimitriev",
    "BUL_vicho_dikov": "Vicho Dikov",
    "BUL_mihail_savov": "Mihail Savov",
    "BUL_nikola_topaldzhikov": "Nikola Topaldzhikov",
    "BUL_petar_midilev": "Petar Midilev",
    "BUL_hristo_burmov": "Hristo Burmov",
    "BUL_pravoslav_tenev": "Pravoslav Tenev",
    "BUL_lazar_draganov": "Lazar Draganov",
    "BUL_stepan_paprikov": "Stefan Paprikov",
    "BUL_aleksandyr_dimitrov": "Aleksandar Dimitrov",
    "BUL_kalin_naidenov": "Kalin Naydenov",
    "BUL_konstantin_kirkov": "Konstantin Kirkov",
    "BUL_vasil_zlatarov": "Vasil Zlatarov",
    "BUL_radul_milkov": "Radul Milkov",
    "BUL_nikola_genadiev": "Nikola Genadiev",
    "BUL_marko_tourlakov": "Marko Turlakov",
    "BUL_rayko_daskalov": "Rayko Daskalov",
    "BUL_ivan_evstratiev_geshov": "Ivan Evstratiev Geshov",
    "BUL_mikhail_madzharov": "Mikhail Madzharov",
    "BUL_todor_ivanchov": "Todor Ivanchov",
    "BUL_dobrev": "Konstantin Dobrev",

    # Canada
    "CAN_lloyd_samuel_breadner": "Lloyd Samuel Breadner",
    "CAN_tasker_cook": "Sir Tasker Cook",
    "CAN_george_pearkes": "George Pearkes",
    "CAN_john_murchie": "John Murchie",
    "CAN_ian_a_mackenzie": "Ian Alistair Mackenzie",
    "CAN_c_d_howe": "C. D. Howe",
    "CAN_newton_wesley_rowell": "Newton Wesley Rowell",
    "CAN_harold_edwards": "Harold Edwards",
    "CAN_leo_richer_lafleche": "Léo Richer LaFlèche",
    "CAN_george_jones": "George C. Jones",
    "CAN_alasdair_murray": "Alasdair Murray",
    "CAN_percy_nelles": "Percy W. Nelles",

    # Serbia
    "SER_petar_pesic": "Petar Pešić",
    "SER_mihailo_rasic": "Mihailo Rašić",
    "SER_milos_vasic": "Miloš Vasić",
    "SER_stevan_hadzic": "Stevan Hadžić",
    "SER_zivko_pavlovic": "Živko Pavlović",
    "SER_jovan_jovanovic_pizon": "Jovan Jovanović Pižon",
    "SER_lazar_pacu": "Lazar Paču",
    "SER_mihailo_gavrilovic": "Mihailo Gavrilović",
    "SER_stojan_novakovic": "Stojan Novaković",
    "SER_momcilo_nincic": "Momčilo Ninčić",
    "SER_stojan_protic": "Stojan Protić",
    "SER_milovan_milovanovic": "Milovan Milovanović",
    "SER_svetozar_pribicevic": "Svetozar Pribićević",
    "SER_duro_dakovic": "Đuro Đaković",
    "SER_milenko_vesnic": "Milenko Vesnić",
    "SER_kosta_miletic": "Kosta Miletić",

    # Romania
    "ROM_constantin_balescu": "Constantin Bălescu",
    "ROM_constantin_niculescu_rizea": "Constantin Niculescu-Rizea",
    "ROM_istrate_micescu": "Istrate Micescu",
    "ROM_mihail_moruzov": "Mihail Moruzov",
    "ROM_ioan_popescu": "Ioan Popescu",
    "ROM_aurel_vlad": "Aurel Vlad",
    "ROM_Monkey_Man": "Gheorghe Mărdărescu",
    "ROM_dumitru_iliescu": "Dumitru Iliescu",
    "ROM_constantin_cristescu": "Constantin Cristescu",
    "ROM_vintila_bratianu": "Vintilă Brătianu",
    "ROM_nicolae_titulescu": "Nicolae Titulescu",
    "ROM_nicolae_negru": "Nicolae Negru",
    "ROM_alexandru_marghiloman": "Alexandru Marghiloman",
    "ROM_vasile_zottu": "Vasile Zottu",

    # Greece
    "GRE_Maurice_Sarrail": "Maurice Sarrail",
    "GRE_zymvrakakis": "Epameinondas Zymvrakakis",
    "GRE_constantin_moschopoulos": "Konstantinos Moschopoulos",

    # USA
    "USA_edward_house": "Colonel Edward M. House",
    "USA_george_b_mcclellan": "George B. McClellan Jr.",

    # Specific names with hyphens/special chars
    "Kofoed-Hansen": "Kofoed-Hansen",
    "DEN_kofoed_hansen": "Kofoed-Hansen",
    "Topsøe-Jensen": "Topsøe-Jensen",
    "DEN_topsoe_jensen": "Topsøe-Jensen",
    "Juel-Brockdorff": "Juel-Brockdorff",
    "DEN_juelbrockdorff": "Juel-Brockdorff",
    "Niculescu-Rizea": "Niculescu-Rizea",
    "ROM_niculescurizea": "Niculescu-Rizea",
    "Mörcke": "Mörcke",
    "SWE_morcke": "Mörcke",
    "Nordenskjöld": "Nordenskjöld",
    "SWE_nordenskjold": "Nordenskjöld",
    "Nyström": "Nyström",
    "SWE_nystrom": "Nyström",
    "Bergström": "Bergström",
    "SWE_bergstrom": "Bergström",
    "Hammarskjöld": "Hammarskjöld",
    "SWE_hammarskjold": "Hammarskjöld",
    "Audéoud": "Audéoud",
    "SWI_audeoud": "Audéoud",
    "Büel": "Büel",
    "SWI_buel": "Büel",
    "Brügger": "Brügger",
    "SWI_bruegger": "Brügger"
}

def clean_key_to_name(tag, key):
    if key in OVERRIDES:
        return OVERRIDES[key]
        
    s = key
    prefixes = [tag + "_", "AUH_", "EGY_"]
    for p in prefixes:
        if s.startswith(p):
            s = s[len(p):]
            break
            
    particles = {"von", "van", "de", "der", "den", "del", "della", "degli", "da", "do", "dos", "das", "du", "di", "e", "d", "l", "la"}
    
    parts = s.split("_")
    capitalized = []
    for idx, word in enumerate(parts):
        w_lower = word.lower()
        if idx > 0 and w_lower in particles:
            capitalized.append(w_lower)
        elif w_lower == "ii":
            capitalized.append("II")
        elif w_lower == "iii":
            capitalized.append("III")
        elif w_lower == "iv":
            capitalized.append("IV")
        elif w_lower == "jr":
            capitalized.append("Jr.")
        elif w_lower == "sr":
            capitalized.append("Sr.")
        else:
            capitalized.append(word.capitalize())
            
    return " ".join(capitalized)

# Parse ALL characters directly from common/characters/*.txt
master_loc = dict(OVERRIDES)

for p in sorted((ROOT / "common/characters").glob("*.txt")):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    tag = p.stem
    clean_txt = re.sub(r'#.*', '', txt)
    m = re.search(r'characters\s*=\s*\{([\s\S]*)\}', clean_txt)
    if not m:
        continue
    body = m.group(1)
    
    depth = 0
    token_start = None
    curr_char_id = None
    i = 0
    n = len(body)
    while i < n:
        c = body[i]
        if c == '{':
            if depth == 0:
                prefix = body[token_start:i].strip()
                m_id = re.search(r'([a-zA-Z0-9_]+)\s*=$', prefix)
                curr_char_id = m_id.group(1) if m_id else "UNKNOWN"
                block_start = i
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0 and curr_char_id:
                char_body = body[block_start:i+1]
                name_m = re.search(r'\bname\s*=\s*(?:\"([^\"]+)\"|([a-zA-Z0-9_\.\-]+))', char_body)
                name_val = name_m.group(1) or name_m.group(2) if name_m else None
                
                # If name_val is a code key (no spaces)
                if name_val:
                    if " " not in name_val:
                        if name_val not in master_loc:
                            master_loc[name_val] = clean_key_to_name(tag, name_val)
                    else:
                        # Even if literal name, map it
                        pass
                else:
                    # No name specified, uses curr_char_id
                    if curr_char_id not in master_loc:
                        master_loc[curr_char_id] = clean_key_to_name(tag, curr_char_id)
                        
                # Also ensure curr_char_id has a mapping
                if curr_char_id not in master_loc:
                    master_loc[curr_char_id] = clean_key_to_name(tag, curr_char_id)
                    
                curr_char_id = None
                token_start = i + 1
        elif depth == 0 and not body[i].isspace() and token_start is None:
            token_start = i
        i += 1

print(f"Total master advisor loc entries generated: {len(master_loc)}")

# Write English file
en_lines = ["l_english:"]
for k, v in sorted(master_loc.items()):
    en_lines.append(f' {k}:0 "{v}"')

p_en = ROOT / "localisation" / "english" / "ww1_advisors_l_english.yml"
p_en.write_bytes(b"\xef\xbb\xbf" + "\n".join(en_lines).encode("utf-8") + b"\n")
print(f"Written {p_en}")

# Write Portuguese file
pt_lines = ["l_braz_por:"]
for k, v in sorted(master_loc.items()):
    pt_lines.append(f' {k}:0 "{v}"')

p_pt = ROOT / "localisation" / "braz_por" / "ww1_advisors_l_braz_por.yml"
p_pt.write_bytes(b"\xef\xbb\xbf" + "\n".join(pt_lines).encode("utf-8") + b"\n")
print(f"Written {p_pt}")

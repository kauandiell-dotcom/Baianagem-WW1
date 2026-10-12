# scripts/apply_uk_rework.py
# Applies the full clean rework to the United Kingdom focus tree, GFX, ideas and localization.

import re
import os
import sys

sys.path.insert(0, '.')

from scripts.eng_data_politics import POLITICS_DATA
from scripts.eng_data_economy import ECONOMY_DATA
from scripts.eng_data_diplomacy import DIPLOMACY_DATA
from scripts.eng_data_military import MILITARY_DATA
from scripts.eng_data_navy_air import NAVY_AIR_DATA
from scripts.eng_data_tech_intel import TECH_INTEL_DATA

# Combine all 200 focus data
ALL_FOCUS_DATA = {}
for name, d in [
    ('Politics', POLITICS_DATA),
    ('Economy', ECONOMY_DATA),
    ('Diplomacy', DIPLOMACY_DATA),
    ('Military', MILITARY_DATA),
    ('Navy/Air', NAVY_AIR_DATA),
    ('Tech/Intel', TECH_INTEL_DATA)
]:
    for k, v in d.items():
        ALL_FOCUS_DATA[k] = v

print(f"Total focus data entries: {len(ALL_FOCUS_DATA)}")

# 5 Core Pillars (Tiers 1-3) + Decision Buffs Localisation
IDEAS_LOC = {
    # Pilar 1: Naval
    'ENG_two_power_standard': {
        'pt': ("O Padrão das Duas Potências Navais", "A doutrina naval de manter uma frota de guerra superior à soma das duas potências navais seguintes assegura o domínio inquestionável dos mares."),
        'en': ("The Two-Power Standard", "The strategic doctrine maintaining a battle fleet equal to or surpassing the combined strength of the next two naval powers guarantees command of the sea.")
    },
    'ENG_two_power_standard_t2': {
        'pt': ("Mobilização da Grand Fleet", "A concentração da Grand Fleet em Scapa Flow e Cromarty estabelece a vigilância hermética do Mar do Norte e prontidão de combate."),
        'en': ("Grand Fleet Mobilisation", "Concentration of the Grand Fleet at Scapa Flow and Cromarty enforces a vigilant northern blockade and instant surface fleet readiness.")
    },
    'ENG_two_power_standard_t3': {
        'pt': ("Senhora dos Mares & Detecção Acústica", "Doutrina anti-submarina de ponta com sonares ASDIC, cargas de profundidade e controle absoluto das rotas marítimas vitais."),
        'en': ("Mistress of the Seas & ASDIC Dominance", "Cutting-edge anti-submarine acoustics, hydrophones, depth charges, and comprehensive convoy escort networks protect imperial commerce.")
    },
    # Pilar 2: Economia
    'ENG_city_of_london_credit': {
        'pt': ("O Centro Financeiro da City de Londres", "A City de Londres como o centro financeiro e comercial do mundo garante crédito global barato, bens de consumo abundantes e liquidez imperial."),
        'en': ("City of London Global Credit", "The City of London stands as the preeminent financial hub of the globe, providing unparalleled commercial borrowing, cheap consumer goods, and sterling liquidity.")
    },
    'ENG_city_of_london_credit_t2': {
        'pt': ("Ministério de Munições de Lloyd George", "O Ministério de Munições assume o controle direto de fábricas e estaleiros, convertendo oficinas civis em colossais complexos de cartuchos e peças pesadas."),
        'en': ("Lloyd George's Ministry of Munitions", "The Ministry of Munitions takes direct wartime control over private industrial plants, converting factories into colossal armament complexes.")
    },
    'ENG_city_of_london_credit_t3': {
        'pt': ("Mobilização Industrial Total & Estabilização da Libra", "A indústria britânica opera com eficiência máxima, superando qualquer escassez material e reequilibrando a balança orçamentária do pós-guerra."),
        'en': ("Total Industrial Mobilisation & Sterling Resilience", "British war manufacturing operates at peak output, overcoming material shortages while securing post-war financial stability.")
    },
    # Pilar 3: Exército
    'ENG_professional_bef': {
        'pt': ("Exército Profissional de Voluntários (BEF)", "Uma força expedicionária altamente profissional e adestrada em tiro rápido com fuzis Lee-Enfield, porém limitada pelo modelo estritamente voluntário."),
        'en': ("The Professional Expeditionary Force (BEF)", "An elite, highly disciplined standing army famed for its rapid-fire rifle marksmanship, yet strictly constrained by peacetime voluntary recruitment.")
    },
    'ENG_professional_bef_t2': {
        'pt': ("Novos Exércitos de Kitchener", "Milhões de cidadãos voluntários atendem ao chamado imperial de Kitchener, transformando o pequeno exército regular em uma poderosa massa de infantaria moderna."),
        'en': ("Kitchener's New Armies", "Millions of patriotic volunteers answer Lord Kitchener's call, expanding Britain's small regular core into a formidable mass citizen army.")
    },
    'ENG_professional_bef_t3': {
        'pt': ("O Martelo Continental & Doutrina Blindada", "A força imperial atinge a maturidade tática interarmas, combinando artilharia rastejante, fuzis-metralhadoras Lewis e os blindados pesados de combate."),
        'en': ("The Continental Hammer & Combined Arms", "Imperial field armies master modern combined arms tactics, integrating creeping barrages, automatic fire, and heavy breakthrough tanks.")
    },
    # Pilar 4: Rede Imperial
    'ENG_the_imperial_web': {
        'pt': ("A Malha do Império Global", "Cadeias de estações de carvão, cabos telegráficos submarinos e relações comerciais privilegiadas unem os quatro cantos dos Domínios e Colônias."),
        'en': ("The Imperial Web", "Coaling stations, undersea telegraph cables, and preferential trading links bind the Dominions and Crown Colonies into an indivisible global network.")
    },
    'ENG_the_imperial_web_t2': {
        'pt': ("Mobilização Expedicionária dos Domínios", "Divisões canadenses, australianas (ANZAC), neozelandesas e indianas atravessam os oceanos para lutar ombro a ombro nos teatros mundiais."),
        'en': ("Dominion Expeditionary Mobilisation", "Divisions from Canada, Australia, New Zealand, South Africa, and India deploy across global fronts, bound by common imperial loyalty.")
    },
    'ENG_the_imperial_web_t3': {
        'pt': ("Gabinete de Guerra Imperial", "Primeiros-ministros dos Domínios compartilham a direção estratégica da guerra em Londres, fundando uma federação de defesa commonwealth permanente."),
        'en': ("The Imperial War Cabinet", "Dominion prime ministers sit in London alongside the British government, co-directing global strategy as an equal imperial partnership.")
    },
    # Pilar 5: Irlanda
    'ENG_irish_home_rule_tension': {
        'pt': ("A Questão do Home Rule Irlandês", "Disputas parlamentares acirradas e milícias sectárias armadas em Ulster e Dublin ameaçam a coesão do Reino Unido."),
        'en': ("The Irish Home Rule Crisis", "Fierce parliamentary deadlock and armed sectarian militias in Ulster and Dublin threaten the constitutional stability of the United Kingdom.")
    },
    'ENG_irish_home_rule_suspended': {
        'pt': ("Home Rule Suspenso na Guerra", "Nacionalistas e unionistas concordam com uma trégua parlamentar temporária durante o esforço bélico contra os Impérios Centrais."),
        'en': ("Home Rule Suspended for War", "Nationalist and Unionist leaders accept a temporary parliamentary armistice to present a united front against hostile powers.")
    },
    'ENG_irish_home_rule_compromise': {
        'pt': ("Acordo Constitucional Irlandês", "Concessões mútuas e garantias institucionais pacificam a questão irlandesa, restaurando a tranquilidade interna na Grã-Bretanha."),
        'en': ("Irish Constitutional Compromise", "Negotiated devolution safeguards regional sensibilities, cementing domestic peace and civilian recruitment stability.")
    },
    # Modificadores de Decisões
    'ENG_ww1_district_contracts_buff': {
        'pt': ("Contratos Distritais Fabris", "Linhas de crédito prioritárias aceleram a expansão de usinas metalúrgicas e oficinas de material bélico."),
        'en': ("District Production Contracts", "Allocated civilian contracts accelerate munitions output and state industrial construction.")
    },
    'ENG_ww1_seaplane_patrols_buff': {
        'pt': ("Patrulha Costeira de Hidroaviões", "Esquadrões de hidroaviões vasculham as enseadas e rotas costeiras em busca de submarinos e minas."),
        'en': ("Seaplane Coastal Patrol Rota", "Naval seaplane rotas scour coastal approaches and shipping lanes for hostile U-boats and minefields.")
    },
    'ENG_ww1_city_credit_line_buff': {
        'pt': ("Linha de Crédito da City de Londres", "O Banco da Inglaterra e os sindicatos bancários da City fornecem liquidez orçamentária emergencial para a Coroa."),
        'en': ("City of London Credit Facility", "The Bank of England and private banking houses issue emergency discount lines to ease government finances.")
    }
}

# 1. Update common/national_focus/uk.txt
print("Updating common/national_focus/uk.txt...")
with open('common/national_focus/uk.txt', 'r', encoding='utf-8') as f:
    uk_text = f.read()

def parse_and_replace_uk_focuses(content):
    pos = 0
    result = []
    replaced_count = 0
    
    while pos < len(content):
        f_idx = content.find('focus = {', pos)
        if f_idx == -1:
            result.append(content[pos:])
            break
            
        result.append(content[pos:f_idx])
        
        brace_depth = 0
        end_idx = f_idx
        for i in range(f_idx, len(content)):
            if content[i] == '{':
                brace_depth += 1
            elif content[i] == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    end_idx = i + 1
                    break
                    
        focus_chunk = content[f_idx:end_idx]
        id_match = re.search(r'\bid\s*=\s*(\w+)', focus_chunk)
        if id_match:
            fid = id_match.group(1)
            if fid in ALL_FOCUS_DATA:
                data = ALL_FOCUS_DATA[fid]
                new_reward_body = data['reward']
                
                orig_events = re.findall(r'country_event\s*=\s*\{[^}]+\}', focus_chunk)
                orig_flags = re.findall(r'set_country_flag\s*=\s*(\w+)', focus_chunk)
                
                extra_lines = []
                for ev in orig_events:
                    if ev not in new_reward_body:
                        extra_lines.append(ev)
                for fl in orig_flags:
                    fl_str = f"set_country_flag = {fl}"
                    if fl_str not in new_reward_body:
                        extra_lines.append(fl_str)
                        
                if extra_lines:
                    combined_reward = new_reward_body + "\n" + "\n".join(extra_lines)
                else:
                    combined_reward = new_reward_body
                    
                reward_lines = [f"   {line.strip()}" for line in combined_reward.strip().split('\n') if line.strip()]
                formatted_reward = "  completion_reward = {\n" + "\n".join(reward_lines) + "\n  }"
                
                cr_start = focus_chunk.find('completion_reward = {')
                if cr_start != -1:
                    cr_depth = 0
                    cr_end = cr_start
                    for ci in range(cr_start, len(focus_chunk)):
                        if focus_chunk[ci] == '{':
                            cr_depth += 1
                        elif focus_chunk[ci] == '}':
                            cr_depth -= 1
                            if cr_depth == 0:
                                cr_end = ci + 1
                                break
                    focus_chunk = focus_chunk[:cr_start] + formatted_reward + focus_chunk[cr_end:]
                    replaced_count += 1
                    
        result.append(focus_chunk)
        pos = end_idx
        
    print(f"Replaced completion_reward in {replaced_count} focuses in uk.txt.")
    return "".join(result)

updated_uk_text = parse_and_replace_uk_focuses(uk_text)
with open('common/national_focus/uk.txt', 'w', encoding='utf-8') as f:
    f.write(updated_uk_text)
print("Updated common/national_focus/uk.txt successfully!")

# 2. Localisation Generation
print("Generating Brazilian Portuguese localization...")
with open('localisation/braz_por/ww1_britain_l_braz_por.yml', 'r', encoding='utf-8-sig', errors='ignore') as f:
    orig_pt_lines = f.readlines()

header_pt = [line.rstrip('\r\n') for line in orig_pt_lines[:54]]
pt_out = ['\ufeffl_braz_por:']
for line in header_pt[1:]:
    pt_out.append(line)

# Shortcuts & Root Focus
pt_out.append('\n # --- Atalhos de Navegacao e Foco Raiz ---')
pt_out.append(' ENG_ww1_shortcut_politics:0 "Política Imperial & Parlamento"')
pt_out.append(' ENG_ww1_shortcut_economy:0 "Indústria & Finanças da City"')
pt_out.append(' ENG_ww1_shortcut_diplomacy:0 "Diplomacia & Relações do Império"')
pt_out.append(' ENG_ww1_shortcut_navy:0 "Royal Navy & Domínio dos Mares"')
pt_out.append(' ENG_ww1_shortcut_army:0 "British Army & Força Expedicionária"')
pt_out.append(' ENG_ww1_1911_1923:0 "O Império Britânico na Grande Guerra"')
pt_out.append(' ENG_ww1_1911_1923_desc:0 "O Império Britânico se estende por todos os continentes, garantindo a paz mundial e o equilíbrio europeu sob a supremacia inquestionável da Royal Navy e das finanças de Londres."')

pt_out.append('\n # --- Ideias e Modificadores Canônicos Britânicos ---')
for idea_id, loc in sorted(IDEAS_LOC.items()):
    t, d = loc['pt']
    pt_out.append(f' {idea_id}:0 "{t}"')
    pt_out.append(f' {idea_id}_desc:0 "{d}"')

pt_out.append('\n # --- Focos Nacionais do Reino Unido (WW1) ---')
for fid, data in ALL_FOCUS_DATA.items():
    t = data['pt_t']
    d = data['pt_d']
    pt_out.append(f' {fid}:0 "{t}"')
    pt_out.append(f' {fid}_desc:0 "{d}"')

with open('localisation/braz_por/ww1_britain_l_braz_por.yml', 'w', encoding='utf-8-sig') as f:
    f.write("\n".join(pt_out) + "\n")
print("Wrote localisation/braz_por/ww1_britain_l_braz_por.yml with UTF-8 BOM!")

print("Generating English localization...")
with open('localisation/english/ww1_britain_l_english.yml', 'r', encoding='utf-8-sig', errors='ignore') as f:
    orig_en_lines = f.readlines()

header_en = [line.rstrip('\r\n') for line in orig_en_lines[:54]]
en_out = ['\ufeffl_english:']
for line in header_en[1:]:
    en_out.append(line)

# Shortcuts & Root Focus
en_out.append('\n # --- Navigation Shortcuts & Root Focus ---')
en_out.append(' ENG_ww1_shortcut_politics:0 "Imperial Politics & Parliament"')
en_out.append(' ENG_ww1_shortcut_economy:0 "Industry & City Finance"')
en_out.append(' ENG_ww1_shortcut_diplomacy:0 "Diplomacy & Imperial Relations"')
en_out.append(' ENG_ww1_shortcut_navy:0 "The Royal Navy & Command of the Seas"')
en_out.append(' ENG_ww1_shortcut_army:0 "The British Army & Expeditionary Force"')
en_out.append(' ENG_ww1_1911_1923:0 "The British Empire in the Great War"')
en_out.append(' ENG_ww1_1911_1923_desc:0 "The British Empire spans every ocean and continent, preserving global order and European equilibrium through naval mastery and industrial preeminence."')

en_out.append('\n # --- British Canonical Ideas & Modifiers ---')
for idea_id, loc in sorted(IDEAS_LOC.items()):
    t, d = loc['en']
    en_out.append(f' {idea_id}:0 "{t}"')
    en_out.append(f' {idea_id}_desc:0 "{d}"')

en_out.append('\n # --- British Empire National Focuses (WW1) ---')
for fid, data in ALL_FOCUS_DATA.items():
    t = data['en_t']
    d = data['en_d']
    en_out.append(f' {fid}:0 "{t}"')
    en_out.append(f' {fid}_desc:0 "{d}"')

with open('localisation/english/ww1_britain_l_english.yml', 'w', encoding='utf-8-sig') as f:
    f.write("\n".join(en_out) + "\n")
print("Wrote localisation/english/ww1_britain_l_english.yml with UTF-8 BOM!")

print("\n=== UK CLEAN REWORK APPLIED COMPREHENSIVELY! ===")

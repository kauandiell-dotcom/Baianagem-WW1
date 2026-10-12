# scripts/apply_uk_rework.py
# Applies the full rework to the United Kingdom focus tree, GFX, ideas and localization.

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

# 65 Ideas bilingual loc
IDEAS_LOC = {
    'ENG_bef_on_the_continent': {
        'pt': ("A BEF no Continente", "A Força Expedicionária Britânica desdobrada em território francês e belga, mantendo firme a linha defensiva dos Aliados."),
        'en': ("The BEF on the Continent", "The British Expeditionary Force deployed in France and Belgium, anchoring Allied defensive lines against hostile offensives.")
    },
    'ENG_fisher_education_act': {
        'pt': ("Lei de Educação Fisher de 1918", "A ampliação da escolaridade técnica e básica qualifica as novas gerações da classe trabalhadora britânica."),
        'en': ("Fisher Education Act of 1918", "Expanded secondary and technical schooling raises literacy and vocational competency across Britain.")
    },
    'ENG_ministry_of_health': {
        'pt': ("Ministério da Saúde", "A unificação dos serviços sanitários nacionais melhora o bem-estar social e o crescimento demográfico metropolitano."),
        'en': ("Ministry of Health", "Consolidated national healthcare and municipal sanitation improve domestic welfare and demographic resilience.")
    },
    'ENG_orderly_demobilisation': {
        'pt': ("Desmobilização Ordenada", "Critérios escalonados de liberação militar evitam o desemprego em massa e restauram o equilíbrio civil."),
        'en': ("Orderly Demobilisation", "Prioritised discharge schedules avert industrial unrest and restore equilibrium to the peacetime economy.")
    },
    'ENG_sterling_stabilization': {
        'pt': ("Estabilização da Libra Esterlina", "Disciplina orçamentária e liquidação de dívidas externas reafirmam o prestígio global da moeda britânica."),
        'en': ("Pound Sterling Stabilization", "Fiscal responsibility and external debt repayment reassert the global prestige of the Pound Sterling.")
    },
    'ENG_whitley_councils': {
        'pt': ("Conselhos Whitley de Relações Industriais", "Fóruns permanentes de negociação paritária entre sindicatos e patronato garantem a harmonia fabril."),
        'en': ("Whitley Industrial Councils", "Permanent consultative councils between employers and trade unions ensure lasting workplace cooperation.")
    },
    'ENG_ww1_aerial_spotting_coordination': {
        'pt': ("Observação Aérea e Balística", "Aeronaves do RFC corrigem disparos de artilharia pesada em tempo real com precisão letal."),
        'en': ("Aerial Spotting and Gunnery Coordination", "RFC spotter aircraft direct heavy artillery salvos in real time with lethal mathematical accuracy.")
    },
    'ENG_ww1_allenby_desert_mobility': {
        'pt': ("Mobilidade no Deserto de Allenby", "Ferrovias avançadas e logística no Sinai garantem manobras fulminantes na Palestina e Síria."),
        'en': ("Allenby's Desert Mobility", "Pipelines and military rails across the Sinai enable rapid, mobile operations through Palestine and Syria.")
    },
    'ENG_ww1_allied_shipping_pool': {
        'pt': ("Pool de Transporte Marítimo Aliado", "Alocação internacional conjunta de navios cargueiros assegura trigo e carvão onde forem vitais."),
        'en': ("Allied Shipping Pool", "Joint allocation of Allied merchant tonnage guarantees uninterrupted coal and wheat shipments.")
    },
    'ENG_ww1_allied_staff_talks': {
        'pt': ("Coordenação com o Estado-Maior Aliado", "Planejamento operacional compartilhado com o comando supremo francês para manobras coordenadas."),
        'en': ("Allied Staff Conversations", "Joint operational planning with the French high command coordinates movements across the Western Front.")
    },
    'ENG_ww1_american_credit_negotiations': {
        'pt': ("Linhas de Crédito em Wall Street", "Créditos comerciais negociados com o mercado americano financiam encomendas bélicas cruciais."),
        'en': ("Wall Street Credit Lines", "Commercial borrowing syndicates in New York fund colossal munitions and grain imports for the war effort.")
    },
    'ENG_ww1_amphibious_pioneers': {
        'pt': ("Pioneirismo em Assalto Anfíbio", "Embarcações blindadas de desembarque e infantaria naval especializada em operações costeiras."),
        'en': ("Amphibious Assault Pioneers", "Specialized landing craft and naval divisions pioneered for combined amphibious operations.")
    },
    'ENG_ww1_armed_neutrality': {
        'pt': ("Neutralidade Armada e Vigilância", "Prontidão das defesas costeiras e mobilização silenciosa da esquadra garantem dissuasão absoluta."),
        'en': ("Armed Neutrality and Vigilance", "Manned coastal fortifications and a mobilized battle fleet provide unwavering strategic deterrence.")
    },
    'ENG_ww1_asc_logistics': {
        'pt': ("Logística do Army Service Corps", "Transporte motorizado e ferrovias de campanha asseguram que suprimentos e munições cheguem ao front."),
        'en': ("Army Service Corps Logistics", "Motorized supply columns and light railways guarantee uninterrupted supply delivery to frontline sectors.")
    },
    'ENG_ww1_asdic_sonar': {
        'pt': ("Detecção Ativa ASDIC (Sonar)", "Pesquisa acústica ativa por quartzo piezoelétrico permite rastrear submarinos submersos."),
        'en': ("ASDIC Active Acoustic Detection", "Active acoustic quartz transducers allow escort vessels to locate submerged submarines with precision.")
    },
    'ENG_ww1_asw_depth_charges': {
        'pt': ("Cargas de Profundidade Anti-Submarinas", "Canistros hidrostáticos lançados por contratorpedeiros esmagam submarinos hostis em imersão."),
        'en': ("Anti-Submarine Depth Charges", "Hydrostatic depth charges launched from destroyers deliver crushing shockwaves to submerged U-boats.")
    },
    'ENG_ww1_backs_to_the_wall': {
        'pt': ("De Costas para a Parede (Ordem de Haig)", "A determinação inabalável das forças imperiais em resistir a qualquer custo até o último homem."),
        'en': ("Backs to the Wall (Haig's Order)", "Unflinching determination across British and Dominion divisions to hold the line at all costs.")
    },
    'ENG_ww1_balkan_liaison': {
        'pt': ("Operações e Apoio nos Bálcãs", "Apoio logístico à Frente de Salonica e coordenação com nações balcânicas aliadas."),
        'en': ("Balkan Allied Liaison", "Logistical support for the Salonika expedition and coordination with Balkan allied armies.")
    },
    'ENG_ww1_central_flying_school': {
        'pt': ("Escola Central de Aviação de Upavon", "Instrução rigorosa em manobras acrobáticas e navegação forma pilotos de caça de primeira linha."),
        'en': ("Central Flying School at Upavon", "Rigorous aerobatic instruction and aerial gunnery cultivate elite frontline fighter pilots.")
    },
    'ENG_ww1_channel_security': {
        'pt': ("Segurança do Canal da Mancha", "Campos minados e a Patrulha de Dover impedem incursões inimigas contra a travessia de tropas."),
        'en': ("English Channel Security", "The Dover Patrol and dense mine barriers safeguard the passage of troop transports to France.")
    },
    'ENG_ww1_channel_transports': {
        'pt': ("Frota de Transporte do Canal", "Vapores mercantes e navios de passageiros requisitados realizam travessias ininterruptas sob escolta."),
        'en': ("Cross-Channel Troop Transports", "Requisitioned steamers and liners maintain a continuous, heavily escorted lifeline to the continent.")
    },
    'ENG_ww1_continental_commitment': {
        'pt': ("Compromisso de Defesa Continental", "O solene compromisso britânico com a liberdade e segurança territorial da Europa Ocidental."),
        'en': ("Continental Defence Commitment", "Britain's solemn pledge that Western European security is paramount to imperial survival.")
    },
    'ENG_ww1_distant_blockade': {
        'pt': ("O Bloqueio Distante", "A Grand Fleet fecha as saídas do Mar do Norte, sufocando as importações das Potências Centrais."),
        'en': ("The Distant Maritime Blockade", "The Grand Fleet seals the exits of the North Sea, starving the Central Powers of vital raw materials.")
    },
    'ENG_ww1_european_security_settlement': {
        'pt': ("Nova Ordem de Segurança Europeia", "A ratificação da Liga das Nações estabelece a cooperação coletiva e a diplomacia pacífica."),
        'en': ("European Security Settlement", "Support for the League of Nations and collective security frameworks underpins a rules-based peace.")
    },
    'ENG_ww1_field_wireless': {
        'pt': ("Rádio de Campanha Marconi", "Comunicações instantâneas por telégrafo sem fio unem regimentos avançados aos quartéis-generais."),
        'en': ("Marconi Field Wireless Transmitters", "Portable spark transmitters link frontline regiments directly with corps artillery and commands.")
    },
    'ENG_ww1_fighter_tactics_rfc': {
        'pt': ("Doutrina de Caça Aérea do RFC", "Formações cerradas e agressividade tática nos céus da França com os lendários Sopwith Camel."),
        'en': ("RFC Fighter Combat Doctrine", "Tight flight formations and aggressive offensive sweeps dominate the airspace over Flanders.")
    },
    'ENG_ww1_french_naval_understanding': {
        'pt': ("Acordo Naval Anglo-Francês", "A Marinha Francesa guarda o Mediterrâneo enquanto a Royal Navy concentra seu poder no Mar do Norte."),
        'en': ("Anglo-French Naval Accord", "The French Navy guards the Mediterranean while the Royal Navy concentrates in home waters.")
    },
    'ENG_ww1_gas_protection_doctrine': {
        'pt': ("Defesa Química e Respiradores Box", "Máscaras contra gases de carvão ativado neutralizam as ameaças de armas químicas no front."),
        'en': ("Gas Protection and Box Respirators", "Standardized Small Box Respirators protect infantry against phosgene and mustard gas attacks.")
    },
    'ENG_ww1_holding_the_line': {
        'pt': ("Defesa de Trincheiras Profundas", "Entrincheiramento cerrado e redes de metralhadoras blindadas resistem a qualquer bombardeio."),
        'en': ("Holding the Trench Line", "Deep trench systems and revetted redoubts hold the line through protracted artillery barrages.")
    },
    'ENG_ww1_hundred_days_offensive': {
        'pt': ("Ofensiva dos Cem Dias (1918)", "Armas combinadas de tanques, artilharia e aviação quebram a Linha Hindenburg de forma definitiva."),
        'en': ("The Hundred Days Offensive", "Masterful combined-arms integration of armor, artillery, and infantry shatters the Hindenburg Line.")
    },
    'ENG_ww1_imperial_airways': {
        'pt': ("Rede Aérea Imperial Airways", "Rotas aéreas de passageiros e mala postal unem a metrópole aos quatro cantos do Império Britânico."),
        'en': ("Imperial Airways Network", "Commercial long-range air routes knit Britain to Cairo, Karachi, and the wider Empire.")
    },
    'ENG_ww1_landships_technical': {
        'pt': ("Engenharia de Blindados (Landships)", "O design pioneiro de tanques romboides com lagartas envolventes para cruzar trincheiras e crateras."),
        'en': ("Landships Technical Engineering", "Pioneering rhomboid heavy tanks engineered to crush barbed wire and cross wide trench spans.")
    },
    'ENG_ww1_machine_gun_corps': {
        'pt': ("Metralhadoras Vickers do MGC", "O Machine Gun Corps concentra metralhadoras médias Vickers em posições de fogo devastador."),
        'en': ("Machine Gun Corps Vickers Batteries", "Specialized Vickers .303 machine gun batteries lay down impenetrable protective curtains of fire.")
    },
    'ENG_ww1_machine_tool_standards': {
        'pt': ("Padrões de Máquinas e Ferramentas", "Tornos de precisão e gabaritos universais aceleram a manufatura intercambiável de armas."),
        'en': ("Machine Tool Standards", "Universal jigs, dies, and precision machine tools accelerate interchangeable defense production.")
    },
    'ENG_ww1_mediterranean_convoy_network': {
        'pt': ("Rede de Comboios do Mediterrâneo", "Escoltas coordenadas a partir de Gibraltar, Malta e Alexandria protegem a rota de Suez."),
        'en': ("Mediterranean Convoy Network", "Escort operations based out of Gibraltar, Malta, and Alexandria secure the Suez sea route.")
    },
    'ENG_ww1_mesopotamian_logistics': {
        'pt': ("Logística Fluvial da Mesopotâmia", "Vapores no Tigre e ferrovias de campanha asseguram a marcha vitoriosa de Maude sobre Bagdá."),
        'en': ("Mesopotamian River Logistics", "Tigris steamers and hospital barges support the advance of British-Indian forces toward Baghdad.")
    },
    'ENG_ww1_naval_disarmament': {
        'pt': ("Ajuste do Desarmamento Naval", "Equilíbrio de tonelagem que poupa recursos fiscais sem abrir mão da supremacia marítima."),
        'en': ("Naval Treaty Equilibrium", "Treaty-limited capital ship tonnages reduce state expenditures while preserving maritime security.")
    },
    'ENG_ww1_naval_gunnery': {
        'pt': ("Sistemas de Direção de Tiro Naval", "Controle centralizado de tiro das torres de comando confere precisão extrema aos disparos."),
        'en': ("Director Firing Gunnery", "Centralized director firing towers deliver synchronized, long-range heavy gun salvos.")
    },
    'ENG_ww1_neutral_shipping_accords': {
        'pt': ("Acordos Comerciais com Neutros", "Garantias marítimas e inspeção de contrabando negociadas pacificamente com nações vizinhas."),
        'en': ("Neutral Shipping Accords", "Pragmatic contraband accords negotiate safe commercial passage while containing enemy supply.")
    },
    'ENG_ww1_npl_standards': {
        'pt': ("Padrões do National Physical Laboratory", "Rigor científico em metrologia e ensaio de materiais eleva a qualidade de toda a indústria."),
        'en': ("National Physical Laboratory Standards", "Scientific metrology and rigorous testing protocols enhance manufacturing efficiency across Britain.")
    },
    'ENG_ww1_operational_reserve': {
        'pt': ("Reservas Operacionais Recompostas", "Divisões veteranas descansadas prontas para explorar brechas táticas ou fechar contra-ataques."),
        'en': ("Operational Reserve Cadres", "Well-equipped reserve shock divisions primed to reinforce critical sectors or exploit breakthroughs.")
    },
    'ENG_ww1_ordnance_metallurgy': {
        'pt': ("Metalurgia de Canhões e Blindagens", "Ligas de aço especiais de Sheffield com excepcional resistência balística e térmica."),
        'en': ("Sheffield Ordnance Metallurgy", "High-tensile alloy steels enhance heavy artillery barrel life and resist armor penetration.")
    },
    'ENG_ww1_otc_officers': {
        'pt': ("Oficiais do Officer Training Corps", "Universidades imperiais formam comandantes de pelotão cultos, resolutos e dedicados."),
        'en': ("Officer Training Corps Cadets", "University and grammar school cadet contingents supply educated junior officers to field battalions.")
    },
    'ENG_ww1_patent_exchanges': {
        'pt': ("Intercâmbio de Patentes Aliadas", "Compartilhamento de inovações químicas e de manufatura com os aliados para modernização civil."),
        'en': ("Allied Patent Exchanges", "Mutual sharing of chemical and precision manufacturing patents accelerates industrial renewal.")
    },
    'ENG_ww1_porton_down_protection': {
        'pt': ("Defesa Química de Porton Down", "Pesquisas de neutralização de substâncias tóxicas garantem imunidade a novos gases bélicos."),
        'en': ("Porton Down Chemical Protection", "Pioneering protective research shields troops from aggressive new chemical agents.")
    },
    'ENG_ww1_postwar_fleet_standards': {
        'pt': ("Modernização da Frota Pós-Guerra", "Aplicação rigorosa das lições da Jutlândia em blindagem horizontal e proteção contra clarão."),
        'en': ("Postwar Fleet Standards", "Jutland design improvements incorporate heavy deck armor and enhanced anti-flash protection.")
    },
    'ENG_ww1_postwar_raf_establishment': {
        'pt': ("A RAF Permanente de Trenchard", "A doutrina de policiamento aéreo imperial mantém a RAF como força de vanguarda no tempo de paz."),
        'en': ("Trenchard's Permanent RAF Cadre", "Imperial air-control doctrines preserve an independent, cost-effective air arm across the globe.")
    },
    'ENG_ww1_postwar_research_council': {
        'pt': ("Conselho de Pesquisa Científica (DSIR)", "Financiamento estatal continuado para universidades e laboratórios de física aplicada."),
        'en': ("Postwar Research Council (DSIR)", "Direct government patronage of applied physics and industrial research fuels technological advance.")
    },
    'ENG_ww1_production_standards': {
        'pt': ("Controle de Qualidade de Produção", "Tolerâncias industriais uniformes reduzem descartes fabris e elevam a velocidade das oficinas."),
        'en': ("Production Quality Norms", "Strict engineering tolerances minimize factory scrap and enhance assembly line throughput.")
    },
    'ENG_ww1_professional_force': {
        'pt': ("Exército Profissional e Cadastrado", "Um quadro regular pequeno, voluntário e altamente mecanizado para missões imperiais."),
        'en': ("Small Professional Standing Army", "A compact, highly motorized volunteer force designed for rapid deployment and imperial policing.")
    },
    'ENG_ww1_ramc_medical': {
        'pt': ("Medicina de Campanha do RAMC", "Evacuação rápida e postos avançados de cirurgia salvam a vida de centenas de milhares de combatentes."),
        'en': ("RAMC Battlefield Medicine", "Rapid motor ambulance evacuation and forward antiseptic surgery save countless frontline lives.")
    },
    'ENG_ww1_reconstruction_credit': {
        'pt': ("Crédito para Reconstrução", "Linhas de crédito comercial estabilizam os preços e apoiam a reestruturação da indústria."),
        'en': ("Reconstruction Credit Facilities", "Targeted commercial credit sustains employment and retools heavy industries for civilian markets.")
    },
    'ENG_ww1_rnas_naval_aviation': {
        'pt': ("Aviação Naval do RNAS", "Hidroaviões de patrulha e primeiros navios aeródromos dedicados à caça submarina e ataque naval."),
        'en': ("RNAS Naval Aviation", "Patrol seaplanes and early flat-top carriers pioneer airborne reconnaissance and torpedo strikes.")
    },
    'ENG_ww1_russian_procurement_liaison': {
        'pt': ("Suprimento ao Império Russo", "Comboios de fuzis e pólvora por Arkhangelsk e Murmansk sustentam o front oriental."),
        'en': ("Russian Procurement Liaison", "British loans and armaments convoys through Murmansk bolster the Russian Imperial Army.")
    },
    'ENG_ww1_signals_direction_finding': {
        'pt': ("Radiogoniometria Costeira (HF/DF)", "Triangulação de transmissões de rádio inimigas localiza U-boats no mar em instantes."),
        'en': ("Coastal Direction Finding (HF/DF)", "Triangulation of enemy wireless signals instantly pinpoints the positions of hunting U-boats.")
    },
    'ENG_ww1_signals_intelligence': {
        'pt': ("Inteligência Criptográfica de Sinais", "Interceptação de mensagens de rádio decifra as intenções diplomáticas e navais inimigas."),
        'en': ("Signals Intelligence and Interception", "Wireless interception posts supply naval analysts with early warning of enemy operations.")
    },
    'ENG_ww1_smuts_report': {
        'pt': ("O Relatório Smuts sobre o Poder Aéreo", "Recomendação histórica para fundir a aviação naval e militar em uma força autônoma soberana."),
        'en': ("The Smuts Report on Air Power", "The historic recommendation advocating a unified, independent ministry and doctrine for the air.")
    },
    'ENG_ww1_sound_ranging_math': {
        'pt': ("Sondagem Sonora e Flash Spotting", "Cálculos de precisão com microfones subterrâneos localizam baterias inimigas pelo estrondo."),
        'en': ("Sound Ranging and Flash Spotting", "Subterranean microphone arrays locate opposing artillery batteries by the shockwave of firing.")
    },
    'ENG_ww1_submarine_service': {
        'pt': ("Flotilhas de Submarinos da Marinha Real", "Submarinos das classes E e J penetram o Heligoland Bight e atacam rotas inimigas no Báltico."),
        'en': ("Royal Navy Submarine Flotillas", "Ocean-going E-class submarines penetrate the Baltic and Heligoland Bight, menacing enemy shipping.")
    },
    'ENG_ww1_supreme_war_council': {
        'pt': ("Conselho Supremo de Guerra de Versalhes", "Comando unificado dos exércitos aliados sob o General Foch para ofensivas sincronizadas."),
        'en': ("Supreme War Council at Versailles", "Unified Allied strategic leadership synchronizes French, British, and American offensives in 1918.")
    },
    'ENG_ww1_tank_assault_doctrine': {
        'pt': ("Doutrina de Assalto com Tanques (Cambrai)", "Avanço maciço de blindados sem bombardeio prévio para romper trincheiras e arames."),
        'en': ("Tank Assault Doctrine (Cambrai)", "Massed armor surprise attacks without preliminary shelling rupture hostile trench networks.")
    },
    'ENG_ww1_technical_education': {
        'pt': ("Educação Técnica de Engenharia", "Institutos politécnicos formam engenheiros civis, químicos e mecânicos para reconstruir o país."),
        'en': ("Technical Education for Reconstruction", "Polytechnics qualify thousands of mechanical and chemical engineers to drive peacetime recovery.")
    },
    'ENG_ww1_territorial_renewal': {
        'pt': ("Renovação do Exército Territorial", "A Força Territorial reorganizada como uma reserva armada robusta e econômica para a metrópole."),
        'en': ("Territorial Force Renewal", "Reconstituted citizen-soldier battalions form an inexpensive yet solid shield for home defense.")
    },
    'ENG_ww1_trench_mortar_doctrine': {
        'pt': ("Morteiros de Trincheira Stokes de 3 Pol.", "Apoio de fogo curvo imediato da infantaria para pulverizar ninhos de metralhadoras em abrigos."),
        'en': ("Stokes 3-Inch Trench Mortars", "High-angle portable mortars provide frontline platoons with immediate destructive firepower.")
    },
    'ENG_ww1_university_research': {
        'pt': ("Pesquisa Universitária Cavendish", "Grandes centros acadêmicos desenvolvem inovações pioneiras em eletrônica e física aplicada."),
        'en': ("Cavendish University Research", "Elite academic faculties solve complex technological problems in electronics and applied physics.")
    }
}

# 1. Update common/national_focus/uk.txt
print("Reading common/national_focus/uk.txt...")
with open('common/national_focus/uk.txt', 'r', encoding='utf-8') as f:
    uk_text = f.read()

# We need to replace completion_reward for each focus cleanly
# Let's find each focus block
focus_pattern = re.compile(r'(\bfocus\s*=\s*\{(?:\s*id\s*=\s*(\w+)[^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\})', re.DOTALL)

def update_focus_block(match):
    full_block = match.group(1)
    fid = match.group(2)
    
    if fid not in ALL_FOCUS_DATA:
        return full_block + "}"
    
    data = ALL_FOCUS_DATA[fid]
    new_reward_body = data['reward']
    
    # Check if there were original country_event or set_country_flag calls to preserve
    orig_events = re.findall(r'country_event\s*=\s*\{[^}]+\}', full_block)
    orig_flags = re.findall(r'set_country_flag\s*=\s*(\w+)', full_block)
    
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
        
    # Indent reward nicely
    reward_lines = [f"   {line.strip()}" for line in combined_reward.strip().split('\n') if line.strip()]
    formatted_reward = "  completion_reward = {\n" + "\n".join(reward_lines) + "\n  }"
    
    # Replace completion_reward in full_block
    new_block = re.sub(r'completion_reward\s*=\s*\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', formatted_reward, full_block)
    return new_block + "}"

# To avoid regex depth issues with huge file, let's parse blocks with brace tracking
def parse_and_replace_uk_focuses(content):
    pos = 0
    result = []
    replaced_count = 0
    
    while pos < len(content):
        # find 'focus = {'
        f_idx = content.find('focus = {', pos)
        if f_idx == -1:
            result.append(content[pos:])
            break
            
        result.append(content[pos:f_idx])
        
        # Track braces to find the end of this focus block
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
        # find id
        id_match = re.search(r'\bid\s*=\s*(\w+)', focus_chunk)
        if id_match:
            fid = id_match.group(1)
            if fid in ALL_FOCUS_DATA:
                data = ALL_FOCUS_DATA[fid]
                new_reward_body = data['reward']
                
                # Extract original events and flags
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
                
                # Replace completion_reward inside focus_chunk
                cr_start = focus_chunk.find('completion_reward = {')
                if cr_start != -1:
                    # Find end of completion_reward
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

# 2. Generate interface/ww1_britain_goals.gfx
print("Generating interface/ww1_britain_goals.gfx for all 200 focuses...")
gfx_lines = [
    '# Generated Sprite Definitions for British Empire (WW1) Focuses (200 goals + 200 shines)',
    'spriteTypes = {'
]

for fid in ALL_FOCUS_DATA.keys():
    tex_path = f"gfx/interface/goals/ww1_britain/{fid}.png"
    gfx_lines.append(f'\tspriteType = {{ name = "GFX_goal_ww1_{fid}" texturefile = "{tex_path}" }}')
    gfx_lines.append('\tspriteType = {')
    gfx_lines.append(f'\t\tname = "GFX_goal_ww1_{fid}_shine"')
    gfx_lines.append(f'\t\ttexturefile = "{tex_path}"')
    gfx_lines.append('\t\teffectFile = "gfx/FX/buttonstate.lua"')
    gfx_lines.append('\t\tanimation = {')
    gfx_lines.append(f'\t\t\tanimationmaskfile = "{tex_path}"')
    gfx_lines.append('\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"')
    gfx_lines.append('\t\t\tanimationrotation = -90.0')
    gfx_lines.append('\t\t\tanimationlooping = no')
    gfx_lines.append('\t\t\tanimationtime = 0.75')
    gfx_lines.append('\t\t\tanimationdelay = 0')
    gfx_lines.append('\t\t\tanimationblendmode = "add"')
    gfx_lines.append('\t\t\tanimationtype = "scrolling"')
    gfx_lines.append('\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }')
    gfx_lines.append('\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }')
    gfx_lines.append('\t\t}')
    gfx_lines.append('\t\tlegacy_lazy_load = no')
    gfx_lines.append('\t}')

gfx_lines.append('}')
gfx_lines.append('')

with open('interface/ww1_britain_goals.gfx', 'w', encoding='utf-8') as f:
    f.write("\n".join(gfx_lines))
print(f"Wrote interface/ww1_britain_goals.gfx with {len(ALL_FOCUS_DATA)*2} sprite definitions!")

# 3. Generate localisation/braz_por/ww1_britain_l_braz_por.yml
print("Generating Brazilian Portuguese localization...")
with open('localisation/braz_por/ww1_britain_l_braz_por.yml', 'r', encoding='utf-8-sig', errors='ignore') as f:
    orig_pt_lines = f.readlines()

header_pt = [line.rstrip('\r\n') for line in orig_pt_lines[:54]]

pt_out = ['\ufeffl_braz_por:']
for line in header_pt[1:]:
    pt_out.append(line)

pt_out.append('\n # --- Ideias e Modificadores do Rework Britanico ---')
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
print(f"Wrote localisation/braz_por/ww1_britain_l_braz_por.yml ({len(pt_out)} lines) with UTF-8 BOM!")

# 4. Generate localisation/english/ww1_britain_l_english.yml
print("Generating English localization...")
with open('localisation/english/ww1_britain_l_english.yml', 'r', encoding='utf-8-sig', errors='ignore') as f:
    orig_en_lines = f.readlines()

header_en = [line.rstrip('\r\n') for line in orig_en_lines[:54]]

en_out = ['\ufeffl_english:']
for line in header_en[1:]:
    en_out.append(line)

en_out.append('\n # --- British Rework Ideas & Modifiers ---')
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
print(f"Wrote localisation/english/ww1_britain_l_english.yml ({len(en_out)} lines) with UTF-8 BOM!")

print("\n=== UK REWORK APPLIED COMPREHENSIVELY! ===")

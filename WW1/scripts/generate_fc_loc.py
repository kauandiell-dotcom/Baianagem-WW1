import os

en_content = """\ufeffl_english:
 bww1_front_counter_category: "Strategic Map Tools"
 bww1_front_counter_category_desc: "Strategic cartographic tools for real-time frontline force assessment across active theaters of the Great War."
 bww1_fc_enable_counter: "Enable Frontline Troop Counters"
 bww1_fc_enable_counter_desc: "Projects dynamic army troop counters directly along contested land borders, displaying friendly coalition forces and estimated enemy strength."
 bww1_fc_disable_counter: "Disable Frontline Troop Counters"
 bww1_fc_disable_counter_desc: "Hides all frontline troop counters and deactivates sector strength calculations."
 bww1_fc_refresh_counter: "Recalculate Frontline Strength"
 bww1_fc_refresh_counter_desc: "Forces an immediate strategic recalculation of troops across all active frontline sectors."
 bww1_fc_friendly_val: "§G[?bww1_friendly_manpower|0]§!"
 bww1_fc_divider_val: "§Y|§!"
 bww1_fc_enemy_val: "§R~[?bww1_enemy_manpower|0]§!"
 bww1_intel_high: "§GHigh (Detailed Reconnaissance)§!"
 bww1_intel_medium: "§YMedium (Trench Observation)§!"
 bww1_intel_low: "§RLow (Heavy Fog of War)§!"
"""

pt_content = """\ufeffl_braz_por:
 bww1_front_counter_category: "Ferramentas Estratégicas de Mapa"
 bww1_front_counter_category_desc: "Ferramentas cartográficas estratégicas para avaliação de forças em tempo real ao longo dos teatros de operações da Grande Guerra."
 bww1_fc_enable_counter: "Ativar Contadores de Frente"
 bww1_fc_enable_counter_desc: "Projeta contadores dinâmicos de tropas diretamente sobre as linhas de frente terrestres ativas, calculando o efetivo amigo e a estimativa inimiga."
 bww1_fc_disable_counter: "Desativar Contadores de Frente"
 bww1_fc_disable_counter_desc: "Oculta todos os contadores de tropas do mapa e desativa os cálculos de efetivo nos setores."
 bww1_fc_refresh_counter: "Recalcular Forças da Linha de Frente"
 bww1_fc_refresh_counter_desc: "Força uma atualização estratégica imediata dos contingentes de tropas em todos os setores de combate."
 bww1_fc_friendly_val: "§G[?bww1_friendly_manpower|0]§!"
 bww1_fc_divider_val: "§Y|§!"
 bww1_fc_enemy_val: "§R~[?bww1_enemy_manpower|0]§!"
 bww1_intel_high: "§GAlta (Reconhecimento Aéreo)§!"
 bww1_intel_medium: "§YMédia (Observação de Trincheira)§!"
 bww1_intel_low: "§RBaixa (Forte Nevoeiro de Guerra)§!"
"""

en_path = r'C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\localisation\english\bww1_front_counter_l_english.yml'
pt_path = r'C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\localisation\braz_por\bww1_front_counter_l_braz_por.yml'

os.makedirs(os.path.dirname(en_path), exist_ok=True)
os.makedirs(os.path.dirname(pt_path), exist_ok=True)

with open(en_path, 'w', encoding='utf-8-sig') as f:
    f.write(en_content.lstrip('\ufeff'))

with open(pt_path, 'w', encoding='utf-8-sig') as f:
    f.write(pt_content.lstrip('\ufeff'))

print('English loc written successfully:', os.path.exists(en_path))
print('Portuguese loc written successfully:', os.path.exists(pt_path))

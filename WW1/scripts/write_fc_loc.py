import os

en_content = """l_english:
 bww1_front_counter_category: "Frontline Strategic Intelligence"
 bww1_front_counter_category_desc: "Real-time frontline force assessments and on-map force deployment across active borders."
 bww1_fc_enable_counter: "Enable Frontline Troop Counter"
 bww1_fc_enable_counter_desc: "Displays the real-time frontline force assessment HUD and on-map sector badges along contested borders."
 bww1_fc_disable_counter: "Disable Frontline Troop Counter"
 bww1_fc_disable_counter_desc: "Hides the frontline force assessment HUD and deactivates sector strength calculations."
 bww1_fc_refresh_counter: "Recalculate Frontline Strength"
 bww1_fc_refresh_counter_desc: "Forces an immediate recount of all divisions and fielded manpower stationed along the active frontline."
 bww1_fc_header_text: "§Y[ROOT.GetName]§! §Wvs§! §Y[?ROOT.bww1_front_enemy_tag.GetName]§! §7— Active Frontline§!"
 bww1_fc_friendly_name_text: "§G[ROOT.GetName]§!"
 bww1_fc_friendly_val: "§W[?ROOT.bww1_front_friendly_manpower|0]§!"
 bww1_fc_friendly_divs_val: "§G[?ROOT.bww1_front_friendly_divs|0] Divisions§!"
 bww1_fc_divider_val: "§RVS§!"
 bww1_fc_enemy_name_text: "§R[?ROOT.bww1_front_enemy_tag.GetName]§!"
 bww1_fc_enemy_val: "§W[?ROOT.bww1_front_enemy_manpower|0]§!"
 bww1_fc_enemy_divs_val: "§R[?ROOT.bww1_front_enemy_divs|0] Divisions§!"
 bww1_fc_friendly_badge_name: "§G[FROM.GetName] Friendly Sector§!"
 bww1_fc_friendly_badge_desc: "Friendly border sector: §Y[FROM.GetName]§!\\nDeployed Force: §W[?FROM.bww1_state_friendly_manpower|0]§! soldiers ([?FROM.bww1_state_friendly_divs|0] divisions)"
 bww1_fc_friendly_badge_cost: "§W[?FROM.bww1_state_friendly_manpower|0]§!"
 bww1_fc_enemy_badge_name: "§R[FROM.GetName] Opposing Sector§!"
 bww1_fc_enemy_badge_desc: "Opposing border sector: §Y[FROM.GetName]§!\\nOpposing Force: §W[?FROM.bww1_state_enemy_manpower|0]§! soldiers ([?FROM.bww1_state_enemy_divs|0] divisions)"
 bww1_fc_enemy_badge_cost: "§W[?FROM.bww1_state_enemy_manpower|0]§!"
 bww1_intel_high: "§GHigh (Detailed Reconnaissance)§!"
 bww1_intel_medium: "§YMedium (Trench Observation)§!"
 bww1_intel_low: "§RLow (Heavy Fog of War)§!"
"""

pt_content = """l_braz_por:
 bww1_front_counter_category: "Inteligência Estratégica de Fronte"
 bww1_front_counter_category_desc: "Avaliação em tempo real de efetivo de combate e marcadores de desdobramento de tropas ao longo do fronte."
 bww1_fc_enable_counter: "Ativar Contador de Tropas no Fronte"
 bww1_fc_enable_counter_desc: "Exibe o painel de inteligência de fronte e os marcadores de setor no mapa ao longo das fronteiras contestadas."
 bww1_fc_disable_counter: "Desativar Contador de Tropas no Fronte"
 bww1_fc_disable_counter_desc: "Oculta o painel de inteligência e desativa o cálculo de efetivo de fronte."
 bww1_fc_refresh_counter: "Recalcular Força do Fronte"
 bww1_fc_refresh_counter_desc: "Força a recontagem imediata de todas as divisões e homens desdobrados ao longo do fronte ativo."
 bww1_fc_header_text: "§Y[ROOT.GetName]§! §Wvs§! §Y[?ROOT.bww1_front_enemy_tag.GetName]§! §7— Fronte Ativo§!"
 bww1_fc_friendly_name_text: "§G[ROOT.GetName]§!"
 bww1_fc_friendly_val: "§W[?ROOT.bww1_front_friendly_manpower|0]§!"
 bww1_fc_friendly_divs_val: "§G[?ROOT.bww1_front_friendly_divs|0] Divisões§!"
 bww1_fc_divider_val: "§RVS§!"
 bww1_fc_enemy_name_text: "§R[?ROOT.bww1_front_enemy_tag.GetName]§!"
 bww1_fc_enemy_val: "§W[?ROOT.bww1_front_enemy_manpower|0]§!"
 bww1_fc_enemy_divs_val: "§R[?ROOT.bww1_front_enemy_divs|0] Divisões§!"
 bww1_fc_friendly_badge_name: "§GSetor Amigo: [FROM.GetName]§!"
 bww1_fc_friendly_badge_desc: "Setor de fronteira amigo: §Y[FROM.GetName]§!\\nForça Desdobrada: §W[?FROM.bww1_state_friendly_manpower|0]§! soldados ([?FROM.bww1_state_friendly_divs|0] divisões)"
 bww1_fc_friendly_badge_cost: "§W[?FROM.bww1_state_friendly_manpower|0]§!"
 bww1_fc_enemy_badge_name: "§RSetor Opositor: [FROM.GetName]§!"
 bww1_fc_enemy_badge_desc: "Setor de fronteira opositor: §Y[FROM.GetName]§!\\nForça Opositora: §W[?FROM.bww1_state_enemy_manpower|0]§! soldados ([?FROM.bww1_state_enemy_divs|0] divisões)"
 bww1_fc_enemy_badge_cost: "§W[?FROM.bww1_state_enemy_manpower|0]§!"
 bww1_intel_high: "§GAlto (Reconhecimento Detalhado)§!"
 bww1_intel_medium: "§YMédio (Observação de Trincheira)§!"
 bww1_intel_low: "§RBaixo (Nevoeiro de Guerra Intenso)§!"
"""

en_path = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\localisation\english\bww1_front_counter_l_english.yml"
pt_path = r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\localisation\braz_por\bww1_front_counter_l_braz_por.yml"

with open(en_path, "wb") as f:
    f.write(b"\xef\xbb\xbf")
    f.write(en_content.encode("utf-8"))

with open(pt_path, "wb") as f:
    f.write(b"\xef\xbb\xbf")
    f.write(pt_content.encode("utf-8"))

print("Bilingual localization files successfully written with UTF-8 BOM.")

# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# 1. Generate full Brazilian Portuguese BM_units_l_braz_por.yml
bm_pt_content = """l_braz_por:
 bm_desert_infantry:0 "Infantaria do Deserto"
 bm_desert_infantry_desc:0 "A infantaria do deserto é especialmente treinada para suportar as duras condições áridas, com fardamentos leves e camuflagem apropriada para tolerância ao calor extremo. Contudo, essa adaptação reduz seu rendimento em ambientes frios."

 bm_winter_infantry:0 "Infantaria de Inverno"
 bm_winter_infantry_desc:0 "A infantaria de inverno sobressai em climas gelados onde outros sucumbem, utilizando equipamentos camuflados brancos para emboscadas e defesa na neve. Seus fardamentos térmicos, porém, são inadequados para o calor."

 bm_shock_troops:0 "Tropas de Choque"
 bm_shock_troops_desc:0 "Tropas de elite selecionadas entre os soldados mais vigorosos e audazes, armadas com submetralhadoras e granadas para romper trincheiras e posições fortificadas sob fogo intenso."

 bm_mechanized_shocktroops:0 "Tropas de Choque Mecanizadas"
 bm_mechanized_shocktroops_desc:0 "Tropas de choque embarcadas em blindados protegidos, combinando a ferocidade do assalto aproximado com velocidade e proteção sobre lagartas."

 bm_motorized_shocktroops:0 "Tropas de Choque Motorizadas"
 bm_motorized_shocktroops_desc:0 "Tropas de choque transportadas por caminhões rápidos para exploração imediata de brechas nas defesas inimigas."

 bm_jungle_infantry:0 "Infantaria de Selva"
 bm_jungle_infantry_desc:0 "Mestres do combate sob densa copa arbórea e pântanos tropicais, operando emboscadas letais onde forças regulares perdem coesão e orientação."

 bm_mechanized_artillery:0 "Artilharia Mecanizada"
 bm_mechanized_artillery_desc:0 "Combina poder de fogo avassalador com mobilidade blindada, reposicionando-se velozmente para prestar suporte imediato a operações ofensivas."

 bm_mechanized_anti_tank:0 "Antitanque Mecanizado"
 bm_mechanized_anti_tank_desc:0 "Veículos blindados projetados para caçar tanques inimigos com canhões de alta velocidade e agilidade de manobra no campo de batalha."

 bm_mechanized_anti_air:0 "Antiaéreo Mecanizado"
 bm_mechanized_anti_air_desc:0 "Sistemas antiaéreos montados em chassis blindados para proteger colunas de avanço contra ataques da aviação inimiga."

 bm_motorcycle_units:0 "Infantaria em Motocicleta"
 bm_motorcycle_units_desc:0 "Tropas leves e velozes sobre motocicletas, ideais para patrulhas avançadas, flanqueamento dinâmico e exploração de lacunas nas linhas inimigas."

 bm_light_infantry:0 "Infantaria Leve"
 bm_light_infantry_desc:0 "Combatentes ágeis com carga reduzida, especializados em deslocamentos difíceis, patrulhas de vanguarda e manobras flexíveis de flanco."

 bm_armored_aa_car:0 "Carro Blindado Antiaéreo"
 bm_armored_aa_car_desc:0 "Autometralhadora ou canhão leve antiaéreo sobre chassi sobre rodas, provendo proteção aérea móvel às colunas."

 bm_armored_at_car:0 "Carro Blindado Antitanque"
 bm_armored_at_car_desc:0 "Carro sobre rodas munido de canhão antitanque para flanquear e emboscar blindados inimigos com extrema agilidade."

 bm_armored_ac_car:0 "Carro Blindado com Canhão Automático"
 bm_armored_ac_car_desc:0 "Veículo blindado rápido dotado de canhão automático leve para varrer infantaria e viaturas de transporte adversárias."

 bm_coastal_garrison:0 "Guarnição Costeira"
 bm_coastal_garrison_desc:0 "Tropas fortificadas em praias e ancoradouros estratégicos para repelir desembarques anfíbios e assaltos navais inimigos."

 bm_garrison:0 "Guarnição"
 bm_garrison_desc:0 "Forças de segurança territorial encarregadas de defender pontos vitais, guarnecer linhas secundárias e sufocar revoltas populares."

 bm_police:0 "Polícia Militar e Civil"
 bm_police_desc:0 "Destacamentos de ordem interna e contenção de distúrbios, peritos em manter toques de recolher e reprimir a resistência em zonas ocupadas."

 gen_helicopter:0 "Batalhão de Helicópteros"
 gen_helicopter_desc:0 "Unidade aérea tática de asas rotativas com incomparável flexibilidade de inserção e transporte direto sobre o teatro de operações."

 bm_command_regiment:0 "Companhia de Comando"
 bm_command_regiment_desc:0 "Núcleo de estado-maior tático coordenando transmissões, apoio aéreo e artilharia diretamente com o escalão divisionário."

 bm_mot_command_regiment:0 "Companhia de Comando Motorizada"
 bm_mot_command_regiment_desc:0 "Posto de comando móvel em caminhões equipados com rádios e mapas para manobras de rápida tomada de decisão."

 bm_light_tank_command_regiment:0 "Companhia de Tanques de Comando Leves"
 bm_light_tank_command_regiment_desc:0 "Tanques de comando com antenas especiais para coordenar brigadas blindadas diretamente no coração do combate."

 bm_medium_tank_command_regiment:0 "Companhia de Tanques de Comando Médios"
 bm_medium_tank_command_regiment_desc:0 "Veículos blindados médios de comando combinando blindagem protetora e rádio de longo alcance para liderança blindada."

 bm_heavy_tank_command_regiment:0 "Companhia de Tanques de Comando Pesados"
 bm_heavy_tank_command_regiment_desc:0 "Posto de comando blindado pesado para dirigir operações de ruptura sob as mais terríveis barragens de artilharia."

 bm_modern_tank_command_regiment:0 "Companhia de Tanques de Comando Modernos"
 bm_modern_tank_command_regiment_desc:0 "Posto avançado de liderança sobre chassis de última geração para coordenação blindada em alta velocidade."

 bm_sniper_company:0 "Companhia de Atiradores de Elite (Snipers)"
 bm_sniper_company_desc:0 "Atiradores munidos de fuzis de precisão e miras ópticas para neutralizar oficiais inimigos, metralhadoras e observadores."

 bm_mortar_company:0 "Companhia de Morteiros"
 bm_mortar_company_desc:0 "Morteiros de infantaria de trajetória parabólica para castigar posições abrigadas e trincheiras fora da linha de visada direta."

 bm_pack_howitzer:0 "Obuseiro Desmontável de Montanha"
 bm_pack_howitzer_desc:0 "Peças leves de artilharia capazes de serem desmontadas e transportadas por mulas através de desfiladeiros e montanhas íngremes."

 bm_chemical_artillery:0 "Artilharia Química"
 bm_chemical_artillery_desc:0 "Projéteis de gás asfixiante e vesicante para desorganizar e sufocar entrincheiramentos inimigos antes do ataque de infantaria."

 bm_machine_gunner:0 "Companhia de Metralhadoras Pesadas"
 bm_machine_gunner_desc:0 "Ninhos de metralhadoras fixas de tiro sustentado que criam cortinas letais de fogo cruzado e aniquilam assaltos frontais."

 bm_flamethower_support:0 "Companhia de Lança-Chamas"
 bm_flamethower_support_desc:0 "Destacamentos de assalto armados com lança-chamas portáteis para limpar casamatas, túneis e abrigos fortificados."

 bm_armored_car_flame:0 "Carro Blindado Lança-Chamas"
 bm_armored_car_flame_desc:0 "Viatura blindada equipada com bocal de fogo para incinerar bolsões de resistência urbana e barricadas com proteção de couraça."

 bm_mechanized_flamethrower:0 "Lança-Chamas Mecanizado"
 bm_mechanized_flamethrower_desc:0 "Chassi blindado sobre lagartas dotado de potente projetor de chamas para liderar a quebra de linhas defensivas."

 bm_motorcycle_recon:0 "Reconhecimento em Motocicletas"
 bm_motorcycle_recon_desc:0 "Patrulhas velozes em motocicletas para mapear disposições inimigas e relatar itinerários seguros com rapidez."

 bm_at_rifle_company:0 "Companhia de Fuzis Antitanque"
 bm_at_rifle_company_desc:0 "Pelotões de infantaria armados com fuzis pesados capazes de perfurar a couraça de carros blindados e tanques primitivos."

 support_light_td:0 "Caça-Tanques Leve de Suporte"
 support_medium_td:0 "Caça-Tanques Médio de Suporte"
 support_heavy_td:0 "Caça-Tanques Pesado de Suporte"
 support_modern_td:0 "Caça-Tanques Moderno de Suporte"
 support_super_heavy_td:0 "Caça-Tanques Superpesado de Suporte"
 MST_super_heavy_tank_destroyer_brigade:0 "Batalhão Caça-Tanques Superpesado"

 support_light_tank_art:0 "Artilharia Autopropulsada Leve de Suporte"
 support_medium_tank_art:0 "Artilharia Autopropulsada Média de Suporte"
 support_heavy_tank_art:0 "Artilharia Autopropulsada Pesada de Suporte"
 support_modern_tank_art:0 "Artilharia Autopropulsada Moderna de Suporte"
 support_super_heavy_tank_art:0 "Artilharia Autopropulsada Superpesada de Suporte"
 MST_super_heavy_sp_artillery_brigade:0 "Batalhão de Artilharia Autopropulsada Superpesada"

 support_light_tank_aa:0 "Antiaéreo Autopropulsado Leve de Suporte"
 support_medium_tank_aa:0 "Antiaéreo Autopropulsado Médio de Suporte"
 support_heavy_tank_aa:0 "Antiaéreo Autopropulsado Pesado de Suporte"
 support_modern_tank_aa:0 "Antiaéreo Autopropulsado Moderno de Suporte"
 support_super_heavy_tank_aa:0 "Antiaéreo Autopropulsado Superpesado de Suporte"
 MST_super_heavy_sp_anti_air_brigade:0 "Batalhão Antiaéreo Autopropulsado Superpesado"

 support_light_tank:0 "Companhia de Tanques Leves de Suporte"
 support_medium_tank:0 "Companhia de Tanques Médios de Suporte"
 support_heavy_tank:0 "Companhia de Tanques Pesados de Suporte"
 support_modern_tank:0 "Companhia de Tanques Modernos de Suporte"
 support_super_heavy_tank:0 "Companhia de Tanques Superpesados de Suporte"
 super_heavy_armor_brigade:0 "Batalhão de Tanques Superpesados"

 support_amphibious_tank:0 "Companhia de Tanques Anfíbios de Suporte"
 support_amphibious_light_tank:0 "Tanques Anfíbios Leves de Suporte"
 support_amphibious_medium_tank:0 "Tanques Anfíbios Médios de Suporte"
 support_amphibious_heavy_tank:0 "Tanques Anfíbios Pesados de Suporte"

 support_mechanized:0 "Mecanizado de Suporte"
 mech_recon:0 "Reconhecimento Mecanizado"
 support_amtrack:0 "Companhia de Trator Anfíbio (Amtrack)"
 support_armoured_car:0 "Companhia de Carros Blindados de Suporte"
 support_motorized_rocket:0 "Foguetes Motorizados de Suporte"
"""

p_bm_pt = ROOT / "localisation" / "braz_por" / "BM_units_l_braz_por.yml"
p_bm_pt.write_bytes(b"\xef\xbb\xbf" + bm_pt_content.strip().encode("utf-8") + b"\n")
print(f"Written {p_bm_pt} with UTF-8 BOM.")

# 2. Generate ww1_units_l_braz_por.yml covering all ground, support, and naval units
ww1_units_pt_content = """l_braz_por:
 # Tropas de Linha
 infantry:0 "Infantaria"
 infantry_desc:0 "A espinha dorsal das forças terrestres, equipada com fuzis, baionetas e capacetes de aço para segurar e assaltar posições defensivas."
 infantry_short:0 "Inf"

 cavalry:0 "Cavalaria"
 cavalry_desc:0 "Regimentos montados rápidos para patrulha, flanqueamento móvel e perseguição de forças rompidas."
 cavalry_short:0 "Cav"

 motorized:0 "Infantaria Motorizada"
 motorized_desc:0 "Infantaria transportada em caminhões para rápida concentração e avanço ao lado das unidades móveis."
 motorized_short:0 "Mot"

 mechanized:0 "Infantaria Mecanizada"
 mechanized_desc:0 "Tropas protegidas em veículos de transporte sobre lagartas, capazes de acompanhar blindados em combate intenso."
 mechanized_short:0 "Mec"

 mountaineers:0 "Tropas de Montanha"
 mountaineers_desc:0 "Tropas treinadas em escalada, sobrevivência em altas altitudes e combate em desfiladeiros escarpados."
 mountaineers_short:0 "Mont"

 marine:0 "Fuzileiros Navais"
 marine_desc:0 "Combatentes anfíbios de assalto especializados na tomada de cabeças de ponte e praias fortificadas."
 marine_short:0 "Fuz Nav"

 marine_commando:0 "Comandos Anfíbios"
 marine_commando_desc:0 "Unidades de elite treinadas para incursões rápidas de sabotagem e captura de posições costeiras vitais."
 marine_commando_short:0 "Comando"

 paratrooper:0 "Paraquedistas"
 paratrooper_desc:0 "Tropas de elite aerotransportadas projetadas para saltos em profundidade atrás das linhas adversárias."
 paratrooper_short:0 "Para"

 bicycle_battalion:0 "Batalhão de Ciclistas"
 bicycle_battalion_desc:0 "Infantaria ágil que emprega bicicletas para marchas rodoviárias rápidas com baixo consumo de combustível."
 bicycle_battalion_short:0 "Cicl"

 ranger_battalion:0 "Batalhão de Rangers"
 ranger_battalion_desc:0 "Batedores de reconhecimento e patrulha em profundidade com grande autonomia operacional."
 ranger_battalion_short:0 "Ranger"

 penal_battalion:0 "Batalhão Penal"
 penal_battalion_desc:0 "Unidades disciplinares destacadas para missões de altíssimo risco e desminagem sob fogo inimigo."
 penal_battalion_short:0 "Penal"

 irregular_infantry:0 "Infantaria Irregular"
 irregular_infantry_desc:0 "Forças voluntárias regionais, guerrilhas e levas civis armadas com fuzis diversos para defesa local."
 irregular_infantry_short:0 "Irreg"

 militia:0 "Milícia"
 militia_desc:0 "Forças territoriais de reserva com treinamento básico para guarnição estática e segurança interna."
 militia_short:0 "Mil"

 fake_intel_unit:0 "Divisão de Engodo (Falsa)"
 fake_intel_unit_desc:0 "Concentração de barracas, blindados de madeira e falsas transmissões de rádio para enganar o serviço de espionagem adversário."
 fake_intel_unit_short:0 "Engodo"

 # Blindados
 light_armor:0 "Tanques Leves"
 light_armor_desc:0 "Blindados rápidos e ágeis com armamento leve, excelentes para reconhecimento armado e exploração de brechas."
 light_armor_short:0 "Bld Leve"

 medium_armor:0 "Tanques Médios"
 medium_armor_desc:0 "Blindados versáteis com equilíbrio ideal entre proteção, poder de fogo e mobilidade tática."
 medium_armor_short:0 "Bld Médio"

 heavy_armor:0 "Tanques Pesados"
 heavy_armor_desc:0 "Colossos encouraçados com canhões de grosso calibre projetados para quebrar linhas estrincheiradas."
 heavy_armor_short:0 "Bld Pesado"

 # Artilharia e Apoio de Fogo
 artillery:0 "Artilharia de Suporte"
 artillery_desc:0 "Baterias de canhões e obuseiros fornecendo barragens de suporte tático direto à infantaria."
 artillery_short:0 "Art"

 artillery_brigade:0 "Artilharia de Campanha"
 artillery_brigade_desc:0 "Batalhão pesado de artilharia para bombardeios sistemáticos e destruição de posições inimigas."
 artillery_brigade_short:0 "Art Camp"

 mot_artillery_brigade:0 "Artilharia Motorizada"
 mot_artillery_brigade_desc:0 "Obuseiros pesados rebocados por tratores e caminhões para suporte veloz a divisões móveis."
 mot_artillery_brigade_short:0 "Art Mot"

 rocket_artillery:0 "Artilharia de Foguetes de Suporte"
 rocket_artillery_desc:0 "Lançadores de foguetes táticos leves capazes de desfechar saraivadas repentinas sobre o inimigo."
 rocket_artillery_short:0 "Fog"

 rocket_artillery_brigade:0 "Artilharia de Foguetes"
 rocket_artillery_brigade_desc:0 "Batalhão de lançadores múltiplos de foguetes para saturação imediata de grandes áreas do campo de batalha."
 rocket_artillery_brigade_short:0 "Fog Camp"

 mot_rocket_artillery_brigade:0 "Artilharia de Foguetes Motorizada"
 mot_rocket_artillery_brigade_desc:0 "Lançadores de foguetes montados sobre veículos motorizados com alta capacidade de 'atirar e mudar de posição'."
 mot_rocket_artillery_brigade_short:0 "Fog Mot"

 motorized_rocket_brigade:0 "Batalhão de Foguetes Motorizado"
 motorized_rocket_brigade_desc:0 "Unidade móvel de saturação por foguetes de barragem montada sobre caminhões."
 motorized_rocket_brigade_short:0 "Fog Mot"

 super_heavy_artillery:0 "Artilharia Superpesada"
 super_heavy_artillery_desc:0 "Gigantescas peças de cerco e obuseiros ferroviários para pulverizar as fortalezas mais maciças."
 super_heavy_artillery_short:0 "Art SPes"

 self_propelled_super_heavy_artillery:0 "Artilharia Autopropulsada Superpesada"
 self_propelled_super_heavy_artillery_desc:0 "Peças monstruosas de artilharia instaladas sobre plataformas blindadas sobre lagartas."
 self_propelled_super_heavy_artillery_short:0 "SP Art SPes"

 anti_tank:0 "Suporte Antitanque"
 anti_tank_desc:0 "Peças antitanque e canhões de tiro rápido para deter assaltos blindados inimigos."
 anti_tank_short:0 "AT"

 anti_tank_brigade:0 "Batalhão Antitanque"
 anti_tank_brigade_desc:0 "Batalhão dedicado de canhões pesados de alta velocidade para aniquilar veículos blindados adversários."
 anti_tank_brigade_short:0 "AT Camp"

 mot_anti_tank_brigade:0 "Antitanque Motorizado"
 mot_anti_tank_brigade_desc:0 "Canhões antitanque rebocados por caminhões rápidos para estabelecimento ágil de emboscadas."
 mot_anti_tank_brigade_short:0 "AT Mot"

 anti_air:0 "Suporte Antiaéreo"
 anti_air_desc:0 "Metralhadoras e canhões leves de tiro rápido para proteger as linhas contra ataques aéreos de baixa altitude."
 anti_air_short:0 "AA"

 anti_air_brigade:0 "Batalhão Antiaéreo"
 anti_air_brigade_desc:0 "Batalhões equipados com peças antiaéreas pesadas para dispersar esquadrilhas de bombardeiros adversárias."
 anti_air_brigade_short:0 "AA Camp"

 mot_anti_air_brigade:0 "Antiaéreo Motorizado"
 mot_anti_air_brigade_desc:0 "Baterias antiaéreas tracionadas por caminhões para acompanhar colunas blindadas e motorizadas."
 mot_anti_air_brigade_short:0 "AA Mot"

 # Companhias de Suporte
 engineer:0 "Engenheiros"
 engineer_desc:0 "Companhias de pioneiros especializadas em cavar trincheiras, armar alambrados, transpor rios e minar posições inimigas."
 engineer_short:0 "Eng"

 recon:0 "Reconhecimento"
 recon_desc:0 "Patrulhas de batedores e pelotões ligeiros encarregados de antecipar o contato com o inimigo."
 recon_short:0 "Rec"

 military_police:0 "Polícia Militar"
 military_police_desc:0 "Companhias de disciplina e segurança de retaguarda, aumentando o controle sobre territórios ocupados."
 military_police_short:0 "PM"

 maintenance_company:0 "Companhia de Manutenção"
 maintenance_company_desc:0 "Mecânicos e artífices que recuperam armamentos danificados e mantêm a disponibilidade de veículos."
 maintenance_company_short:0 "Manut"

 field_hospital:0 "Hospital de Campanha"
 field_hospital_desc:0 "Posto de primeiros socorros e triagem médica avançada para estancar baixas e recuperar homens feridos."
 field_hospital_short:0 "Hosp"

 logistics_company:0 "Companhia de Logística"
 logistics_company_desc:0 "Intendência avançada otimizando distribuição de munição, rações e combustível na linha de frente."
 logistics_company_short:0 "Log"

 signal_company:0 "Companhia de Comunicações"
 signal_company_desc:0 "Telefonistas, telegrafistas e operadores de rádio para coordenar manobras em tempo real."
 signal_company_short:0 "Com"

 # Navios Principais
 battleship:0 "Couraçado"
 battleship_desc:0 "Navio de linha de primeira classe dotado de couraça de aço e canhões monumentais de longo alcance."
 battleship_short:0 "BB"

 battle_cruiser:0 "Cruzador de Batalha"
 battle_cruiser_desc:0 "Navio capital veloz sacrificando parte da couraça para alcançar maior velocidade operacional."
 battle_cruiser_short:0 "BC"
"""

p_ww1_pt = ROOT / "localisation" / "braz_por" / "ww1_units_l_braz_por.yml"
p_ww1_pt.write_bytes(b"\xef\xbb\xbf" + ww1_units_pt_content.strip().encode("utf-8") + b"\n")
print(f"Written {p_ww1_pt} with UTF-8 BOM.")

# 3. Generate ww1_units_l_english.yml covering all ground, support, and naval units
ww1_units_en_content = """l_english:
 # Ground Battalions
 infantry:0 "Infantry"
 infantry_desc:0 "The backbone of any ground force, equipped with rifles, bayonets, and helmets to hold and assault defensive lines."
 infantry_short:0 "Inf"

 cavalry:0 "Cavalry"
 cavalry_desc:0 "Mounted regiments for patrol, rapid flanking, and pursuing retreating forces."
 cavalry_short:0 "Cav"

 motorized:0 "Motorized Infantry"
 motorized_desc:0 "Infantry transported by trucks to achieve rapid concentration and advance alongside mobile units."
 motorized_short:0 "Mot"

 mechanized:0 "Mechanized Infantry"
 mechanized_desc:0 "Troops protected in tracked armored vehicles, capable of fighting in close coordination with armor."
 mechanized_short:0 "Mech"

 mountaineers:0 "Mountaineers"
 mountaineers_desc:0 "Troops specialized in mountain warfare, climbing, and survival across harsh rugged peaks."
 mountaineers_short:0 "Mtn"

 marine:0 "Marines"
 marine_desc:0 "Amphibious assault troops specialized in storming hostile beaches and securing bridgeheads."
 marine_short:0 "Mar"

 marine_commando:0 "Marine Commandos"
 marine_commando_desc:0 "Elite naval commandos trained for daring behind-the-lines amphibious raids."
 marine_commando_short:0 "Cdo"

 paratrooper:0 "Paratroopers"
 paratrooper_desc:0 "Airborne assault troops trained to jump deep behind enemy fortified lines."
 paratrooper_short:0 "Para"

 bicycle_battalion:0 "Bicycle Battalion"
 bicycle_battalion_desc:0 "Agile infantry employing bicycles for swift road marches with zero fuel consumption."
 bicycle_battalion_short:0 "Bic"

 ranger_battalion:0 "Ranger Battalion"
 ranger_battalion_desc:0 "Scouts and deep reconnaissance patrols with superior survival and tactical agility."
 ranger_battalion_short:0 "Rgr"

 penal_battalion:0 "Penal Battalion"
 penal_battalion_desc:0 "Disciplinary formations assigned to high-risk missions and clearing barbed wire under fire."
 penal_battalion_short:0 "Penal"

 irregular_infantry:0 "Irregular Infantry"
 irregular_infantry_desc:0 "Regional militia, partisans, and levies armed with diverse small arms for local defense."
 irregular_infantry_short:0 "Irreg"

 militia:0 "Militia"
 militia_desc:0 "Territorial home-guard troops with basic training for static garrison and rear-area defense."
 militia_short:0 "Mil"

 fake_intel_unit:0 "Decoy Division (Dummy)"
 fake_intel_unit_desc:0 "Mock tents, wooden armor models, and false radio traffic to deceive enemy intelligence."
 fake_intel_unit_short:0 "Decoy"

 # Armor
 light_armor:0 "Light Armor"
 light_armor_desc:0 "Fast and agile light tanks equipped with light guns, ideal for reconnaissance and breakthrough exploitation."
 light_armor_short:0 "L Arm"

 medium_armor:0 "Medium Armor"
 medium_armor_desc:0 "Versatile tanks balancing armor protection, firepower, and tactical speed."
 medium_armor_short:0 "M Arm"

 heavy_armor:0 "Heavy Armor"
 heavy_armor_desc:0 "Thickly armored behemoths armed with high-caliber guns to crush fortified trench lines."
 heavy_armor_short:0 "H Arm"

 # Artillery & Fire Support
 artillery:0 "Support Artillery"
 artillery_desc:0 "Light field guns and howitzers providing immediate direct artillery support to frontline troops."
 artillery_short:0 "Art"

 artillery_brigade:0 "Artillery Brigade"
 artillery_brigade_desc:0 "Dedicated heavy field artillery battalion for systematic bombardment and destruction of fortifications."
 artillery_brigade_short:0 "Art Bde"

 mot_artillery_brigade:0 "Motorized Artillery"
 mot_artillery_brigade_desc:0 "Heavy howitzers towed by tractors or trucks for rapid deployment alongside motorized divisions."
 mot_artillery_brigade_short:0 "Mot Art"

 rocket_artillery:0 "Support Rocket Artillery"
 rocket_artillery_desc:0 "Tactical light rocket batteries providing sudden, devastating barrages upon concentrated enemy positions."
 rocket_artillery_short:0 "Rkt"

 rocket_artillery_brigade:0 "Rocket Artillery"
 rocket_artillery_brigade_desc:0 "Multiple rocket launcher battalion for saturation fire over broad sectors of the front."
 rocket_artillery_brigade_short:0 "Rkt Bde"

 mot_rocket_artillery_brigade:0 "Motorized Rocket Artillery"
 mot_rocket_artillery_brigade_desc:0 "Rocket launchers mounted on motorized trucks with rapid shoot-and-scoot capability."
 mot_rocket_artillery_brigade_short:0 "Mot Rkt"

 motorized_rocket_brigade:0 "Motorized Rocket Battalion"
 motorized_rocket_brigade_desc:0 "Mobile rocket artillery battalion delivering high-explosive saturation barrages."
 motorized_rocket_brigade_short:0 "Mot Rkt"

 super_heavy_artillery:0 "Super-Heavy Artillery"
 super_heavy_artillery_desc:0 "Colossal siege howitzers and railway guns built to obliterate the strongest permanent fortresses."
 super_heavy_artillery_short:0 "SH Art"

 self_propelled_super_heavy_artillery:0 "Super-Heavy SP Artillery"
 self_propelled_super_heavy_artillery_desc:0 "Enormous siege howitzers mounted upon tracked armored platforms."
 self_propelled_super_heavy_artillery_short:0 "SH SP Art"

 anti_tank:0 "Support Anti-Tank"
 anti_tank_desc:0 "Light anti-tank guns and high-velocity rifles to defend against armored thrusts."
 anti_tank_short:0 "AT"

 anti_tank_brigade:0 "Anti-Tank Brigade"
 anti_tank_brigade_desc:0 "Dedicated battalion of heavy high-velocity anti-tank guns to destroy enemy armored fighting vehicles."
 anti_tank_brigade_short:0 "AT Bde"

 mot_anti_tank_brigade:0 "Motorized Anti-Tank"
 mot_anti_tank_brigade_desc:0 "Anti-tank guns towed by fast trucks to set up lethal ambushes ahead of advancing hostile armor."
 mot_anti_tank_brigade_short:0 "Mot AT"

 anti_air:0 "Support Anti-Air"
 anti_air_desc:0 "Rapid-fire autocannons and heavy machine guns guarding frontline troops against low-altitude strafing."
 anti_air_short:0 "AA"

 anti_air_brigade:0 "Anti-Air Brigade"
 anti_air_brigade_desc:0 "Dedicated anti-aircraft artillery battalion to break up enemy bomber formations."
 anti_air_brigade_short:0 "AA Bde"

 mot_anti_air_brigade:0 "Motorized Anti-Air"
 mot_anti_air_brigade_desc:0 "Truck-mounted or towed anti-aircraft guns providing mobile air defense for mechanized spearheads."
 mot_anti_air_brigade_short:0 "Mot AA"

 # Support Companies
 engineer:0 "Engineers"
 engineer_desc:0 "Combat pioneers trained in trench digging, wire obstacle clearance, bridge building, and fort assault."
 engineer_short:0 "Eng"

 recon:0 "Reconnaissance"
 recon_desc:0 "Scouts and forward cavalry/light elements reporting enemy movements and guiding maneuvers."
 recon_short:0 "Rec"

 military_police:0 "Military Police"
 military_police_desc:0 "Rear-area security and discipline detachments suppressing local resistance and unrest."
 military_police_short:0 "MP"

 maintenance_company:0 "Maintenance Company"
 maintenance_company_desc:0 "Field mechanics and workshops salvaging damaged weaponry and keeping vehicle engines running."
 maintenance_company_short:0 "Maint"

 field_hospital:0 "Field Hospital"
 field_hospital_desc:0 "Forward medical dressing stations stabilizing wounded soldiers and conserving valuable manpower."
 field_hospital_short:0 "Hosp"

 logistics_company:0 "Logistics Company"
 logistics_company_desc:0 "Quartermaster teams optimizing fuel, ammunition, and food supply lines across difficult terrain."
 logistics_company_short:0 "Log"

 signal_company:0 "Signal Company"
 signal_company_desc:0 "Telegraph, field telephone, and wireless operators coordinating artillery and infantry movements."
 signal_company_short:0 "Sig"

 # Capital Ships
 battleship:0 "Battleship"
 battleship_desc:0 "First-rate dreadnought capital warship clad in thick armor plate and armed with massive main batteries."
 battleship_short:0 "BB"

 battle_cruiser:0 "Battlecruiser"
 battle_cruiser_desc:0 "High-speed capital warship trading armor thickness for supreme speed and heavy gunnery."
 battle_cruiser_short:0 "BC"
"""

p_ww1_en = ROOT / "localisation" / "english" / "ww1_units_l_english.yml"
p_ww1_en.write_bytes(b"\xef\xbb\xbf" + ww1_units_en_content.strip().encode("utf-8") + b"\n")
print(f"Written {p_ww1_en} with UTF-8 BOM.")

import os

# UTF-8 BOM
BOM = b'\xef\xbb\xbf'

# 1. Update ww1_characters
en_char = """
 SOV_maria_bochkareva:0 "Maria Bochkareva"
 SOV_maria_bochkareva_desc:0 "Commander of the 1st Russian Women's Battalion of Death, decorated with the Cross of St. George for extraordinary valor on the frontline."
"""

pt_char = """
 SOV_maria_bochkareva:0 "Maria Bochkareva"
 SOV_maria_bochkareva_desc:0 "Comandante do 1º Batalhão da Morte das Mulheres Russas, condecorada com a Cruz de São Jorge por extraordinária bravura no fronte de batalha."
"""

def append_to_file(path, content_str):
    if not os.path.exists(path):
        data = BOM + b"l_english:\n" + content_str.encode('utf-8')
    else:
        with open(path, 'rb') as f:
            raw = f.read()
        if not raw.startswith(BOM):
            raw = BOM + raw
        # decode
        text = raw[3:].decode('utf-8')
        if content_str.strip() not in text:
            text = text.rstrip() + '\n' + content_str.strip() + '\n'
        data = BOM + text.encode('utf-8')
    with open(path, 'wb') as f:
        f.write(data)

append_to_file('localisation/english/ww1_characters_l_english.yml', en_char)
append_to_file('localisation/braz_por/ww1_characters_l_braz_por.yml', pt_char)

# 2. Update ww1_russia_ideas
en_ideas = """
 SOV_goremykin_reactionary_cabinet:0 "Goremykin Reactionary Cabinet"
 SOV_goremykin_reactionary_cabinet_desc:0 "The elderly Premier Goremykin oversees a paralyzed, bureaucratic administration that resists cooperation with the Duma."
 SOV_progressive_coalition_cabinet:0 "Progressive Coalition Cabinet"
 SOV_progressive_coalition_cabinet_desc:0 "A broad coalition of public figures, industrial magnates, and Duma delegates working together to mobilize the home front."
 SOV_petrograd_soviet_order_no_1:0 "Petrograd Soviet Order No. 1"
 SOV_petrograd_soviet_order_no_1_desc:0 "Soldiers committees and dual power paralyze officer authority and undermine combat discipline."
 SOV_land_socialization_decree:0 "Decree on Land Socialization"
 SOV_land_socialization_decree_desc:0 "Transfer of landed estates to peasant agrarian soviets fulfills the centuries-old dream of land and liberty."
 SOV_all_russian_cheka:0 "All-Russian Extraordinary Commission (Cheka)"
 SOV_all_russian_cheka_desc:0 "The revolutionary sword and shield against counter-revolution, sabotage, and foreign espionage."
 SOV_declaration_rights_peoples:0 "Declaration of Rights of the Peoples of Russia"
 SOV_declaration_rights_peoples_desc:0 "Guarantees self-determination, autonomy, and cultural equality across the borderland nations."
 SOV_black_hundreds_paramilitaries:0 "Black Hundreds Armed Leagues"
 SOV_black_hundreds_paramilitaries_desc:0 "Fiercely loyal monarchist leagues patrol the streets to crush revolutionary sentiment."
 SOV_divine_autocracy:0 "Sacred Autocracy Restored"
 SOV_divine_autocracy_desc:0 "Nicholas II rules as the God-appointed sovereign over Holy Mother Russia."
 SOV_imperial_secret_police:0 "Purified Imperial Okhrana"
 SOV_imperial_secret_police_desc:0 "Relentless surveillance and counter-insurgency protect the imperial throne from subversion."
 SOV_undivided_autocratic_will:0 "Undivided Imperial Will"
 SOV_undivided_autocratic_will_desc:0 "Dissolution of the Duma removes parliamentary obstacles to direct imperial decrees."
 SOV_sacred_romanov_autocracy:0 "Sacred Romanov Dynasty"
 SOV_sacred_romanov_autocracy_desc:0 "Three hundred years of Romanov rule stands vindicated and unchallenged."
 SOV_grain_procurement_system:0 "Centralized Grain Requisition"
 SOV_grain_procurement_system_desc:0 "State monopoly over agricultural surpluses ensures rations reach army depots and munitions workers."
 SOV_defender_of_orthodox_christendom:0 "Defender of Orthodox Christendom"
 SOV_defender_of_orthodox_christendom_desc:0 "The Russian Empire stands as the rightful shield of all Orthodox peoples."
 SOV_shield_of_the_slavs:0 "Shield of the South Slavs"
 SOV_shield_of_the_slavs_desc:0 "Russia will not permit Austria-Hungary to extinguish Serbian independence."
 SOV_pan_slavic_patronage:0 "Pan-Slavic Patronage"
 SOV_pan_slavic_patronage_desc:0 "Diplomatic and military guarantees bind the Slavic nations under Russian leadership."
 GER_wartime_rationing_spirit:0 "Wartime Rationing (Kriegsbrot)"
 GER_wartime_rationing_spirit_desc:0 "Strict state rationing of flour and food staples protects civilian reserves during the naval blockade."
 GER_kaiserliche_weltmacht:0 "Kaiserliche Weltmacht"
 GER_kaiserliche_weltmacht_desc:0 "Germany's place in the sun is permanently cemented by decisive military victory."
 GER_democratic_franchise_reform:0 "Equal Universal Franchise"
 GER_democratic_franchise_reform_desc:0 "Abolition of the archaic Prussian three-class voting system establishes true representative democracy."
 GER_democratic_legitimacy:0 "Democratic Parliamentary Legitimacy"
 GER_democratic_legitimacy_desc:0 "The Reichstag and the Kaiser rule in harmonious constitutional partnership."
"""

pt_ideas = """
 SOV_goremykin_reactionary_cabinet:0 "Gabinete Reacionário de Goremykin"
 SOV_goremykin_reactionary_cabinet_desc:0 "O idoso Primeiro-Ministro Goremykin lidera uma administração paralisada que resiste a cooperar com a Duma."
 SOV_progressive_coalition_cabinet:0 "Gabinete de Coalizão Progressista"
 SOV_progressive_coalition_cabinet_desc:0 "Uma ampla coalizão de figuras públicas, industriais e delegados da Duma trabalhando para mobilizar a nação."
 SOV_petrograd_soviet_order_no_1:0 "Ordem nº 1 do Soviete de Petrogrado"
 SOV_petrograd_soviet_order_no_1_desc:0 "Comitês de soldados e o poder dual paralisam a autoridade dos oficiais e minam a disciplina."
 SOV_land_socialization_decree:0 "Decreto de Socialização da Terra"
 SOV_land_socialization_decree_desc:0 "A transferência de latifúndios para sovietes agrários realiza o sonho secular de terra e liberdade."
 SOV_all_russian_cheka:0 "Comissão Extraordinária de Toda a Rússia (Cheka)"
 SOV_all_russian_cheka_desc:0 "A espada e o escudo revolucionários contra a contra-revolução, sabotagem e espionagem."
 SOV_declaration_rights_peoples:0 "Declaração dos Direitos dos Povos da Rússia"
 SOV_declaration_rights_peoples_desc:0 "Garante autodeterminação, autonomia e igualdade cultural para todas as nações do império."
 SOV_black_hundreds_paramilitaries:0 "Legiões Armadas da Centúria Negra"
 SOV_black_hundreds_paramilitaries_desc:0 "Legiões monarquistas ferozmente leais patrulham as ruas para esmagar agitadores revolucionários."
 SOV_divine_autocracy:0 "Autocracia Sagrada Restaurada"
 SOV_divine_autocracy_desc:0 "Nicolau II governa como o soberano divinamente ungido sobre a Santa Mãe Rússia."
 SOV_imperial_secret_police:0 "Okhrana Imperial Purificada"
 SOV_imperial_secret_police_desc:0 "Vigilância implacável e contra-insurgência protegem o trono imperial de conspirações."
 SOV_undivided_autocratic_will:0 "Vontade Autocrática Indivisa"
 SOV_undivided_autocratic_will_desc:0 "A dissolução da Duma elimina os entraves parlamentares aos decretos imperiais diretos."
 SOV_sacred_romanov_autocracy:0 "Sagrada Dinastia Romanov"
 SOV_sacred_romanov_autocracy_desc:0 "Trezentos anos de soberania dos Romanov permanecem inabaláveis e vitoriosos."
 SOV_grain_procurement_system:0 "Requisição Centralizada de Grãos"
 SOV_grain_procurement_system_desc:0 "O monopólio estatal sobre excedentes agrícolas garante o abastecimento de depósitos militares e operários fabris."
 SOV_defender_of_orthodox_christendom:0 "Defensor da Cristandade Ortodoxa"
 SOV_defender_of_orthodox_christendom_desc:0 "O Império Russo ergue-se como o legítimo escudo protetor de todos os povos ortodoxos."
 SOV_shield_of_the_slavs:0 "Escudo dos Eslavos do Sul"
 SOV_shield_of_the_slavs_desc:0 "A Rússia jamais permitirá que a Áustria-Hungria aniquile a independência sérvia."
 SOV_pan_slavic_patronage:0 "Patronato Pan-Eslavo"
 SOV_pan_slavic_patronage_desc:0 "Garantias diplomáticas e militares unem os povos eslavos sob a liderança fraterna da Rússia."
 GER_wartime_rationing_spirit:0 "Racionamento em Tempo de Guerra (Kriegsbrot)"
 GER_wartime_rationing_spirit_desc:0 "Racionamento estatal estrito de farinha e gêneros alimentícios protege as reservas civis sob o bloqueio naval."
 GER_kaiserliche_weltmacht:0 "Kaiserliche Weltmacht"
 GER_kaiserliche_weltmacht_desc:0 "O lugar da Alemanha ao sol fica permanentemente consolidado pela vitória militar decisiva."
 GER_democratic_franchise_reform:0 "Sufrágio Universal Igualitário"
 GER_democratic_franchise_reform_desc:0 "A abolição do arcaico sistema de voto das três classes na Prússia estabelece a verdadeira democracia representativa."
 GER_democratic_legitimacy:0 "Legitimidade Parlamentar Democrática"
 GER_democratic_legitimacy_desc:0 "O Reichstag e o Kaiser governam em harmonia constitucional representativa."
"""

append_to_file('localisation/english/ww1_russia_ideas_l_english.yml', en_ideas)
append_to_file('localisation/braz_por/ww1_russia_ideas_l_braz_por.yml', pt_ideas)

# 3. Update ww1_diplomacy
en_dip = """
 ww1_diplomacy.70.t:0 "Constantinople and Straits Agreement"
 ww1_diplomacy.70.d:0 "The Imperial Russian Government has submitted formal claims to the Western Entente regarding Constantinople and the Turkish Straits. In exchange for continued total commitment to the defeat of the Central Powers, Russia requests recognition of its historic mission to control the Bosphorus and Dardanelles."
 ww1_diplomacy.70.a:0 "Recognize Russian Primacy over Tsargrad"
 ww1_diplomacy.70.b:0 "The Straits must remain international"
 ww1_diplomacy.71.t:0 "Constantinople Agreement Ratified"
 ww1_diplomacy.71.d:0 "France and the United Kingdom have formally signed the secret Constantinople Agreement of 1915, agreeing to Russian annexation of Tsargrad, Eastern Thrace, and the Straits upon victory over the Ottoman Empire."
 ww1_diplomacy.71.a:0 "The Cross shall rise over the Hagia Sophia!"
 SOV_constantinople_agreement_confirmed_tt:0 "§YThe Western Allies have officially recognized Russian claims to Constantinople and the Turkish Straits.§!"
 SOV_trabzon_amphibious_landing_tt:0 "§GSpawns the Caucasian Plastun Marine Brigade in Batumi with upgraded naval facilities.§!"
 SOV_bochkareva_recruited_tt:0 "§GRecruits General Maria Bochkareva and spawns the 1st Russian Women's Battalion of Death in Petrograd.§!"
"""

pt_dip = """
 ww1_diplomacy.70.t:0 "Acordo de Constantinopla e dos Estreitos"
 ww1_diplomacy.70.d:0 "O Governo Imperial Russo submeteu reivindicações formais à Entente Ocidental a respeito de Constantinopla e dos Estreitos Turcos. Em troca do compromisso total na derrota dos Impérios Centrais, a Rússia requer o reconhecimento de sua missão histórica de controlar o Bósforo e Dardanelos."
 ww1_diplomacy.70.a:0 "Reconhecer o Primado Russo sobre Tsargrad"
 ww1_diplomacy.70.b:0 "Os Estreitos devem permanecer internacionais"
 ww1_diplomacy.71.t:0 "Acordo de Constantinopla Ratificado"
 ww1_diplomacy.71.d:0 "A França e o Reino Unido assinaram formalmente o Tratado secreto de Constantinopla de 1915, concordando com a anexação russa de Tsargrad, Trácia Oriental e dos Estreitos após a vitória sobre o Império Otomano."
 ww1_diplomacy.71.a:0 "A Cruz erguer-se-á novamente sobre a Santa Sofia!"
 SOV_constantinople_agreement_confirmed_tt:0 "§YOs Aliados Ocidentais reconheceram formalmente as reivindicações russas a Constantinopla e aos Estreitos Turcos.§!"
 SOV_trabzon_amphibious_landing_tt:0 "§GCria a Brigada Plastun de Fuzileiros do Cáucaso em Batumi com instalações navais aprimoradas.§!"
 SOV_bochkareva_recruited_tt:0 "§GRecruta a General Maria Bochkareva e cria o 1º Batalhão da Morte das Mulheres Russas em Petrogrado.§!"
"""

append_to_file('localisation/english/ww1_diplomacy_l_english.yml', en_dip)
append_to_file('localisation/braz_por/ww1_diplomacy_l_braz_por.yml', pt_dip)

print("Successfully appended bilingual localisation with UTF-8 BOM!")

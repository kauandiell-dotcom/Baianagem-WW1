# scripts/eng_data_diplomacy.py
# British Empire WW1 - Diplomacy & Coalition Strategy (20 focuses)

DIPLOMACY_DATA = {
    "ENG_ww1_edward_grey_and_the_entente": {
        "pt_t": "Sir Edward Grey e a Entente Cordiale",
        "en_t": "Sir Edward Grey and the Entente Cordiale",
        "pt_d": "O Secretário de Relações Exteriores Sir Edward Grey conduz uma diplomacia firme para conter o expansionismo imperial alemão, estreitando laços com a França e a Rússia.",
        "en_d": "Foreign Secretary Sir Edward Grey pursues a determined diplomatic strategy to balance German expansionism, reinforcing bilateral understandings with France and Russia.",
        "reward": """add_political_power = 60
add_opinion_modifier = { target = FRA modifier = eng_fra_entente_understanding }
add_opinion_modifier = { target = RUS modifier = eng_rus_entente_understanding }
set_country_flag = ENG_ww1_grey_entente_cemented"""
    },
    "ENG_ww1_the_french_naval_understanding": {
        "pt_t": "O Acordo Naval Anglo-Francês de 1912",
        "en_t": "The French Naval Understanding",
        "pt_d": "Um acordo naval histórico transfere a frota de guerra francesa para o Mediterrâneo, enquanto a Royal Navy assume a defesa total do Canal da Mancha e do Atlântico Norte.",
        "en_d": "A historic naval distribution assigns the French Marine Nationale to secure the Mediterranean while the Royal Navy guarantees the English Channel and the North Sea.",
        "reward": """navy_experience = 25
add_political_power = 50
FRA = {
    add_opinion_modifier = {
        target = ENG
        modifier = entente_naval_understanding
    }
}"""
    },
    "ENG_ww1_french_staff_conversations": {
        "pt_t": "Conversações entre os Estados-Maiores Anglo-Franceses",
        "en_t": "French Staff Conversations",
        "pt_d": "O General Wilson e o Estado-Maior francês planejam secretamente o desembarque, rotas ferroviárias e setores de combate para a Força Expedicionária Britânica.",
        "en_d": "General Henry Wilson and the French General Staff secretly coordinate troop embarkation ports, railway timetables, and assembly zones for the British Expeditionary Force.",
        "reward": """army_experience = 20
add_political_power = 40"""
    },
    "ENG_ww1_continental_commitment": {
        "pt_t": "O Compromisso Continental",
        "en_t": "Continental Commitment",
        "pt_d": "A Grã-Bretanha declara inequivocamente que a segurança da Europa Ocidental e a integridade da França são vitais para a sobrevivência do Império Britânico.",
        "en_d": "Britain formally affirms that Western European liberty and the defense of northern France are inseparable from the sovereign security of the British Empire.",
        "reward": """add_war_support = 0.08
add_political_power = 50"""
    },
    "ENG_ww1_armed_neutrality": {
        "pt_t": "Neutralidade Armada e Alerta Estratégico",
        "en_t": "Armed Neutrality and Vigilance",
        "pt_d": "Enquanto as chancelarias buscam a paz, as defesas costeiras britânicas são guarnecidas e a Grand Fleet concentra seus esquadrões em alto mar.",
        "en_d": "While diplomatic avenues are exhausted, British coastal artillery is manned and the Grand Fleet quietly sails to its war stations in northern waters.",
        "reward": """add_stability = 0.08
add_war_support = 0.05"""
    },
    "ENG_ww1_belgian_treaty_obligations": {
        "pt_t": "O Tratado de Londres e a Neutralidade Belga",
        "en_t": "Belgian Treaty Obligations",
        "pt_d": "Invocando o solene Tratado de Londres de 1839, o Reino Unido entra na guerra contra o Império Alemão pela violação da neutralidade da Bélgica.",
        "en_d": "Upholding the solemn 1839 Treaty of London, Great Britain delivers an ultimatum demanding German withdrawal from neutral Belgium, entering the world conflict.",
        "reward": """give_guarantee = BEL
add_war_support = 0.10
add_stability = 0.05
set_country_flag = ENG_ww1_belgian_treaty_honored"""
    },
    "ENG_ww1_reconsider_the_continental_policy": {
        "pt_t": "Flexibilidade na Política Continental",
        "en_t": "Continental Policy Flexibility",
        "pt_d": "O Foreign Office avalia opções diplomáticas pragmáticas, assegurando que o Reino Unido mantenha sua liberdade de manobra e vantagens comerciais globais.",
        "en_d": "The Foreign Office reviews pragmatic diplomatic avenues, ensuring Britain maintains strategic maritime flexibility and international trade privileges.",
        "reward": """add_political_power = 60
add_stability = 0.03
set_country_flag = ENG_ww1_continental_policy_reviewed"""
    },
    "ENG_ww1_channel_expeditionary_coordination": {
        "pt_t": "Coordenação Expedicionária do Canal da Mancha",
        "en_t": "Channel Expeditionary Coordination",
        "pt_d": "A Marinha Real e o Almirantado estabelecem a 'Dover Patrol', garantindo que nenhum navio inimigo ameace a passagem de centenas de milhares de soldados ingleses para a França.",
        "en_d": "The Admiralty institutes the Dover Patrol and heavily minelands the Straits, securing the passage of millions of British soldiers and supplies into French ports.",
        "reward": """123 = {
    add_building_construction = {
        type = naval_base
        level = 1
        instant_build = yes
    }
}
navy_experience = 15"""
    },
    "ENG_ww1_russian_procurement_liaison": {
        "pt_t": "Missão de Suprimento ao Império Russo",
        "en_t": "Russian Procurement Liaison",
        "pt_d": "Técnicos e financiadores britânicos coordenam o envio de fuzis, obuses e matérias-primas essenciais para o Exército Imperial Russo pelos portos árticos.",
        "en_d": "British military missions and merchant convoys deliver armaments, heavy artillery, and critical components to Imperial Russia via Murmansk and Arkhangelsk.",
        "reward": """add_equipment_to_stockpile = {
    type = infantry_equipment_1
    amount = 3000
    producer = ENG
}
add_political_power = 40"""
    },
    "ENG_ww1_neutral_shipping_assurances": {
        "pt_t": "Garantias de Navegação para Países Neutros",
        "en_t": "Neutral Shipping Assurances",
        "pt_d": "Acordos diplomáticos com Holanda, Noruega e Dinamarca regulam o tráfego comercial no Mar do Norte, fechando o contrabando para a Alemanha sem provocar incidentes.",
        "en_d": "Diplomatic accords with the Netherlands, Norway, and Denmark regulate North Sea trade, sealing contraband routes into Germany while honoring neutral sensibilities.",
        "reward": """add_equipment_to_stockpile = {
    type = convoy
    amount = 50
    producer = ENG
}
add_political_power = 50"""
    },
    "ENG_ww1_american_credit_negotiations": {
        "pt_t": "Negociações de Crédito com os Estados Unidos",
        "en_t": "American Credit Negotiations",
        "pt_d": "A nomeação do banco J.P. Morgan como agente de compras britânico abre o monumental mercado financeiro e industrial dos Estados Unidos para a Entente.",
        "en_d": "Appointing J.P. Morgan as Britain's purchasing agent in New York opens vast commercial credit syndicates and munitions access across the United States.",
        "reward": """add_political_power = 100
add_equipment_to_stockpile = {
    type = support_equipment_1
    amount = 200
    producer = ENG
}"""
    },
    "ENG_ww1_italian_coalition_talks": {
        "pt_t": "As Negociações do Pacto de Londres com a Itália",
        "en_t": "Italian Coalition Talks",
        "pt_d": "Conversações diplomáticas secretas em Londres garantem a entrada da Itália na guerra ao lado da Entente em maio de 1915, abrindo um front alpino contra a Áustria-Hungria.",
        "en_d": "Secret negotiations in London secure Italy's entry into the Entente coalition in May 1915, pinning Austro-Hungarian armies along the Alpine frontier.",
        "reward": """add_opinion_modifier = { target = ITA modifier = eng_london_pact }
add_political_power = 60
set_country_flag = ENG_ww1_italy_entente_pact"""
    },
    "ENG_ww1_the_portuguese_connection": {
        "pt_t": "A Histórica Aliança Luso-Britânica",
        "en_t": "The Portuguese Connection",
        "pt_d": "A invocação do Tratado de Windsor de 1386 traz Portugal para o conflito, garantindo o Corpo Expedicionário Português (CEP) em Flandres e segurança colonial na África.",
        "en_d": "Invoking the historic Treaty of Windsor brings Portugal into the Allied coalition, deploying the Corpo Expedicionário Português to Flanders and securing African ports.",
        "reward": """give_guarantee = POR
add_opinion_modifier = { target = POR modifier = eng_ancient_alliance }
add_political_power = 50"""
    },
    "ENG_ww1_balkan_allied_coordination": {
        "pt_t": "Coordenação Aliada nos Bálcãs",
        "en_t": "Balkan Allied Coordination",
        "pt_d": "A expedição de Salonica e o apoio logístico à Sérvia, Romênia e Grécia sustentam o fronte meridional, ameaçando o flanco das Potências Centrais.",
        "en_d": "The Salonika expedition and munitions deliveries to Serbia, Romania, and Greece pin Bulgarian forces and destabilize the Central Powers' southern flank.",
        "reward": """add_political_power = 50
army_experience = 15"""
    },
    "ENG_ww1_coalition_shipping_priorities": {
        "pt_t": "Prioridades Marítimas da Coalizão",
        "en_t": "Coalition Shipping Priorities",
        "pt_d": "O Conselho Aliado de Transporte Marítimo reúne navios mercantes britânicos, franceses e italianos sob alocação conjunta, garantindo trigo e carvão onde forem vitais.",
        "en_d": "The Allied Maritime Transport Council pools merchant tonnage, coordinating grain, coal, and ore shipments to sustain Allied industrial resilience.",
        "reward": """add_equipment_to_stockpile = {
    type = convoy
    amount = 75
    producer = ENG
}
navy_experience = 15"""
    },
    "ENG_ww1_the_supreme_war_council": {
        "pt_t": "O Conselho Supremo de Guerra de Versalhes",
        "en_t": "The Supreme War Council",
        "pt_d": "A criação de um comando estratégico unificado em Versalhes sob o Generalíssimo Ferdinand Foch harmoniza as ofensivas britânicas, francesas e americanas em 1918.",
        "en_d": "Establishing the Supreme War Council and appointing Generalissimo Ferdinand Foch to overall Allied command synchronizes the decisive 1918 counteroffensives.",
        "reward": """army_experience = 25
navy_experience = 20
add_political_power = 50"""
    },
    "ENG_ww1_armistice_consultations": {
        "pt_t": "Consultas para o Armistício",
        "en_t": "Armistice Consultations",
        "pt_d": "Os líderes aliados formulam as cláusulas incontornáveis de cessar-fogo: entrega da frota alemã, evacuação da Bélgica e ocupação da Renânia.",
        "en_d": "Allied heads of state draft uncompromising armistice terms: the surrender of the High Seas Fleet, total evacuation of occupied territories, and Allied control of the Rhine.",
        "reward": """add_political_power = 75
add_war_support = 0.05
set_country_flag = ENG_ww1_armistice_conditions_drafted"""
    },
    "ENG_ww1_reconstruction_credit_negotiations": {
        "pt_t": "Negociações de Crédito para a Reconstrução",
        "en_t": "Reconstruction Credit Negotiations",
        "pt_d": "Negociações financeiras entre Londres, Paris e Washington estabelecem moratórias responsáveis e investimentos cooperativos para reerguer a Europa devastada.",
        "en_d": "Financial conferences between London, Paris, and Washington establish orderly repayment frameworks and capital injections to rebuild European trade.",
        "reward": """126 = {
    add_extra_state_shared_building_slots = 1
    add_building_construction = {
        type = industrial_complex
        level = 1
        instant_build = yes
    }
}
add_political_power = 50"""
    },
    "ENG_ww1_the_naval_disarmament_conference": {
        "pt_t": "A Conferência de Desarmamento Naval",
        "en_t": "The Naval Disarmament Conference",
        "pt_d": "Diplomatas britânicos lideram o debate para fixar proporções globais de encouraçados (o Tratado de Washington), aliviando despesas sem perder a supremacia do mar.",
        "en_d": "British delegates take the lead in formulating capital ship tonnage ratios at Washington, restraining a costly naval arms race while preserving imperial security.",
        "reward": """add_stability = 0.08
add_political_power = 60"""
    },
    "ENG_ww1_a_european_security_settlement": {
        "pt_t": "O Acordo de Segurança Europeia e a Liga das Nações",
        "en_t": "A European Security Settlement",
        "pt_d": "A adesão britânica à Liga das Nações e a consagração do direito internacional inauguram uma nova ordem diplomática fundada na autodeterminação e na mediação pacífica.",
        "en_d": "British founding sponsorship of the League of Nations and the codification of collective security establish a diplomatic order anchored in international law.",
        "reward": """add_stability = 0.10
add_political_power = 80"""
    }
}

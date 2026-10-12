# scripts/eng_data_tech_intel.py
# British Empire WW1 - Science, Technology & Secret Intelligence (Room 40) (20 focuses)

TECH_INTEL_DATA = {
    "ENG_ww1_the_national_physical_laboratory": {
        "pt_t": "O Laboratório Físico Nacional (NPL) de Teddington",
        "en_t": "The National Physical Laboratory",
        "pt_d": "O NPL estabelece padrões científicos soberanos em metrologia, aerodinâmica e termodinâmica, fornecendo precisão inigualável à engenharia britânica.",
        "en_d": "The NPL at Teddington standardizes sovereign scientific norms in metrology, aerodynamics, and materials testing, giving British industry precision rigor.",
        "reward": """add_ideas = ENG_ww1_npl_standards
add_research_slot = 1
add_political_power = 50"""
    },
    "ENG_ww1_university_military_contracts": {
        "pt_t": "Contratos Universitários de Pesquisa Militar",
        "en_t": "University Military Research Contracts",
        "pt_d": "Os laboratórios Cavendish de Cambridge, Oxford e o Imperial College canalizam as maiores mentes acadêmicas para desvendar soluções bélicas de vanguarda.",
        "en_d": "The Cavendish Laboratory at Cambridge, Oxford, and Imperial College harness world-leading physicists and chemists to solve urgent wartime engineering puzzles.",
        "reward": """add_ideas = ENG_ww1_university_research
add_tech_bonus = {
    name = university_science_bonus
    bonus = 1.0
    uses = 2
    category = electronics
}
add_political_power = 40"""
    },
    "ENG_ww1_ordnance_metallurgy_research": {
        "pt_t": "Metalurgia Avançada de Blindagens de Sheffield",
        "en_t": "Sheffield Ordnance Metallurgy Research",
        "pt_d": "Ligas especiais de aço-níquel-cromo desenvolvidas em Sheffield resistem ao impacto de projéteis perfurantes e aumentam a vida útil das almas de canhões.",
        "en_d": "Specialized nickel-chromium alloy steels developed in Sheffield withstand high-velocity penetrations and multiply artillery barrel wear endurance.",
        "reward": """add_tech_bonus = {
    name = metallurgy_bonus
    bonus = 1.0
    uses = 2
    category = industry
}
add_ideas = ENG_ww1_ordnance_metallurgy"""
    },
    "ENG_ww1_machine_tool_standards": {
        "pt_t": "Padronização de Tornos e Ferramentas Mecânicas",
        "en_t": "Machine Tool Standardization",
        "pt_d": "Gabaritos e matrizes universais permitem que pequenas oficinas familiares fabriquem peças de fuzis e obuses com tolerâncias micrométricas perfeitamente intercambiáveis.",
        "en_d": "Standardized jigs, fixtures, and micrometric gauges enable thousands of subcontracted workshops to produce flawlessly interchangeable weapon components.",
        "reward": """add_ideas = ENG_ww1_machine_tool_standards
add_political_power = 40"""
    },
    "ENG_ww1_railway_engineering_standards": {
        "pt_t": "Padronização da Engenharia Ferroviária",
        "en_t": "Railway Engineering Standards",
        "pt_d": "Projetos de locomotivas pesadas e vagões-plataforma com freios automáticos Westinghouse aceleram o transporte de carretas de artilharia pesada e carvão.",
        "en_d": "Heavy locomotive blueprints and standardized rolling stock with automatic Westinghouse brakes accelerate the haulage of super-heavy siege railguns.",
        "reward": """add_tech_bonus = {
    name = trains_bonus
    bonus = 1.0
    uses = 1
    category = train_tech
}
add_political_power = 40"""
    },
    "ENG_ww1_naval_architecture_research": {
        "pt_t": "Pesquisa de Arquitetura Naval e Hidrodinâmica em Haslar",
        "en_t": "Naval Architecture Research at Haslar",
        "pt_d": "Tanques de teste de modelos hidrodinâmicos em Haslar refinam o desenho de proas e cascos com bulbo, elevando a velocidade dos encouraçados com menor consumo de óleo.",
        "en_d": "Experimental hydrodynamic towing tanks at Haslar refine hull flare and bulbous bows, maximizing capital ship knots while curbing oil expenditure.",
        "reward": """add_tech_bonus = {
    name = naval_arch_bonus
    bonus = 1.0
    uses = 2
    category = naval_equipment
}
add_navy_experience = 20"""
    },
    "ENG_ww1_explosive_safety_research": {
        "pt_t": "Pesquisa de Segurança Química de Explosivos (Amatol)",
        "en_t": "Explosive Chemistry and Amatol Research",
        "pt_d": "O desenvolvimento do Amatol (mistura de TNT e nitrato de amônio) supera a escassez de explosivos, garantindo detonações seguras sem risco de acidentes em paióis.",
        "en_d": "Pioneering Amatol propellant blends solves acute TNT shortages while rigid stabilization chemical formulas eliminate horrific magazine flash accidents.",
        "reward": """add_tech_bonus = {
    name = explosives_bonus
    bonus = 1.0
    uses = 1
    category = industry
}
add_stability = 0.04"""
    },
    "ENG_ww1_field_wireless_research": {
        "pt_t": "Equipamentos de Rádio de Campanha da Marconi",
        "en_t": "Marconi Field Wireless Transmitters",
        "pt_d": "Transmissores de faísca portáteis montados em caminhões e mochilas conectam quartéis-generais de divisão diretamente aos fronts avançados de combate.",
        "en_d": "Portable pack and vehicle-mounted spark transmitters engineered with Marconi link corps headquarters directly to forward artillery coordination posts.",
        "reward": """add_tech_bonus = {
    name = wireless_bonus
    bonus = 1.0
    uses = 1
    category = electronics
}
add_ideas = ENG_ww1_field_wireless"""
    },
    "ENG_ww1_signals_intelligence_organisation": {
        "pt_t": "Organização do Serviço de Inteligência de Sinais",
        "en_t": "Signals Intelligence Organisation",
        "pt_d": "Redes de escuta eletromagnética monitoram o tráfego de rádio das marinhas e exércitos centrais, alimentando os analistas britânicos com dados vitais.",
        "en_d": "Electromagnetic interception stations across Britain intercept telegraphic traffic, feeding cryptanalysts with raw intelligence on enemy troop movements.",
        "reward": """add_ideas = ENG_ww1_signals_intelligence
add_political_power = 50"""
    },
    "ENG_ww1_the_room_forty_office": {
        "pt_t": "O Lendário Room 40 e o Telegrama Zimmermann",
        "en_t": "The Legendary Room 40 and Zimmermann Telegram",
        "pt_d": "A seção criptográfica ultra-secreta do Almirantado sob o Almirante Hall decifra códigos navais alemães e intercepta o Telegrama Zimmermann, alterando o curso da história.",
        "en_d": "The Admiralty's clandestine cryptanalysis bureau under Admiral 'Blinker' Hall deciphers German naval ciphers and intercepts the momentous Zimmermann Telegram.",
        "reward": """add_ideas = ENG_ww1_room_forty
add_political_power = 75
add_war_support = 0.08
set_country_flag = ENG_ww1_room_40_active"""
    },
    "ENG_ww1_aerial_photography_research": {
        "pt_t": "Pesquisa em Aerofotogrametria Estereoscópica",
        "en_t": "Stereoscopic Aerial Photography",
        "pt_d": "Câmeras estereoscópicas revelam a profundidade de trincheiras, casamatas subterrâneas e ninhos de metralhadoras camuflados com precisão matemática.",
        "en_d": "Stereoscopic cameras reveal trench depths, subterranean concrete dugouts, and camouflaged battery positions with mathematical precision.",
        "reward": """add_tech_bonus = {
    name = aerial_recon_bonus
    bonus = 1.0
    uses = 1
    category = air_doctrine
}
add_air_experience = 15"""
    },
    "ENG_ww1_artillery_survey_mathematics": {
        "pt_t": "Sondagem Sonora e Matemática de Artilharia (Bragg)",
        "en_t": "Sound Ranging and Artillery Mathematics",
        "pt_d": "O jovem físico Lawrence Bragg desenvolve sistemas de microfones subterrâneos que calculam a localização exata de baterias alemãs pelo estrondo dos canhões.",
        "en_d": "Nobel laureate Lawrence Bragg develops sound-ranging microphone arrays that pinpoint hidden German heavy batteries within seconds of firing.",
        "reward": """add_ideas = ENG_ww1_sound_ranging_math
add_army_experience = 20"""
    },
    "ENG_ww1_chemical_protection_research": {
        "pt_t": "Centro de Defesa Química de Porton Down",
        "en_t": "Porton Down Chemical Protection Research",
        "pt_d": "Cientistas em Porton Down desenvolvem filtros de carvão ativado e tecidos impermeabilizantes capazes de neutralizar gás cloro, fosgênio e gás mostarda.",
        "en_d": "Scientists at Porton Down engineer activated-charcoal filters and neutralizing ointments to completely shield Allied soldiers from mustard and phosgene gas.",
        "reward": """add_ideas = ENG_ww1_porton_down_protection
add_tech_bonus = {
    name = support_bonus
    bonus = 1.0
    uses = 1
    category = support_tech
}"""
    },
    "ENG_ww1_the_landships_technical_committee": {
        "pt_t": "Comitê Técnico de Navios Terrestres (Landships)",
        "en_t": "The Landships Technical Committee",
        "pt_d": "O comitê secreto fundado por Churchill e Eustace Tennyson d'Eyncourt projeta lagartas envolventes e blindagens balísticas para cruzar trincheiras de 3 metros.",
        "en_d": "Churchill's clandestine Landships Committee designs rhomboid wrap-around tracks and bulletproof hulls capable of crossing 9-foot trench spans.",
        "reward": """add_ideas = ENG_ww1_landships_technical
add_tech_bonus = {
    name = heavy_armor_bonus
    bonus = 1.0
    uses = 2
    category = armor
}
add_army_experience = 20"""
    },
    "ENG_ww1_aircraft_engine_research": {
        "pt_t": "Pesquisa de Compressores e Motores Aeronáuticos",
        "en_t": "Aero Engine Supercharging Research",
        "pt_d": "Engenheiros da Royal Aircraft Factory desenvolvem compressores mecânicos e carburadores calibrados para combate em altitudes superiores a 5.000 metros.",
        "en_d": "Royal Aircraft Factory engineers design mechanical superchargers and high-altitude carburetors to dominate the thin air above 18,000 feet.",
        "reward": """add_tech_bonus = {
    name = air_engine_bonus
    bonus = 1.0
    uses = 1
    category = light_fighter
}
add_air_experience = 15"""
    },
    "ENG_ww1_hydrophone_analysis_laboratory": {
        "pt_t": "Laboratório de Análise Acústica e o Sonar ASDIC",
        "en_t": "ASDIC Acoustic Analysis Laboratory",
        "pt_d": "O comitê BIR (Board of Invention and Research) sob Ernest Rutherford desenvolve cristais de quartzo piezelétricos, criando o sonar ativo (ASDIC) pioneiro.",
        "en_d": "Ernest Rutherford and Allied researchers develop piezoelectric quartz transducers, birthing the world's first active acoustic submarine detection (ASDIC).",
        "reward": """add_ideas = ENG_ww1_asdic_sonar
add_navy_experience = 20"""
    },
    "ENG_ww1_production_quality_standards": {
        "pt_t": "Normas Nacionais de Qualidade de Produção",
        "en_t": "Production Quality Standards",
        "pt_d": "A Associação Britânica de Padrões de Engenharia (BSI) estabelece tolerâncias industriais rigorosas para parafusos, porcas, aços e rolamentos em todo o Império.",
        "en_d": "The British Engineering Standards Association enforces strict tolerances across all imperial armaments plants, dramatically reducing factory waste.",
        "reward": """add_ideas = ENG_ww1_production_standards
add_political_power = 40"""
    },
    "ENG_ww1_the_postwar_research_council": {
        "pt_t": "Conselho de Pesquisa Científica e Industrial (DSIR)",
        "en_t": "Department of Scientific and Industrial Research",
        "pt_d": "A criação do DSIR consolida o financiamento permanente da pesquisa científica aplicada, mantendo o Reino Unido na liderança tecnológica mundial.",
        "en_d": "Founding the DSIR cements state-sponsored scientific and industrial innovation, ensuring British technological leadership into the postwar era.",
        "reward": """add_ideas = ENG_ww1_postwar_research_council
add_political_power = 60"""
    },
    "ENG_ww1_industrial_patent_exchanges": {
        "pt_t": "Intercâmbio de Patentes Industriais Anglo-Aliadas",
        "en_t": "Anglo-Allied Industrial Patent Exchanges",
        "pt_d": "Compartilhamento mútuo de patentes de química industrial, processos de refino de petróleo e eletromecânica acelera a modernização de manufaturas civis.",
        "en_d": "Reciprocal patent pooling in industrial chemistry, optical glass, and petroleum cracking accelerates postwar manufacturing modernizations.",
        "reward": """add_ideas = ENG_ww1_patent_exchanges
add_tech_bonus = {
    name = postwar_tech_bonus
    bonus = 1.0
    uses = 1
    category = industry
}"""
    },
    "ENG_ww1_technical_education_for_reconstruction": {
        "pt_t": "Educação Técnica Superior para a Reconstrução",
        "en_t": "Technical Education for Reconstruction",
        "pt_d": "Faculdades politécnicas e institutos de mecânica aplicada formam centenas de milhares de engenheiros, químicos e arquitetos civis para o futuro britânico.",
        "en_d": "Polytechnic colleges and mechanical institutes qualify hundreds of thousands of certified engineers, chemists, and architects for Britain's future.",
        "reward": """add_ideas = ENG_ww1_technical_education
add_political_power = 75
add_stability = 0.05"""
    }
}

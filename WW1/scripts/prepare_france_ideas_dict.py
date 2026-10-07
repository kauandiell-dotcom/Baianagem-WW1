# -*- coding: utf-8 -*-
"""Definitions for all French WW1 National Spirits & Ideas.
Ensures zero banned modifiers, balanced values, and rich flavor.
"""

ALL_FRENCH_IDEAS = {
    # -------------------------------------------------------------
    # Starting / Evolved Spirits (From history & Political Wing)
    # -------------------------------------------------------------
    'FRA_republican_vigilance': {
        'name_en': 'Republican Vigilance',
        'name_pt': 'Vigilância Republicana',
        'desc_en': 'The institutions of the Third Republic stand guarded against monarchist, clerical, and authoritarian intrigue through civic dedication.',
        'desc_pt': 'As instituições da Terceira República permanecem guardadas contra intrigas monarquistas, clericais e autoritárias pela dedicação cívica.',
        'modifier': {
            'political_power_gain': 0.10,
            'stability_factor': 0.05,
        }
    },
    'FRA_secular_civic_order': {
        'name_en': 'Secular Civic Order',
        'name_pt': 'Ordem Cívica Secular',
        'desc_en': 'The separation of church and state has solidified civil society and public education as the foundation of modern French democracy.',
        'desc_pt': 'A separação entre Igreja e Estado consolidou a sociedade civil e a educação pública como base da democracia francesa moderna.',
        'modifier': {
            'political_power_gain': 0.05,
            'stability_factor': 0.04,
            'research_speed_factor': 0.03,
        }
    },
    'FRA_parliamentary_equilibrium': {
        'name_en': 'Parliamentary Equilibrium',
        'name_pt': 'Equilíbrio Parlamentar',
        'desc_en': 'Careful coalitions between radicals and moderates maintain steady republican governance through parliamentary consensus.',
        'desc_pt': 'Coalisões cuidadosas entre radicais e moderados mantêm a governança republicana estável por meio do consenso parlamentar.',
        'modifier': {
            'political_power_factor': 0.08,
            'stability_factor': 0.05,
        }
    },
    'FRA_competent_civil_administration': {
        'name_en': 'Meritocratic Civil Administration',
        'name_pt': 'Administração Civil Meritocrática',
        'desc_en': 'Rigorous competitive examinations and professional prefectures ensure administrative efficiency throughout metropolitan France.',
        'desc_pt': 'Concursos públicos rigorosos e prefeituras profissionais garantem a eficiência administrativa em toda a França metropolitana.',
        'modifier': {
            'production_speed_industrial_complex_factor': 0.05,
            'production_speed_infrastructure_factor': 0.05,
            'political_power_gain': 0.05,
        }
    },
    'FRA_socialist_labor_peace': {
        'name_en': 'Socialist Labor Compact',
        'name_pt': 'Pacto Trabalhista Socialista',
        'desc_en': 'Constructive dialogue with reformist socialists and labor unions maintains social peace in crucial industrial sectors.',
        'desc_pt': 'O diálogo construtivo com socialistas reformistas e sindicatos operários mantém a paz social em setores industriais cruciais.',
        'modifier': {
            'stability_factor': 0.06,
            'industrial_capacity_factory': 0.04,
            'consumer_goods_factor': 0.01,
        }
    },
    'FRA_employer_union_compact': {
        'name_en': 'Tripartite Social Accord',
        'name_pt': 'Acordo Social Tripartite',
        'desc_en': 'State arbitration between employers and workers prevents paralyzing strikes during vital infrastructure projects.',
        'desc_pt': 'A arbitragem estatal entre patrões e operários evita greves paralisantes durante projetos vitais de infraestrutura.',
        'modifier': {
            'industrial_capacity_factory': 0.05,
            'stability_factor': 0.03,
        }
    },
    'FRA_three_year_conscription': {
        'name_en': 'Three-Year Service Law',
        'name_pt': 'Lei do Serviço Militar de Três Anos',
        'desc_en': 'Extending compulsory service to three years offsets France’s demographic deficit, providing active divisions ready at the border.',
        'desc_pt': 'Estender o serviço obrigatório para três anos compensa o déficit demográfico da França, fornecendo divisões prontas na fronteira.',
        'modifier': {
            'conscription_factor': 0.15,
            'training_time_army_factor': -0.10,
            'political_power_factor': -0.05,
        }
    },
    'FRA_three_year_law_and_colonial_ranks': {
        'name_en': 'Extended Conscription & Colonial Ranks',
        'name_pt': 'Conscrição Ampliada e Fileiras Coloniais',
        'desc_en': 'Combining metropolitan three-year service with recruitment from North and West Africa ensures substantial strategic reserves.',
        'desc_pt': 'Combinar o serviço de três anos metropolitano com o recrutamento do norte e oeste africanos garante reservas estratégicas robustas.',
        'modifier': {
            'conscription_factor': 0.18,
            'non_core_manpower': 0.04,
            'political_power_factor': -0.05,
        }
    },
    'FRA_poincare_presidency': {
        'name_en': 'Poincaré Presidency',
        'name_pt': 'Presidência Poincaré',
        'desc_en': 'Raymond Poincaré brings unyielding firmness, national pride, and diplomatic resolve to the Élysée Palace.',
        'desc_pt': 'Raymond Poincaré traz firmeza inabalável, orgulho nacional e determinação diplomática ao Palácio do Eliseu.',
        'modifier': {
            'war_support_factor': 0.08,
            'stability_factor': 0.05,
            'political_power_gain': 0.10,
        }
    },
    'FRA_poincare_national_firmness': {
        'name_en': 'Poincaré National Firmness',
        'name_pt': 'Firmeza Nacional de Poincaré',
        'desc_en': 'Firm patriotic leadership strengthens national unity and signals unwavering commitment to France’s treaty allies.',
        'desc_pt': 'A liderança patriótica firme fortalece a unidade nacional e sinaliza compromisso inabalável com os aliados de tratado da França.',
        'modifier': {
            'war_support_factor': 0.10,
            'stability_factor': 0.06,
            'political_power_gain': 0.12,
        }
    },
    'FRA_pams_conciliatory_presidency': {
        'name_en': 'Pams Conciliatory Presidency',
        'name_pt': 'Presidência Conciliatória de Pams',
        'desc_en': 'Jules Pams pursues a moderate, pacifist policy aimed at defusing European flashpoints through multilateral arbitration.',
        'desc_pt': 'Jules Pams adota uma política moderada e pacifista com o objetivo de desarmar crises europeias por arbitragem multilateral.',
        'modifier': {
            'stability_factor': 0.08,
            'trade_laws_cost_factor': -0.15,
            'war_support_factor': -0.05,
        }
    },
    'FRA_union_sacree_spirit': {
        'name_en': "L'Union Sacrée",
        'name_pt': 'A União Sagrada',
        'desc_en': 'All political rivalries dissolve into solemn solidarity to defend France against foreign invasion.',
        'desc_pt': 'Todas as rivalidades políticas dissolvem-se em solidariedade solene para defender a França contra a invasão estrangeira.',
        'modifier': {
            'stability_factor': 0.12,
            'war_support_factor': 0.15,
            'political_power_factor': 0.10,
        }
    },
    'FRA_war_cabinet_discipline': {
        'name_en': 'War Cabinet Executive Discipline',
        'name_pt': 'Disciplina do Gabinete de Guerra',
        'desc_en': 'Streamlined executive authority ensures prompt wartime decisions and decisive resource coordination.',
        'desc_pt': 'A autoridade executiva enxuta garante decisões ágeis em tempos de guerra e coordenação decisiva de recursos.',
        'modifier': {
            'political_power_gain': 0.15,
            'war_support_factor': 0.05,
        }
    },
    'FRA_clemenceau_iron_resolve': {
        'name_en': 'Je Fais la Guerre (Clemenceau)',
        'name_pt': 'Eu Faço a Guerra (Clemenceau)',
        'desc_en': 'Georges Clemenceau embodies absolute determination: no compromise, no pacifism, only total victory.',
        'desc_pt': 'Georges Clemenceau personifica a determinação absoluta: sem trégua, sem pacifismo, apenas vitória total.',
        'modifier': {
            'war_support_factor': 0.15,
            'stability_weekly': 0.001,
            'surrender_limit': -0.10,
            'drift_defence_factor': 0.25,
        }
    },
    'FRA_wards_of_the_nation_care': {
        'name_en': 'Pupilles de la Nation',
        'name_pt': 'Pupilos da Nação',
        'desc_en': 'The Republic adopts the war orphans and cares for widowed families, cementing societal gratitude and moral strength.',
        'desc_pt': 'A República adota os órfãos de guerra e ampara as famílias viúvas, cimentando a gratidão social e a força moral.',
        'modifier': {
            'stability_factor': 0.06,
            'conscription_factor': 0.03,
            'consumer_goods_factor': 0.01,
        }
    },
    'FRA_versailles_supreme_guarantor': {
        'name_en': 'Guarantor of European Order',
        'name_pt': 'Garantidor da Ordem Europeia',
        'desc_en': 'Victorious and resolute, France stands as the principal guarantor of peace and democratic treaties in continental Europe.',
        'desc_pt': 'Vitoriosa e resoluta, a França ergue-se como o principal garantidor da paz e dos tratados democráticos na Europa continental.',
        'modifier': {
            'political_power_gain': 0.20,
            'stability_factor': 0.10,
            'war_support_factor': 0.05,
        }
    },

    # -------------------------------------------------------------
    # Economic Wing Ideas
    # -------------------------------------------------------------
    'FRA_bank_of_france_gold_bullion': {
        'name_en': 'Bank of France Gold Reserves',
        'name_pt': 'Reservas de Ouro do Banco da França',
        'desc_en': 'Substantial gold bullion reserves provide extraordinary creditworthiness and stable foreign exchange for vital overseas imports.',
        'desc_pt': 'Reservas substanciais em barras de ouro garantem crédito extraordinário e estabilidade cambial para importações vitais do exterior.',
        'modifier': {
            'trade_laws_cost_factor': -0.15,
            'consumer_goods_factor': -0.02,
            'political_power_gain': 0.05,
        }
    },
    'FRA_chemical_explosives_industry': {
        'name_en': 'Chemical Explosives Syndicate',
        'name_pt': 'Sindicato de Explosivos Químicos',
        'desc_en': 'Advanced chemical plants along the Rhône synthesize cordite, nitrocellulose, and trinitrotoluene on a massive scale.',
        'desc_pt': 'Instalações químicas avançadas ao longo do Ródano sintetizam cordite, nitrocelulose e trinitrotolueno em escala maciça.',
        'modifier': {
            'industrial_capacity_factory': 0.05,
            'army_artillery_attack_factor': 0.04,
        }
    },
    'FRA_rouen_coal_dispatch': {
        'name_en': 'Rouen Maritime Coal Terminal',
        'name_pt': 'Terminal Carvoeiro de Rouen',
        'desc_en': 'Dredged docks and specialized cranes unload Welsh and Scottish coal swiftly into river barges heading for Paris.',
        'desc_pt': 'Docas dragadas e guindastes especializados descarregam carvão galês e escocês rapidamente em barcaças rumo a Paris.',
        'modifier': {
            'supply_consumption_factor': -0.05,
            'production_speed_infrastructure_factor': 0.08,
        }
    },
    'FRA_shell_crisis_1914': {
        'name_en': 'The Shell Crisis of 1914',
        'name_pt': 'A Crise de Munições de 1914',
        'desc_en': 'Unprecedented artillery consumption has emptied metropolitan arsenals, forcing emergency rationing of 75mm shells.',
        'desc_pt': 'O consumo sem precedentes de artilharia esvaziou os arsenais metropolitanos, forçando o racionamento emergencial de projéteis de 75mm.',
        'modifier': {
            'army_artillery_attack_factor': -0.15,
            'industrial_capacity_factory': -0.05,
        }
    },
    'FRA_albert_thomas_munitions_boom': {
        'name_en': 'Albert Thomas Industrial Mobilization',
        'name_pt': 'Mobilização Industrial de Albert Thomas',
        'desc_en': 'Under Socialist Undersecretary Albert Thomas, private factories, arsenals, and civil workshops unite in record shell production.',
        'desc_pt': 'Sob a liderança de Albert Thomas, fábricas privadas, arsenais e oficinas civis unem-se em uma produção recorde de munições.',
        'modifier': {
            'industrial_capacity_factory': 0.12,
            'production_speed_arms_factory_factor': 0.10,
        }
    },
    'FRA_skilled_workforce_recall': {
        'name_en': 'Affectés Spéciaux (Mechanic Recall)',
        'name_pt': 'Affectés Spéciaux (Retorno dos Especialistas)',
        'desc_en': 'Skilled machinists, metallurgists, and chemists are recalled from frontline trenches to staff high-precision war factories.',
        'desc_pt': 'Mecânicos experientes, metalúrgicos e químicos são retirados das trincheiras para operar indústrias bélicas de alta precisão.',
        'modifier': {
            'industrial_capacity_factory': 0.08,
            'conscription_factor': -0.03,
            'army_artillery_defence_factor': 0.03,
        }
    },
    'FRA_munitionnettes_workforce': {
        'name_en': 'Les Munitionnettes',
        'name_pt': 'As Munitionnettes',
        'desc_en': 'Hundreds of thousands of courageous French women take over lathe benches and explosive assembly lines.',
        'desc_pt': 'Centenas de milhares de francesas corajosas assumem tornos e linhas de montagem de explosivos nas fábricas de guerra.',
        'modifier': {
            'industrial_capacity_factory': 0.10,
            'conscription_factor': 0.04,
            'stability_factor': 0.03,
        }
    },
    'FRA_defense_bonds_liquidity': {
        'name_en': 'National Defense Bond Liquidity',
        'name_pt': 'Liquidez dos Bônus de Defesa Nacional',
        'desc_en': 'Popular patriotic loans mobilize household savings to finance wartime purchases without hyperinflation.',
        'desc_pt': 'Empréstimos populares patrióticos mobilizam as economias familiares para financiar compras bélicas sem gerar hiperinflação.',
        'modifier': {
            'consumer_goods_factor': -0.03,
            'production_speed_arms_factory_factor': 0.05,
        }
    },
    'FRA_ww1_rationing': {
        'name_en': 'Fair Wartime Food Supply',
        'name_pt': 'Abastecimento Justo em Tempo de Guerra',
        'desc_en': 'Rationing coupons and municipal bread cards ensure urban workers and soldiers receive adequate sustenance.',
        'desc_pt': 'Cupons de racionamento e cartões municipais garantem sustento alimentar adequado a operários urbanos e soldados.',
        'modifier': {
            'consumer_goods_factor': -0.02,
            'stability_factor': 0.04,
        }
    },
    'FRA_standardised_war_tooling': {
        'name_en': 'Standardized War Tooling',
        'name_pt': 'Padronização do Maquinário Bélico',
        'desc_en': 'Rigorous technical standardization across all armaments factories streamlines production lines and ammunition logistics.',
        'desc_pt': 'Padronização técnica rigorosa em todas as fábricas de armas agiliza as linhas de montagem e a logística de munição.',
        'modifier': {
            'industrial_capacity_factory': 0.06,
            'production_speed_arms_factory_factor': 0.06,
        }
    },
    'FRA_british_coal_imports': {
        'name_en': 'British Maritime Coal Lifeline',
        'name_pt': 'Linha de Carvão Britânica',
        'desc_en': 'Guaranteed shipments of high-grade British coal replace lost production from the occupied Nord coal basins.',
        'desc_pt': 'Remessas garantidas de carvão britânico de alta qualidade substituem a produção perdida das bacias do Norte.',
        'modifier': {
            'industrial_capacity_factory': 0.05,
            'consumer_goods_factor': -0.02,
        }
    },
    'FRA_national_credit_solvency': {
        'name_en': 'Crédit National Solvency',
        'name_pt': 'Solvência do Crédit National',
        'desc_en': 'A dedicated state credit entity coordinates reparations, reconstruction funding, and postwar industrial retooling.',
        'desc_pt': 'Uma entidade estatal dedicada de crédito coordena fundos de reconstrução e reconversão industrial pós-guerra.',
        'modifier': {
            'production_speed_industrial_complex_factor': 0.10,
            'production_speed_infrastructure_factor': 0.10,
            'consumer_goods_factor': -0.02,
        }
    },
    'FRA_supreme_industrial_mobilisation': {
        'name_en': 'Supreme Industrial Mobilization',
        'name_pt': 'Mobilização Industrial Suprema',
        'desc_en': 'Total economic coordination between automotive giants, heavy steelworks, and chemical conglomerates.',
        'desc_pt': 'Coordenação econômica total entre gigantes automobilísticos, siderúrgicas pesadas e conglomerados químicos.',
        'modifier': {
            'industrial_capacity_factory': 0.10,
            'production_speed_arms_factory_factor': 0.08,
            'efficiency_retention_bonus': 0.05,
        }
    },
    'FRA_1914_fiscal_solvency': {
        'name_en': '1914 Fiscal Solvency',
        'name_pt': 'Solvência Fiscal de 1914',
        'desc_en': 'Fiscal reforms passed on the eve of war secure state credit and budgetary stability.',
        'desc_pt': 'Reformas fiscais aprovadas às vésperas da guerra garantem o crédito estatal e a estabilidade orçamentária.',
        'modifier': {
            'consumer_goods_factor': -0.03,
            'production_speed_industrial_complex_factor': 0.05,
            'political_power_gain': 0.10,
        }
    },

    # -------------------------------------------------------------
    # Colonial Wing Ideas
    # -------------------------------------------------------------
    'FRA_colonial_order_aof': {
        'name_en': 'Order of French West Africa',
        'name_pt': 'Ordem da África Ocidental Francesa',
        'desc_en': 'The colonial administration in Dakar ensures civic stability and steady resource extraction across French West Africa.',
        'desc_pt': 'A administração colonial em Dacar assegura estabilidade cívica e extração regular de recursos na AOF.',
        'modifier': {
            'non_core_manpower': 0.02,
            'stability_factor': 0.04,
        }
    },
    'FRA_dakar_atlantic_hub': {
        'name_en': 'Dakar Atlantic Naval Hub',
        'name_pt': 'Polo Naval Atlântico de Dacar',
        'desc_en': 'Deep-water berths and coal bunkering facilities secure maritime lines of communication connecting Europe, South America, and Africa.',
        'desc_pt': 'Atracadouros de águas profundas e depósitos de carvão protegem linhas de navegação entre Europa, América do Sul e África.',
        'modifier': {
            'industrial_capacity_dockyard': 0.05,
            'convoy_escort_efficiency': 0.10,
        }
    },
    'FRA_dakar_niger_logistics': {
        'name_en': 'Dakar-Niger Logistic Corridor',
        'name_pt': 'Corredor Logístico Dacar-Níger',
        'desc_en': 'Extending railway lines into the African interior facilitates rapid dispatch of tropical commodities and volunteers.',
        'desc_pt': 'A extensão de linhas ferroviárias para o interior africano agiliza o envio de mercadorias tropicais e voluntários.',
        'modifier': {
            'supply_consumption_factor': -0.04,
            'production_speed_infrastructure_factor': 0.05,
        }
    },
    'FRA_madagascar_strategic_minerals': {
        'name_en': 'Madagascan Strategic Minerals',
        'name_pt': 'Minerais Estratégicos de Madagascar',
        'desc_en': 'Graphite, mica, and precious metals extracted from the island bolster French high-precision instrumentation.',
        'desc_pt': 'Grafite, mica e metais preciosos extraídos da ilha fortalecem a instrumentação militar francesa de alta precisão.',
        'modifier': {
            'industrial_capacity_factory': 0.04,
            'research_speed_factor': 0.02,
        }
    },
    'FRA_tamatave_port_infrastructure': {
        'name_en': 'Tamatave Harbor Facilities',
        'name_pt': 'Instalações Portuárias de Tamatave',
        'desc_en': 'Modernized piers and cargo cranes safeguard vital Indian Ocean sea lanes.',
        'desc_pt': 'Píeres modernizados e guindastes de carga protegem rotas marítimas vitais no Oceano Índico.',
        'modifier': {
            'industrial_capacity_dockyard': 0.04,
            'naval_speed_factor': 0.03,
        }
    },
    'FRA_pasteur_colonial_hygiene': {
        'name_en': 'Pasteur Overseas Medical Network',
        'name_pt': 'Rede Médica Ultramarina Pasteur',
        'desc_en': 'Inoculation campaigns and tropical disease prevention preserve military garrisons and native populations alike.',
        'desc_pt': 'Campanhas de vacinação e controle de doenças tropicais preservam guarnições militares e populações locais.',
        'modifier': {
            'casualty_trickleback': 0.05,
            'conscription_factor': 0.03,
        }
    },
    'FRA_force_noire_integration': {
        'name_en': 'La Force Noire Integration',
        'name_pt': 'Integração de La Force Noire',
        'desc_en': 'Conceived by General Charles Mangin, colonial infantry units bridge the metropolitan demographic shortfall with bravery.',
        'desc_pt': 'Idealizada pelo General Mangin, a infantaria colonial compensa a escassez demográfica metropolitana com bravura.',
        'modifier': {
            'conscription_factor': 0.08,
            'non_core_manpower': 0.04,
            'stability_factor': -0.02,
        }
    },
    'FRA_nineteenth_corps_african_army': {
        'name_en': '19th Army Corps (Armée d’Afrique)',
        'name_pt': '19º Corpo de Exército (Armée d’Afrique)',
        'desc_en': 'Hardened veterans of Algerian and Tunisian campaigns form the shock vanguard of French expeditionary warfare.',
        'desc_pt': 'Veteranos endurecidos das campanhas na Argélia e Tunísia formam a vanguarda de choque da força expedicionária francesa.',
        'modifier': {
            'army_morale_factor': 0.05,
            'army_attack_factor': 0.04,
        }
    },
    'FRA_tirailleurs_marocains_shock': {
        'name_en': 'Tirailleurs Marocains Shock Cadres',
        'name_pt': 'Quadros de Choque dos Atiradores Marroquinos',
        'desc_en': 'Renowned for ferocious assault capabilities in trench fighting, Moroccan regiments lead frontline counter-offensives.',
        'desc_pt': 'Famosos pela feroz capacidade de assalto nas trincheiras, regimentos marroquinos lideram contra-ofensivas na linha de frente.',
        'modifier': {
            'army_attack_factor': 0.05,
            'army_org_factor': 0.03,
        }
    },
    'FRA_algerian_spahis_cavalry': {
        'name_en': 'Algerian Spahis Reconnaissance',
        'name_pt': 'Reconhecimento dos Spahis Argelinos',
        'desc_en': 'Skilled North African light cavalry excel at rapid flank screening, pursuit, and battlefield scouting.',
        'desc_pt': 'A experiente cavalaria ligeira norte-africana destaca-se no rastreamento de flancos, perseguição e reconhecimento de campo.',
        'modifier': {
            'recon_factor': 0.15,
            'army_speed_factor': 0.04,
        }
    },
    'FRA_tirailleurs_senegalais_valor': {
        'name_en': 'Tirailleurs Sénégalais Tenacity',
        'name_pt': 'Tenacidade dos Atiradores Senegaleses',
        'desc_en': 'Unshakable courage under severe enemy artillery fire earns West African riflemen legendary status.',
        'desc_pt': 'A coragem inabalável sob pesado bombardeio inimigo confere aos atiradores oeste-africanos status lendário.',
        'modifier': {
            'army_defence_factor': 0.05,
            'army_morale_factor': 0.04,
        }
    },
    'FRA_foreign_legion_cadres': {
        'name_en': 'Légion Étrangère Elite Cadres',
        'name_pt': 'Quadros de Elite da Legião Estrangeira',
        'desc_en': 'Foreign volunteers bound by sacred legionary brotherhood defend French colors to the last breath.',
        'desc_pt': 'Voluntários estrangeiros unidos pela irmandade legionária defendem as cores francesas até o último suspiro.',
        'modifier': {
            'army_core_defence_factor': 0.06,
            'army_morale_factor': 0.06,
        }
    },
    'FRA_colonial_logistics_labor': {
        'name_en': 'Colonial Labor & Logistics Corps',
        'name_pt': 'Corpo Colonial de Trabalho e Logística',
        'desc_en': 'Indochinese and North African worker contingents maintain port handling, rail maintenance, and ammunition dumps.',
        'desc_pt': 'Contingentes de trabalhadores indochineses e norte-africanos mantêm portos, ferrovias e depósitos de munição operacionais.',
        'modifier': {
            'production_speed_infrastructure_factor': 0.08,
            'supply_consumption_factor': -0.04,
        }
    },
    'FRA_imperial_blood_solidarity': {
        'name_en': 'Imperial Blood Solidarity',
        'name_pt': 'Solidariedade de Sangue do Império',
        'desc_en': 'Shared sacrifice on the battlefield creates unbreakable ties between the metropole and overseas peoples.',
        'desc_pt': 'O sacrifício compartilhado nos campos de batalha forja laços inquebrantáveis entre a metrópole e os povos ultramarinos.',
        'modifier': {
            'war_support_factor': 0.08,
            'stability_factor': 0.05,
            'non_core_manpower': 0.03,
        }
    },
    'FRA_blaise_diagne_citizenship_reforms': {
        'name_en': 'Blaise Diagne Citizenship Reforms',
        'name_pt': 'Reformas de Cidadania de Blaise Diagne',
        'desc_en': 'Extending full French civic rights to decorated colonial soldiers recognizes supreme service to the Republic.',
        'desc_pt': 'Conceder plenos direitos civis a soldados coloniais condecorados reconhece o supremo serviço prestado à República.',
        'modifier': {
            'stability_factor': 0.06,
            'political_power_gain': 0.10,
            'non_core_manpower': 0.04,
        }
    },
    'FRA_lyautey_moroccan_order': {
        'name_en': 'Lyautey Moroccan Protectorate Order',
        'name_pt': 'Ordem do Protetorado Marroquino de Lyautey',
        'desc_en': 'Respect for local customs combined with modern economic development maintains tranquil stability across Morocco.',
        'desc_pt': 'O respeito aos costumes locais aliado ao desenvolvimento econômico garante estabilidade e tranquilidade no Marrocos.',
        'modifier': {
            'non_core_manpower': 0.04,
            'stability_factor': 0.05,
        }
    },
    'FRA_morocco_treaty_of_fez': {
        'name_en': 'Treaty of Fez Sovereignty',
        'name_pt': 'Soberania do Tratado de Fez',
        'desc_en': 'French protectorate status over Morocco is formally confirmed by international treaty.',
        'desc_pt': 'O estatuto de protetorado francês sobre o Marrocos é formalmente referendado por tratado internacional.',
        'modifier': {
            'political_power_gain': 0.05,
            'stability_factor': 0.04,
        }
    },

    # -------------------------------------------------------------
    # Navy & Aviation Wing Ideas
    # -------------------------------------------------------------
    'FRA_boue_de_lapeyrere_naval_law': {
        'name_en': 'Boué de Lapeyrère Naval Program',
        'name_pt': 'Programa Naval Boué de Lapeyrère',
        'desc_en': 'A deliberate focus on modern dreadnoughts and fleet modernization revitalizes French maritime supremacy.',
        'desc_pt': 'Foco deliberado em encouraçados modernos e renovação da frota revitaliza a supremacia marítima francesa.',
        'modifier': {
            'industrial_capacity_dockyard': 0.08,
            'navy_capital_ship_attack_factor': 0.05,
        }
    },
    'FRA_mediterranean_battlefleet': {
        'name_en': '1ère Armée Navale (Toulon)',
        'name_pt': '1ère Armée Navale (Toulon)',
        'desc_en': 'France concentrates its capital ship strength in the Mediterranean to neutralize Austro-Hungarian and Ottoman threats.',
        'desc_pt': 'A França concentra seus navios de linha no Mediterrâneo para neutralizar ameaças austro-húngaras e otomanas.',
        'modifier': {
            'navy_capital_ship_attack_factor': 0.06,
            'navy_capital_ship_defence_factor': 0.05,
        }
    },
    'FRA_adriatic_naval_blockade': {
        'name_en': 'Otranto Barrage & Adriatic Patrols',
        'name_pt': 'Barragem de Otranto e Patrulhas do Adriático',
        'desc_en': 'Continuous naval patrols bottle up the Austro-Hungarian fleet and protect Allied transports heading for Salonika.',
        'desc_pt': 'Patrulhas contínuas bloqueiam a frota austro-húngara e protegem os comboios aliados com destino a Salônica.',
        'modifier': {
            'convoy_escort_efficiency': 0.12,
            'naval_strike_factor': 0.05,
        }
    },
    'FRA_q_ships_and_coastal_avisos': {
        'name_en': 'Coastal Avisos & Q-Ships',
        'name_pt': 'Avisos Costeiros e Navios-Isca Q-Ships',
        'desc_en': 'Arming civilian vessels with concealed quick-firing guns creates deadly traps for surfaced enemy submarines.',
        'desc_pt': 'Armar embarcações civis com canhões ocultos de tiro rápido cria armadilhas mortais para submarinos inimigos na superfície.',
        'modifier': {
            'sub_detection': 0.15,
            'navy_screen_attack_factor': 0.05,
        }
    },
    'FRA_escorted_maritime_convoys': {
        'name_en': 'Allied Escorted Maritime Convoys',
        'name_pt': 'Comboios Marítimos Escoltados Aliados',
        'desc_en': 'Grouping merchantmen under rigorous naval destroyer escorts sharply reduces losses to unrestricted submarine warfare.',
        'desc_pt': 'Reunir navios mercantes sob rigorosa escolta de contratorpedeiros reduz drasticamente as perdas na guerra submarina.',
        'modifier': {
            'convoy_escort_efficiency': 0.15,
            'naval_speed_factor': 0.04,
        }
    },
    'FRA_mediterranean_dominance': {
        'name_en': 'Mediterranean Naval Dominance',
        'name_pt': 'Domínio Naval do Mediterrâneo',
        'desc_en': 'Complete command of the Mediterranean sea lanes safeguards troop movements from North Africa and the Levant.',
        'desc_pt': 'O controle total das rotas do Mediterrâneo garante a movimentação segura de tropas do Norte da África e Levante.',
        'modifier': {
            'naval_coordination': 0.15,
            'navy_screen_attack_factor': 0.08,
            'navy_capital_ship_defence_factor': 0.06,
        }
    },
    'FRA_pilot_training_corps': {
        'name_en': 'Aeronautique Flight Schools',
        'name_pt': 'Escolas de Voo da Aeronáutica',
        'desc_en': 'Standardized flight curriculums at Pau and Étampes train high-caliber aviators in aerobatics and aerial gunnery.',
        'desc_pt': 'Currículos padronizados de voo em Pau e Étampes formam aviadores de alto calibre em acrobacias e tiro aéreo.',
        'modifier': {
            'air_accidental_factor': -0.15,
            'air_training_xp_gain_factor': 0.10,
        }
    },
    'FRA_aerial_photo_reconnaissance': {
        'name_en': 'Aerial Photographic Reconnaissance',
        'name_pt': 'Reconhecimento Fotográfico Aéreo',
        'desc_en': 'Daily aerial photographic sorties map enemy trench networks and gun emplacements with unmatched accuracy.',
        'desc_pt': 'Sortidas aéreas fotográficas diárias mapeiam as redes de trincheiras e baterias inimigas com precisão sem igual.',
        'modifier': {
            'recon_factor': 0.15,
            'air_superiority_factor': 0.04,
        }
    },
    'FRA_synchronized_vickers_guns': {
        'name_en': 'Deflector Wedges & Synchronizer Gears',
        'name_pt': 'Defletores e Engrenagens Sincronizadoras',
        'desc_en': 'Machineguns firing directly through the propeller arc turn French pursuit planes into lethal dogfighters.',
        'desc_pt': 'Metralhadoras disparando através do arco da hélice transformam os caças franceses em armas letais de combate.',
        'modifier': {
            'air_superiority_efficiency': 0.08,
            'air_agility_factor': 0.06,
        }
    },
    'FRA_spad_fighter_supremacy': {
        'name_en': 'SPAD Fighter Superiority',
        'name_pt': 'Superioridade dos Caças SPAD',
        'desc_en': 'Robust SPAD VII and XIII biplanes powered by Hispano-Suiza V8 engines dominate high-altitude dogfights.',
        'desc_pt': 'Os robustos caças SPAD VII e XIII com motores Hispano-Suiza V8 dominam os combates aéreos em grandes altitudes.',
        'modifier': {
            'air_superiority_factor': 0.08,
            'air_agility_factor': 0.08,
        }
    },
    'FRA_legendary_flying_aces': {
        'name_en': 'Les As de la Chasse (Flying Aces)',
        'name_pt': 'Os Ases da Caça (Les Cigognes)',
        'desc_en': 'Heroes like Guynemer, Fonck, and Nungesser inspire the nation and demoralize enemy aviators.',
        'desc_pt': 'Heróis como Guynemer, Fonck e Nungesser inspiram a nação e desmoralizam os aviadores adversários.',
        'modifier': {
            'air_ace_generation_chance_factor': 0.25,
            'air_superiority_factor': 0.05,
        }
    },
    'FRA_air_ground_tsf_radio_coordination': {
        'name_en': 'Air-Ground Wireless (TSF) Artillery Spotting',
        'name_pt': 'Regulagem Aérea de Artilharia por Rádio TSF',
        'desc_en': 'Airborne wireless telegraphy transmits immediate target corrections to heavy artillery batteries.',
        'desc_pt': 'A telegrafia sem fio aérea transmite correções imediatas de alvos para as baterias de artilharia pesada.',
        'modifier': {
            'army_artillery_attack_factor': 0.06,
            'recon_factor': 0.10,
        }
    },
    'FRA_hispano_suiza_aero_engines': {
        'name_en': 'Hispano-Suiza & Gnome-Rhône Engine Works',
        'name_pt': 'Motores Hispano-Suiza e Gnome-Rhône',
        'desc_en': 'Aluminum-block V8 engines provide superior power-to-weight ratios for French combat aircraft.',
        'desc_pt': 'Motores V8 em bloco de alumínio fornecem superior relação potência-peso para os aviões de combate franceses.',
        'modifier': {
            'industrial_capacity_factory': 0.05,
            'air_maximum_speed_factor': 0.05,
        }
    },
    'FRA_caquot_observation_balloons': {
        'name_en': 'Caquot Aerodynamic Observation Balloons',
        'name_pt': 'Balões Aerodinâmicos Caquot',
        'desc_en': 'Tethered kite balloons designed by Albert Caquot remain stable in high winds, providing continuous artillery spotting.',
        'desc_pt': 'Balões cativos projetados por Albert Caquot permanecem estáveis sob ventos fortes, orientando o fogo de artilharia.',
        'modifier': {
            'max_dig_in': 2,
            'army_artillery_defence_factor': 0.04,
        }
    },
    'FRA_night_interception_patrols': {
        'name_en': 'Night Air Interception Patrols',
        'name_pt': 'Patrulhas de Interceptação Noturna',
        'desc_en': 'Coordinated searchlights, acoustic detectors, and night-fighter patrols intercept enemy Gotha bombing raids.',
        'desc_pt': 'Holofotes coordenados, detectores acústicos e patrulhas noturnas interceptam incursões de bombardeiros inimigos.',
        'modifier': {
            'air_night_penalty': -0.15,
            'air_superiority_factor': 0.04,
        }
    },
    'FRA_colonel_duval_air_division': {
        'name_en': 'Massed Air Division (Colonel Duval)',
        'name_pt': 'Divisão Aérea de Massa (Cel. Duval)',
        'desc_en': 'Concentrating hundreds of bombers and fighters under unified tactical command crushes enemy frontline concentrations.',
        'desc_pt': 'A concentração de centenas de caças e bombardeiros sob comando tático unificado esmaga concentrações inimigas.',
        'modifier': {
            'air_cas_efficiency': 0.10,
            'air_superiority_efficiency': 0.08,
        }
    },
    'FRA_victorious_aero_industry': {
        'name_en': 'Victorious Aeronautical Industry',
        'name_pt': 'Indústria Aeronáutica Vitoriosa',
        'desc_en': 'France produces more combat aircraft and engines than any other nation in the Great War.',
        'desc_pt': 'A França produz mais aeronaves e motores de combate do que qualquer outra nação durante a Grande Guerra.',
        'modifier': {
            'industrial_capacity_factory': 0.08,
            'air_superiority_factor': 0.06,
        }
    },
    'FRA_air_supremacy_spad': {
        'name_en': 'SPAD Air Supremacy',
        'name_pt': 'Supremacia Aérea SPAD',
        'desc_en': 'French pursuit squadrons dominate the Western Front skies.',
        'desc_pt': 'Os esquadrões franceses de caça dominam os céus da Frente Ocidental.',
        'modifier': {
            'air_superiority_efficiency': 0.06,
            'air_agility_factor': 0.08,
        }
    },

    # -------------------------------------------------------------
    # Army Wing Ideas
    # -------------------------------------------------------------
    'FRA_joffre_supreme_staff': {
        'name_en': 'Grand Quartier Général (Joffre Staff)',
        'name_pt': 'Grand Quartier Général (Estado-Maior de Joffre)',
        'desc_en': 'Centralized operational control from GQG coordinates rail mobilizations and strategic troop redeployments.',
        'desc_pt': 'O controle operacional centralizado do GQG coordena mobilizações ferroviárias e remanejamentos estratégicos.',
        'modifier': {
            'planning_speed': 0.15,
            'army_org_factor': 0.04,
        }
    },
    'FRA_offensive_school': {
        'name_en': 'Offensive Doctrine School',
        'name_pt': 'Escola da Ofensiva à Outrance',
        'desc_en': 'Belief in aggressive maneuver and bayonet spirit drives the early French battle doctrine.',
        'desc_pt': 'A crença na manobra agressiva e no espírito da baioneta orienta a doutrina inicial de combate do exército francês.',
        'modifier': {
            'army_attack_factor': 0.06,
            'army_speed_factor': 0.04,
            'army_defence_factor': -0.04,
        }
    },
    'FRA_plan_xvii_concentration': {
        'name_en': 'Plan XVII Concentration',
        'name_pt': 'Concentração do Plano XVII',
        'desc_en': 'Carefully pre-planned railway timetables concentrate five French armies along the Lorraine and Ardennes frontier.',
        'desc_pt': 'Horários ferroviários milimetricamente planejados concentram cinco exércitos franceses ao longo da fronteira.',
        'modifier': {
            'planning_speed': 0.10,
            'max_planning': 0.08,
        }
    },
    'FRA_lessons_of_the_frontiers': {
        'name_en': 'Lessons of the Frontiers',
        'name_pt': 'Lições das Batalhas das Fronteiras',
        'desc_en': 'The bloody repulse of August 1914 shattered blind faith in naked assault, teaching the supremacy of cover and firepower.',
        'desc_pt': 'A sangrenta derrota de agosto de 1914 destruiu a fé cega no ataque descoberto, ensinando a primazia do abrigo e do poder de fogo.',
        'modifier': {
            'army_defence_factor': 0.08,
            'max_dig_in': 3,
            'army_morale_factor': -0.02,
        }
    },
    'FRA_miracle_of_the_marne': {
        'name_en': 'Miracle of the Marne Spirit',
        'name_pt': 'Espírito do Milagre do Marne',
        'desc_en': 'The desperate counter-offensive that saved Paris forged an unbreakable bond of resilience across all ranks.',
        'desc_pt': 'A desesperada contra-ofensiva que salvou Paris forjou um laço inabalável de resiliência em todas as patentes.',
        'modifier': {
            'army_core_defence_factor': 0.10,
            'army_morale_factor': 0.06,
        }
    },
    'FRA_race_to_the_sea_entrenchment': {
        'name_en': 'Continuous Trench Frontline',
        'name_pt': 'Frente Contínua de Trincheiras',
        'desc_en': 'Connecting trenches from Switzerland to the North Sea prevents any further outflanking maneuvers.',
        'desc_pt': 'Ligar trincheiras contínuas da Suíça até o Mar do Norte impede manobras de flanqueamento adicionais.',
        'modifier': {
            'max_dig_in': 4,
            'dig_in_speed_factor': 0.15,
        }
    },
    'FRA_horizon_blue_uniforms_idea': {
        'name_en': 'Bleu Horizon Low-Visibility Uniforms',
        'name_pt': 'Uniformes Bleu Horizon de Baixa Visibilidade',
        'desc_en': 'Replacing bright red trousers with subdued horizon blue blend French infantry into misty European battlegrounds.',
        'desc_pt': 'Substituir as calças vermelhas por azul horizonte discreto camufla a infantaria francesa nas névoas da batalha.',
        'modifier': {
            'army_defence_factor': 0.06,
            'casualty_trickleback': 0.04,
        }
    },
    'FRA_adrian_helmet_protection': {
        'name_en': 'M1915 Adrian Steel Helmet',
        'name_pt': 'Capacete de Aço Adrian M1915',
        'desc_en': 'Stamping millions of steel helmets drastically reduces shrapnel fatalities and head wounds among frontline soldiers.',
        'desc_pt': 'A estampagem de milhões de capacetes de aço reduz drasticamente mortes por estilhaços e ferimentos na cabeça.',
        'modifier': {
            'army_defence_factor': 0.05,
            'casualty_trickleback': 0.05,
        }
    },
    'FRA_ww1_field_fortification': {
        'name_en': 'Deep Concrete Field Fortifications',
        'name_pt': 'Fortificações Profundas de Campanha',
        'desc_en': 'Reinforced concrete pillboxes, deep underground shelters, and multiple barbed wire belts withstand bombardment.',
        'desc_pt': 'Casamatas de concreto armado, abrigos subterrâneos profundos e arames farpados resistem ao bombardeio mais feroz.',
        'modifier': {
            'max_dig_in': 5,
            'dig_in_speed_factor': 0.20,
        }
    },
    'FRA_petain_elastic_defense': {
        'name_en': 'Pétain Elastic Defense in Depth',
        'name_pt': 'Defesa Elástica em Profundidade de Pétain',
        'desc_en': 'Holding frontlines lightly and crushing penetrations with massive artillery and immediate counter-attacks.',
        'desc_pt': 'Manter as primeiras linhas com poucos homens e esmagar penetrações com artilharia massiva e contra-ataques imediatos.',
        'modifier': {
            'army_defence_factor': 0.08,
            'army_org_factor': 0.06,
            'supply_consumption_factor': -0.06,
        }
    },
    'FRA_kaiser_offensive_halted': {
        'name_en': 'Repulse of the Kaiserschlacht',
        'name_pt': 'Rechaço da Kaiserschlacht',
        'desc_en': 'Weathering the German spring stormtroopers through depth and artillery prepares the stage for the final Allied victory.',
        'desc_pt': 'Suportar os ataques de tropas de choque alemãs com profundidade e artilharia abre caminho para a vitória final.',
        'modifier': {
            'army_core_defence_factor': 0.08,
            'army_morale_factor': 0.06,
        }
    },
    'FRA_firepower_doctrine': {
        'name_en': 'Firepower Superiority Doctrine',
        'name_pt': 'Doutrina de Primazia do Poder de Fogo',
        'desc_en': 'Artillery conquers, infantry occupies. Heavy guns pound enemy works relentlessly before any soldier advances.',
        'desc_pt': 'A artilharia conquista, a infantaria ocupa. Canhões pesados pulverizam defesas antes do avanço de qualquer homem.',
        'modifier': {
            'army_artillery_attack_factor': 0.08,
            'army_artillery_defence_factor': 0.06,
        }
    },
    'FRA_balanced_siege_and_field_artillery': {
        'name_en': 'Balanced Field & Heavy Siege Artillery',
        'name_pt': 'Artilharia Mista de Campanha e Cerco Pesado',
        'desc_en': 'Combining quick-firing 75mm guns with 155mm howitzers and 220mm mortars gives French commanders tactical flexibility.',
        'desc_pt': 'Combinar canhões rápidos de 75mm com obuseiros de 155mm e morteiros de 220mm oferece flexibilidade tática incomparável.',
        'modifier': {
            'army_artillery_attack_factor': 0.08,
            'army_attack_factor': 0.04,
        }
    },
    'FRA_railway_super_heavy_artillery': {
        'name_en': 'ALVF Railway Super-Heavy Artillery',
        'name_pt': 'Artilharia Super-Pesada Ferroviária (ALVF)',
        'desc_en': 'Monstrous 320mm and 400mm naval guns mounted on railroad wagons demolish deep enemy concrete fortifications.',
        'desc_pt': 'Monstruosos canhões navais de 320mm e 400mm sobre vagões ferroviários destroem fortificações subterrâneas de concreto.',
        'modifier': {
            'army_artillery_attack_factor': 0.10,
            'breakthrough_factor': 0.05,
        }
    },
    'FRA_somme_artillery_coordination': {
        'name_en': 'Creeping Barrage & Rolling Fire',
        'name_pt': 'Barragem Rolante e Fogo Coordenado',
        'desc_en': 'Timing artillery curtains to march precisely 100 meters ahead of advancing infantry neutralizes machinegun nests.',
        'desc_pt': 'Cronometrar cortinas de artilharia para avançar exatamente 100 metros à frente da infantaria neutraliza ninhos de metralhadoras.',
        'modifier': {
            'army_artillery_attack_factor': 0.06,
            'army_attack_factor': 0.04,
        }
    },
    'FRA_light_machinegun_fireteams': {
        'name_en': 'Chauchat Tactical Fireteams',
        'name_pt': 'Equipes Táticas de Metralhadora Leve Chauchat',
        'desc_en': 'Distributing automatic rifles down to the squad level gives infantry organic marching fire capability.',
        'desc_pt': 'Distribuir fuzis-metralhadoras ao nível de esquadra confere à infantaria capacidade própria de fogo em movimento.',
        'modifier': {
            'army_infantry_attack_factor': 0.06,
            'army_defence_factor': 0.04,
        }
    },
    'FRA_artillerie_speciale_cadres': {
        'name_en': 'Artillerie Spéciale (Tank Corps Cadres)',
        'name_pt': 'Artillerie Spéciale (Quadros Blindados)',
        'desc_en': 'Pioneered by General Estienne, dedicated assault vehicle units train in mechanized breakthrough and trench crossing.',
        'desc_pt': 'Criadas pelo General Estienne, unidades de veículos de assalto treinam penetração mecanizada e cruzamento de trincheiras.',
        'modifier': {
            'army_armor_speed_factor': 0.05,
            'army_armor_attack_factor': 0.08,
        }
    },
    'FRA_renault_ft_revolution': {
        'name_en': 'Renault FT Turreted Tank Concept',
        'name_pt': 'Conceito de Tanque Renault FT',
        'desc_en': 'The revolutionary fully rotating 360-degree turret and rear engine layout defines modern armored warfare.',
        'desc_pt': 'A torre giratória revolucionária em 360 graus e o motor traseiro definem a guerra mecanizada moderna.',
        'modifier': {
            'army_armor_attack_factor': 0.08,
            'breakthrough_factor': 0.06,
        }
    },
    'FRA_mass_swarm_tank_tactics': {
        'name_en': 'Mass Swarm Light Armor Tactics',
        'name_pt': 'Táticas de Enxame de Blindados Ligeiros',
        'desc_en': 'Deploying hundreds of inexpensive, nimble light tanks in tight mutual support overwhelms enemy defensive belts.',
        'desc_pt': 'Empregar centenas de blindados ligeiros em estreito apoio mútuo sobrecarrega os cinturões defensivos inimigos.',
        'modifier': {
            'army_armor_attack_factor': 0.08,
            'army_armor_speed_factor': 0.05,
        }
    },
    'FRA_fully_motorised_logistics': {
        'name_en': 'Motorized Supply Columns',
        'name_pt': 'Colunas Motorizadas de Suprimento',
        'desc_en': 'Replacing horse carts with fleets of Renault and Berliet trucks accelerates tactical redeployments.',
        'desc_pt': 'Substituir carroças de tração animal por caminhões Renault e Berliet acelera os deslocamentos táticos.',
        'modifier': {
            'supply_consumption_factor': -0.08,
            'army_speed_factor': 0.05,
        }
    },

    # -------------------------------------------------------------
    # Diplomacy Wing Ideas
    # -------------------------------------------------------------
    'FRA_franco_russian_sacred_alliance': {
        'name_en': 'Franco-Russian Sacred Alliance',
        'name_pt': 'Aliança Sagrada Franco-Russa',
        'desc_en': 'The cornerstone of French security: binding mutual defense guarantees that force Germany to fight on two fronts.',
        'desc_pt': 'A pedra angular da segurança francesa: garantias mútuas de defesa que forçam a Alemanha a lutar em duas frentes.',
        'modifier': {
            'war_support_factor': 0.08,
            'stability_factor': 0.05,
            'planning_speed': 0.05,
        }
    },
    'FRA_eastern_front_containment': {
        'name_en': 'Russian Pressure on the East',
        'name_pt': 'Pressão Russa no Leste',
        'desc_en': 'Russian offensives in East Prussia and Galicia pin down vast German corps away from Paris.',
        'desc_pt': 'Ofensivas russas na Prússia Oriental e Galícia prendem vastos corpos de exército alemães longe de Paris.',
        'modifier': {
            'army_core_defence_factor': 0.06,
            'war_support_factor': 0.04,
        }
    },
    'FRA_entente_cordiale_brotherhood': {
        'name_en': 'Entente Cordiale Brotherhood',
        'name_pt': 'Irmandade da Entente Cordiale',
        'desc_en': 'Centuries of Anglo-French rivalry give way to staunch military cooperation against continental hegemony.',
        'desc_pt': 'Séculos de rivalidade anglo-francesa dão lugar a cooperação militar resoluta contra a hegemonia continental.',
        'modifier': {
            'trade_laws_cost_factor': -0.10,
            'naval_coordination': 0.10,
            'stability_factor': 0.04,
        }
    },
    'FRA_bef_channel_ports_coordination': {
        'name_en': 'BEF Channel Flank Coordination',
        'name_pt': 'Coordenação do Flanco do Canal com a BEF',
        'desc_en': 'Coordinated defense of Dunkirk, Calais, and Boulogne ensures unobstructed British reinforcements into northern France.',
        'desc_pt': 'A defesa coordenada de Dunquerque, Calais e Bolonha garante o fluxo livre de reforços britânicos ao norte da França.',
        'modifier': {
            'supply_consumption_factor': -0.05,
            'army_org_factor': 0.04,
        }
    },
    'FRA_treaty_of_london_1839_guarantor': {
        'name_en': '1839 Treaty of London Guarantor',
        'name_pt': 'Garantidor do Tratado de Londres de 1839',
        'desc_en': 'France stands unconditionally behind Belgian neutrality and sovereignty against imperial aggression.',
        'desc_pt': 'A França posiciona-se incondicionalmente em favor da neutralidade e soberania belga contra a agressão imperial.',
        'modifier': {
            'war_support_factor': 0.06,
            'political_power_gain': 0.05,
        }
    },
    'FRA_joint_liaison_missions': {
        'name_en': 'Balkan Allied Military Liaison',
        'name_pt': 'Ligação Militar Aliada nos Bálcãs',
        'desc_en': 'French advisory missions in Serbia and Romania coordinate supplies and counter-offensives across southeastern Europe.',
        'desc_pt': 'Missões francesas de assessoria na Sérvia e Romênia coordenam suprimentos e contra-ofensivas no sudeste europeu.',
        'modifier': {
            'planning_speed': 0.08,
            'war_support_factor': 0.04,
        }
    },
    'FRA_ww1_salonika_transport': {
        'name_en': 'Armée d’Orient (Salonika Lifeline)',
        'name_pt': 'Armée d’Orient (Linha de Suprimento de Salônica)',
        'desc_en': 'Specialized transport convoys maintain the multinational allied front in northern Greece and the Balkans.',
        'desc_pt': 'Comboios especializados de transporte mantêm a frente aliada multinacional no norte da Grécia e Bálcãs.',
        'modifier': {
            'convoy_escort_efficiency': 0.10,
            'army_morale_factor': 0.04,
        }
    },
    'FRA_joint_franco_american_staff': {
        'name_en': 'Franco-American Combined Staff',
        'name_pt': 'Estado-Maior Combinado Franco-Americano',
        'desc_en': 'French instructors train arriving American divisions in modern artillery spotting, gas defense, and trench tactics.',
        'desc_pt': 'Instrutores franceses treinam divisões americanas recém-chegadas em observação de artilharia, defesa química e trincheiras.',
        'modifier': {
            'planning_speed': 0.10,
            'army_org_factor': 0.05,
        }
    },
    'FRA_american_aef_arrival': {
        'name_en': 'Arrival of the American AEF',
        'name_pt': 'Chegada da AEF Americana',
        'desc_en': 'General Pershing’s doughboys arrive in vast numbers, turning the strategic manpower balance irreversibly in the Allies’ favor.',
        'desc_pt': 'Os soldados do General Pershing chegam aos milhões, revertendo o equilíbrio estratégico de efetivos em favor dos Aliados.',
        'modifier': {
            'war_support_factor': 0.12,
            'army_morale_factor': 0.08,
            'consumer_goods_factor': -0.02,
        }
    },
    'FRA_supreme_allied_command': {
        'name_en': 'Supreme Allied Command (Foch)',
        'name_pt': 'Comando Supremo Aliado (Foch)',
        'desc_en': 'Marshal Ferdinand Foch directs all British, American, and French armies under a unified operational strategy.',
        'desc_pt': 'O Marechal Ferdinand Foch dirige todos os exércitos britânicos, americanos e franceses sob estratégia operacional unificada.',
        'modifier': {
            'planning_speed': 0.15,
            'max_planning': 0.10,
            'army_org_factor': 0.05,
        }
    },
    'FRA_alsace_lorraine_reclaimed': {
        'name_en': 'Alsace-Lorraine Reclaimed',
        'name_pt': 'Alsácia-Lorena Reconquistada',
        'desc_en': 'The lost provinces return to the Republic. The long national mourning is over, and French honor is vindicated.',
        'desc_pt': 'As províncias perdidas retornam à República. O longo luto nacional chega ao fim e a honra francesa é resgatada.',
        'modifier': {
            'stability_factor': 0.15,
            'war_support_factor': 0.10,
            'political_power_gain': 0.20,
        }
    },

    # -------------------------------------------------------------
    # Bounded Operations / Temporary Mission Ideas (Strict limits)
    # -------------------------------------------------------------
    'FRA_verdun_resilience': {
        'name_en': 'Verdun Fortress Defense (Active Surge)',
        'name_pt': 'Defesa da Fortaleza de Verdun (Surto Ativo)',
        'desc_en': 'Temporary bounded combat surge: heroic resilience at Fort Douaumont and Vaux. Lasts strictly during the crisis.',
        'desc_pt': 'Surto temporário de combate delimitado: resiliência heroica em Fort Douaumont e Vaux. Dura estritamente durante a crise.',
        'modifier': {
            'army_core_defence_factor': 0.12,
            'army_morale_factor': 0.08,
            'dig_in_speed_factor': 0.15,
        }
    },
    'FRA_nivelle_offensive_surge': {
        'name_en': 'Chemin des Dames Rupture Attempt',
        'name_pt': 'Tentativa de Ruptura de Chemin des Dames',
        'desc_en': 'Temporary bounded assault bonus: massive artillery preparation across the Aisne. Expires quickly with severe exhaustion if prolonged.',
        'desc_pt': 'Bônus de assalto temporário: massiva preparação de artilharia pelo Aisne. Expira rapidamente com severa exaustão se prolongado.',
        'modifier': {
            'army_attack_factor': 0.08,
            'breakthrough_factor': 0.10,
            'army_org_factor': -0.05,
        }
    },
    'FRA_cent_jours_combined_arms': {
        'name_en': 'Cent Jours Combined Arms Surge',
        'name_pt': 'Ofensiva dos Cem Dias em Armas Combinadas',
        'desc_en': 'Bounded final offensive: synchronized tanks, creeping barrages, and aircraft breaking the Hindenburg Line.',
        'desc_pt': 'Ofensiva final delimitada: blindados sincronizados, barragens móveis e aviação rompendo a Linha Hindenburg.',
        'modifier': {
            'army_attack_factor': 0.10,
            'breakthrough_factor': 0.12,
            'army_artillery_attack_factor': 0.08,
        }
    },
    'FRA_la_voie_sacree_convoy': {
        'name_en': 'La Voie Sacrée Logistics Pipeline',
        'name_pt': 'Linha Logística La Voie Sacrée',
        'desc_en': 'Bar-le-Duc to Verdun road kept open 24/7 by thousands of trucks and stone-spreading territorial troops.',
        'desc_pt': 'A estrada de Bar-le-Duc a Verdun mantida aberta 24h por milhares de caminhões e tropas territoriais que espalham cascalho.',
        'modifier': {
            'supply_consumption_factor': -0.15,
            'land_reinforce_rate': 0.15,
            'army_core_defence_factor': 0.05,
        }
    },
    'FRA_ww1_division_rotation': {
        'name_en': 'Noria Division Rotation System',
        'name_pt': 'Sistema Noria de Rotação de Divisões',
        'desc_en': 'Regularly rotating frontline units prevents morale collapse and maintains high unit cohesion.',
        'desc_pt': 'Rotacionar unidades de primeira linha regularmente evita o colapso do moral e mantém alta coesão das tropas.',
        'modifier': {
            'army_morale_factor': 0.08,
            'army_org_factor': 0.05,
        }
    },
    'FRA_trench_soup_and_wine_rations': {
        'name_en': 'Improved Poilu Rations (Pinard & Warm Soup)',
        'name_pt': 'Rações Melhoradas dos Poilus (Pinard e Sopa Quente)',
        'desc_en': 'Providing hot meals and regular pinard wine rations directly to frontline trenches raises morale.',
        'desc_pt': 'Fornecer refeições quentes e rações regulares de vinho pinard diretamente nas trincheiras eleva o ânimo da tropa.',
        'modifier': {
            'army_morale_factor': 0.06,
            'army_defence_factor': 0.03,
        }
    },
}

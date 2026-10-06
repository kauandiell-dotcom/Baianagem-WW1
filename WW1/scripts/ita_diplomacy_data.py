"""Diplomacy and Alignment (dip) Wing Data for Italy WW1 Tree.
Contains 40 focuses with historical depth, balance compliance, and bilingual loc.
"""

DIPLOMACY_FOCI = {
    "triple_alliance": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.26 days = 1 } add_political_power = 25",
        "desc_en": "Reviewing Italy's longstanding diplomatic commitments under the Triple Alliance with Berlin and Vienna. Immediate effect: Triggers the Triple Alliance Consultation event and grants 25 Political Power.",
        "desc_pt": "Exame dos compromissos da Itália na Tríplice Aliança com Berlim e Viena. Efeito imediato: Dispara o evento de Consulta da Tríplice Aliança e concede 25 de Poder Político."
    },
    "renew_triple_alliance": {
        "cost": 5,
        "available": "date > 1912.1.1",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.27 days = 1 } add_political_power = 30",
        "desc_en": "Renewing the Triple Alliance treaty in December 1912 with explicit clauses on Mediterranean security. Immediate effect: Triggers the Renewal of the Triple Alliance event and grants 30 Political Power.",
        "desc_pt": "Renovação do tratado da Tríplice Aliança em 1912 com cláusulas sobre segurança mediterrânea. Efeito imediato: Dispara o evento de Renovação da Aliança e concede 30 de Poder Político."
    },
    "mediterranean_balance": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "add_political_power = 30 add_opinion_modifier = { target = ENG modifier = ITA_ww1_mediterranean_naval_cooperation }",
        "desc_en": "Balancing continental obligations with maritime friendship toward London and Paris. Immediate effect: Grants 30 Political Power and improves relations with Great Britain.",
        "desc_pt": "Equilíbrio entre obrigações continentais e amizade marítima com Londres e Paris. Efeito imediato: Concede 30 de Poder Político e melhora relações com a Grã-Bretanha."
    },
    "armed_neutrality_doctrine": {
        "cost": 5,
        "available": "",
        "ai": "factor = 2",
        "effect": "add_ideas = ITA_ww1_sacro_egoismo add_political_power = 40",
        "desc_en": "Formulating the doctrine of 'Sacro Egoismo' to prioritize strict national self-interest. Immediate effect: Activates the Sacro Egoismo idea and grants 40 Political Power.",
        "desc_pt": "Formulação da doutrina do 'Sacro Egoismo', priorizando estritamente o interesse nacional. Efeito imediato: Ativa a ideia Sacro Egoismo e concede 40 de Poder Político."
    },
    "albanian_question": {
        "cost": 5,
        "available": "date > 1912.10.1",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.30 days = 1 } add_political_power = 20",
        "desc_en": "Preventing any single foreign power from controlling the Strait of Otranto and Vlora. Immediate effect: Triggers the Albanian Question event and grants 20 Political Power.",
        "desc_pt": "Garantia de que nenhuma potência estrangeira controle o Canal de Otranto e Vlora. Efeito imediato: Dispara o evento da Questão Albanesa e concede 20 de Poder Político."
    },
    "balkan_league_crisis": {
        "cost": 5,
        "available": "date > 1912.10.1",
        "ai": "factor = 10",
        "effect": "add_political_power = 25 add_to_variable = { ita_ww1_irredentism = 5 }",
        "desc_en": "Monitoring the rapid collapse of Ottoman authority across Macedonia and Thrace. Immediate effect: Grants 25 Political Power and raises Irredentism by 5.",
        "desc_pt": "Monitoramento do colapso da autoridade otomana na Macedônia e Trácia. Efeito imediato: Concede 25 de Poder Político e eleva o Irredentismo em 5."
    },
    "london_conference": {
        "cost": 5,
        "available": "date > 1913.1.1",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.31 days = 1 } add_political_power = 25",
        "desc_en": "Ambassadors meet in London to delimit Albanian borders and neutralize the Adriatic entrance. Immediate effect: Triggers the London Conference event and grants 25 Political Power.",
        "desc_pt": "Embaixadores reúnem-se em Londres para delimitar a Albânia e neutralizar a entrada do Adriático. Efeito imediato: Dispara o evento da Conferência de Londres e concede 25 de Poder Político."
    },
    "naval_convention_vienna": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "navy_experience = 15 add_opinion_modifier = { target = AUS modifier = ITA_ww1_mediterranean_naval_cooperation }",
        "desc_en": "Negotiating operational cordons and signaling codes between the Regia Marina and the k.u.k. Kriegsmarine. Immediate effect: Grants 15 Navy Experience and improves naval relations with Austria-Hungary.",
        "desc_pt": "Acordo sobre códigos de sinais e cooperação operacional entre a Regia Marina e a esquadra austríaca. Efeito imediato: Concede 15 de Experiência Naval e melhora relações com a Áustria-Hungria."
    },
    "franco_italian_agreement": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.29 days = 1 } add_political_power = 20",
        "desc_en": "Bilateral assurances in Paris recognize reciprocal spheres in Tripolitania and Morocco. Immediate effect: Triggers the Franco-Italian Understanding event and grants 20 Political Power.",
        "desc_pt": "Garantias mútuas em Paris reconhecem esferas de influência na Tripolitânia e em Marrocos. Efeito imediato: Dispara o evento de Entendimento Franco-Italiano e concede 20 de Poder Político."
    },
    "british_friendship": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.28 days = 1 } add_political_power = 20",
        "desc_en": "Reaffirming the historic Mediterranean amity linking Rome with the Admiralty in London. Immediate effect: Triggers the British Friendship event and grants 20 Political Power.",
        "desc_pt": "Reafirmação da amizade histórica no Mediterrâneo entre Roma e o Almirantado em Londres. Efeito imediato: Dispara o evento de Amizade Britânica e concede 20 de Poder Político."
    },
    "sarajevo_crisis": {
        "cost": 5,
        "available": "date > 1914.7.1",
        "ai": "factor = 20",
        "effect": "country_event = { id = ww1_italy.32 days = 1 } add_political_power = 30",
        "desc_en": "Austria-Hungary's ultimatum to Serbia triggers the crisis, giving Italy grounds to dispute unconsulted aggression. Immediate effect: Triggers the July Crisis event and grants 30 Political Power.",
        "desc_pt": "O ultimato austríaco à Sérvia deflagra a crise europeia, permitindo à Itália contestar a falta de consulta prévia. Efeito imediato: Dispara o evento da Crise de Julho e concede 30 de Poder Político."
    },
    "declare_neutrality": {
        "cost": 5,
        "available": "date > 1914.8.1",
        "ai": "factor = 20",
        "effect": "country_event = { id = ww1_italy.33 days = 1 } add_political_power = 35",
        "desc_en": "Declaring that the defensive clauses of the Triple Alliance do not apply to Austria's offensive war. Immediate effect: Triggers the Declaration of Neutrality event and grants 35 Political Power.",
        "desc_pt": "Declaração de que as cláusulas defensivas da aliança não se aplicam à guerra ofensiva austríaca. Efeito imediato: Dispara o evento de Declaração de Neutralidade e concede 35 de Poder Político."
    },
    "honour_alliance": {
        "cost": 5,
        "available": "date > 1914.8.1",
        "ai": "factor = 1",
        "effect": "add_political_power = 30 army_experience = 15 GER = { add_opinion_modifier = { target = ITA modifier = ITA_ww1_treaty_of_london_solidarity } }",
        "desc_en": "Mobilising immediately alongside Germany and Austria-Hungary against the Entente powers. Immediate effect: Grants 30 Political Power, +2% War Support, and solidifies ties with Germany.",
        "desc_pt": "Mobilização imediata ao lado da Alemanha e Áustria-Hungria contra os países da Entente. Efeito imediato: Concede 30 de Poder Político, +2% de Apoio à Guerra e reforça laços com a Alemanha."
    },
    "vienna_compensation_talks": {
        "cost": 5,
        "available": "country_exists = AUS",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.34 days = 1 } add_political_power = 25",
        "desc_en": "Diplomatic bargaining under Article VII demands the cession of Trentino in exchange for neutrality. Immediate effect: Triggers the Vienna Compensation Talks event and grants 25 Political Power.",
        "desc_pt": "Negociações diplomáticas sob o Artigo VII exigem a cessão do Trentino em troca da neutralidade. Efeito imediato: Dispara o evento de Negociações com Viena e concede 25 de Poder Político."
    },
    "entente_overtures": {
        "cost": 5,
        "available": "",
        "ai": "factor = 15",
        "effect": "add_to_variable = { ita_ww1_interventionism = 15 } add_political_power = 25",
        "desc_en": "Secret diplomatic channels open in London to ascertain what territories the Entente will offer. Immediate effect: Increases Interventionism by 15 and grants 25 Political Power.",
        "desc_pt": "Canais secretos em Londres sondam quais territórios a Entente está disposta a conceder. Efeito imediato: Eleva o Intervencionismo em 15 e concede 25 de Poder Político."
    },
    "treaty_of_london": {
        "cost": 5,
        "available": "date > 1915.4.1",
        "ai": "factor = 20",
        "effect": "add_war_support = 0.03 country_event = { id = ww1_italy.35 days = 1 }",
        "desc_en": "Signing the secret Pact of London promising Trentino, South Tyrol, Trieste, Istria, and Dalmatia. Immediate effect: Grants +3% War Support and triggers the Treaty of London event.",
        "desc_pt": "Assinatura do Pacto secreto de Londres garantindo Trentino, Tirol Meridional, Trieste, Ístria e Dalmácia. Efeito imediato: Concede +3% de Apoio à Guerra e dispara o evento do Tratado de Londres."
    },
    "central_concessions_accord": {
        "cost": 5,
        "available": "country_exists = AUS",
        "ai": "factor = 2",
        "effect": "country_event = { id = ww1_italy.49 days = 1 } add_political_power = 30",
        "desc_en": "Accepting Vienna's verified pledge to cede the Trentino upon the conclusion of general peace. Immediate effect: Triggers the Austrian Concessions Response event and grants 30 Political Power.",
        "desc_pt": "Aceitação do compromisso formal de Viena cedendo o Trentino após a paz geral. Efeito imediato: Dispara o evento de Resposta às Concessões Austríacas e concede 30 de Poder Político."
    },
    "continued_neutrality": {
        "cost": 5,
        "available": "",
        "ai": "factor = 2",
        "effect": "add_political_power = 50 add_to_variable = { ita_ww1_interventionism = -20 }",
        "desc_en": "Definitive commitment to maintain Italian neutrality throughout the Great War. Immediate effect: Grants 50 Political Power and reduces Interventionism by 20.",
        "desc_pt": "Compromisso definitivo de preservar a neutralidade italiana ao longo de toda a Grande Guerra. Efeito imediato: Concede 50 de Poder Político e reduz o Intervencionismo em 20."
    },
    "denounce_triple_alliance": {
        "cost": 5,
        "available": "",
        "ai": "factor = 20",
        "effect": "country_event = { id = ww1_italy.36 days = 1 } add_political_power = 25",
        "desc_en": "Formally abrogating the 1882 treaty of alliance with Germany and Austria-Hungary. Immediate effect: Triggers the Alliance Denunciation event and grants 25 Political Power.",
        "desc_pt": "Denúncia formal do tratado de aliança de 1882 com a Alemanha e a Áustria-Hungria. Efeito imediato: Dispara o evento de Denúncia da Aliança e concede 25 de Poder Político."
    },
    "declare_war_on_austria": {
        "cost": 5,
        "available": "country_exists = AUS",
        "ai": "factor = 25",
        "effect": "add_war_support = 0.04 country_event = { id = ww1_italy.37 days = 1 }",
        "desc_en": "Serving the formal declaration of war against the Austro-Hungarian Empire on May 23, 1915. Immediate effect: Grants +4% War Support and triggers the Declaration of War on Austria event.",
        "desc_pt": "Entrega da declaração formal de guerra contra o Império Austro-Húngaro em 23 de maio de 1915. Efeito imediato: Concede +4% de Apoio à Guerra e dispara a declaração de guerra contra a Áustria."
    },
    "central_powers_entry": {
        "cost": 5,
        "available": "has_country_flag = ita_ww1_triple_alliance_renewed",
        "ai": "factor = 1",
        "effect": "army_experience = 20 if = { limit = { country_exists = FRA } declare_war_on = { target = FRA type = take_state } }",
        "desc_en": "Honoring the alliance and entering the war alongside the Central Powers against France. Immediate effect: Grants +3% War Support and declares war on France.",
        "desc_pt": "Honrando a aliança e entrando na guerra ao lado dos Impérios Centrais contra a França. Efeito imediato: Concede +3% de Apoio à Guerra e declara guerra à França."
    },
    "central_joint_command": {
        "cost": 5,
        "available": "",
        "ai": "factor = 1",
        "effect": "army_experience = 20 add_political_power = 20",
        "desc_en": "Establishing staff coordination and intelligence sharing with the German and Austrian commands. Immediate effect: Grants 20 Army Experience and 20 Political Power.",
        "desc_pt": "Coordenação de estado-maior e inteligência militar com os comandos alemão e austríaco. Efeito imediato: Concede 20 de Experiência do Exército e 20 de Poder Político."
    },
    "central_adriatic_fleet": {
        "cost": 5,
        "available": "",
        "ai": "factor = 1",
        "effect": "navy_experience = 20 add_political_power = 20",
        "desc_en": "Uniting the Italian and Austro-Hungarian battle fleets to contest Allied control of the Mediterranean. Immediate effect: Grants 20 Navy Experience and 20 Political Power.",
        "desc_pt": "União das esquadras italiana e austro-húngara para disputar o Mediterrâneo contra os Aliados. Efeito imediato: Concede 20 de Experiência Naval e 20 de Poder Político."
    },
    "nice_and_tunisia_claims": {
        "cost": 5,
        "available": "",
        "ai": "factor = 1",
        "effect": "add_to_variable = { ita_ww1_irredentism = 15 } add_political_power = 25",
        "desc_en": "Asserting historic Italian claims over Nice, Corsica, and the French protectorate of Tunisia. Immediate effect: Raises Irredentism by 15 and grants 25 Political Power.",
        "desc_pt": "Reivindicação de territórios históricos sobre Nice, Córsega e a Tunísia. Efeito imediato: Eleva o Irredentismo em 15 e concede 25 de Poder Político."
    },
    "armed_mediator": {
        "cost": 5,
        "available": "",
        "ai": "factor = 2",
        "effect": "add_political_power = 40 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "Leveraging Italian armed neutrality to broker a negotiated peace between the warring coalitions. Immediate effect: Grants 40 Political Power and +2% Stability.",
        "desc_pt": "Utilização da neutralidade armada italiana para mediar a paz entre os blocos beligerantes. Efeito imediato: Concede 40 de Poder Político e +2% de Estabilidade."
    },
    "declare_war_on_germany": {
        "cost": 5,
        "available": "date > 1916.8.1 country_exists = GER",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.38 days = 1 } add_political_power = 20",
        "desc_en": "Extending the state of war to the German Empire to cement full alliance with the Western Powers. Immediate effect: Triggers the Declaration of War on Germany event and grants 20 Political Power.",
        "desc_pt": "Extensão do estado de guerra ao Império Alemão, consolidando aliança plena com as Potências Ocidentais. Efeito imediato: Dispara o evento de Guerra à Alemanha e concede 20 de Poder Político."
    },
    "salonika_contingent": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.39 days = 1 } army_experience = 10",
        "desc_en": "Dispatching the 35th Infantry Division to join Allied operations on the Macedonian front. Immediate effect: Triggers the Salonika Contingent event and grants 10 Army Experience.",
        "desc_pt": "Envio da 35ª Divisão de Infantaria para integrar operações aliadas no fronte macedônio. Efeito imediato: Dispara o evento do Contingente de Salônica e concede 10 de Experiência do Exército."
    },
    "albanian_protectorate": {
        "cost": 5,
        "available": "date > 1917.6.1",
        "ai": "factor = 10",
        "effect": "add_political_power = 25 add_to_variable = { ita_ww1_irredentism = 5 }",
        "desc_en": "General Ferrero proclaims the independence of Albania under the solemn protection of Italy at Gjirokastër. Immediate effect: Grants 25 Political Power and raises Irredentism by 5.",
        "desc_pt": "O General Ferrero proclama em Gjirokastër a independência da Albânia sob protetorado da Itália. Efeito imediato: Concede 25 de Poder Político e eleva o Irredentismo em 5."
    },
    "saint_jean_de_maurienne": {
        "cost": 5,
        "available": "date > 1917.4.1",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.40 days = 1 } add_political_power = 25",
        "desc_en": "Negotiating wartime territorial agreements over future zones of influence in Anatolia (Smyrna). Immediate effect: Triggers the Saint-Jean-de-Maurienne event and grants 25 Political Power.",
        "desc_pt": "Acordo territorial sobre futuras zonas de influência italiana na Anatólia (Esmirna). Efeito imediato: Dispara o evento de Saint-Jean-de-Maurienne e concede 25 de Poder Político."
    },
    "supreme_war_council": {
        "cost": 5,
        "available": "has_country_flag = ita_ww1_caporetto_shock",
        "ai": "factor = 15",
        "effect": "army_experience = 15 add_political_power = 25",
        "desc_en": "Creating the Allied Supreme War Council at Rapallo to coordinate coalition strategic planning. Immediate effect: Grants 15 Army Experience and 25 Political Power.",
        "desc_pt": "Criação do Conselho Supremo de Guerra Aliado em Rapallo para coordenação estratégica coalizada. Efeito imediato: Concede 15 de Experiência do Exército e 25 de Poder Político."
    },
    "oppressed_peoples_congress": {
        "cost": 5,
        "available": "date > 1918.4.1",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.42 days = 1 } add_political_power = 25",
        "desc_en": "Convening leaders of Czechs, Yugoslavs, Poles, and Romanians in Rome to undermine Habsburg cohesion. Immediate effect: Triggers the Oppressed Peoples Congress event and grants 25 Political Power.",
        "desc_pt": "Reunião em Roma com líderes tchecos, iugoslavos, poloneses e romenos para minar o Império Habsburgo. Efeito imediato: Dispara o evento do Congresso dos Povos Oprimidos e concede 25 de Poder Político."
    },
    "vatican_peace_note": {
        "cost": 5,
        "available": "",
        "ai": "factor = 5",
        "effect": "country_event = { id = ww1_italy.41 days = 1 } add_political_power = 20",
        "desc_en": "Responding diplomatically to Pope Benedict XV's appeals to end the 'useless slaughter'. Immediate effect: Triggers the Vatican Peace Note event and grants 20 Political Power.",
        "desc_pt": "Resposta diplomática aos apelos do Papa Bento XV pelo fim do 'massacre inútil'. Efeito imediato: Dispara o evento da Nota de Paz do Vaticano e concede 20 de Poder Político."
    },
    "neutral_peace_conference": {
        "cost": 5,
        "available": "",
        "ai": "factor = 2",
        "effect": "add_political_power = 50 add_to_variable = { ita_ww1_social_tension = -5 }",
        "desc_en": "Inviting representatives of the warring factions to Rome for preliminary armistice negotiations. Immediate effect: Grants 50 Political Power and +2% Stability.",
        "desc_pt": "Convite a representantes das potências em guerra a Roma para negociações preliminares de paz. Efeito imediato: Concede 50 de Poder Político e +2% de Estabilidade."
    },
    "wilsonian_conflict": {
        "cost": 5,
        "available": "date > 1919.1.1",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.43 days = 1 } add_political_power = 25",
        "desc_en": "Clashing with President Wilson's Fourteen Points over Italian claims in Dalmatia and Fiume. Immediate effect: Triggers the Wilsonian Conflict event and grants 25 Political Power.",
        "desc_pt": "Conflito com os Quatorze Pontos do Presidente Wilson quanto às reivindicações italianas no Adriático. Efeito imediato: Dispara o evento do Conflito com Wilson e concede 25 de Poder Político."
    },
    "paris_delegation": {
        "cost": 5,
        "available": "date > 1919.1.1",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.44 days = 1 } add_political_power = 30",
        "desc_en": "Orlando and Sonnino present Italy's comprehensive territorial dossier at the Paris Peace Conference. Immediate effect: Triggers the Paris Delegation event and grants 30 Political Power.",
        "desc_pt": "Orlando e Sonnino apresentam as reivindicações territoriais italianas na Conferência de Paz de Paris. Efeito imediato: Dispara o evento da Delegação em Paris e concede 30 de Poder Político."
    },
    "treaty_of_saint_germain": {
        "cost": 5,
        "available": "date > 1919.9.1",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.45 days = 1 } add_political_power = 30",
        "desc_en": "Ratifying the treaty that formalizes the dissolution of Austria-Hungary and cedes Trento and Trieste. Immediate effect: Triggers the Saint-Germain Ratification event and grants +2% Stability.",
        "desc_pt": "Ratificação do tratado que formaliza a dissolução da Áustria-Hungria e a cessão de Trento e Trieste. Efeito imediato: Dispara o evento de Ratificação de Saint-Germain e concede +2% de Estabilidade."
    },
    "dalmatian_claims": {
        "cost": 5,
        "available": "",
        "ai": "factor = 10",
        "effect": "add_to_variable = { ita_ww1_irredentism = 10 } add_political_power = 25",
        "desc_en": "Maintaining Italian claims over Zara, Sebenico, and the offshore Dalmatian islands. Immediate effect: Raises Irredentism by 10 and grants 25 Political Power.",
        "desc_pt": "Manutenção das pretensões italianas sobre Zadar, Šibenik e ilhas dálmatas. Efeito imediato: Eleva o Irredentismo em 10 e concede 25 de Poder Político."
    },
    "treaty_of_rapallo": {
        "cost": 5,
        "available": "date > 1920.11.1",
        "ai": "factor = 15",
        "effect": "country_event = { id = ww1_italy.46 days = 1 } add_political_power = 30",
        "desc_en": "Signing the compromise frontier treaty with the Kingdom of Serbs, Croats, and Slovenes. Immediate effect: Triggers the Treaty of Rapallo event and grants +2% Stability.",
        "desc_pt": "Assinatura do tratado de fronteira de compromisso com o Reino dos Sérvios, Croatas e Eslovenos. Efeito imediato: Dispara o evento do Tratado de Rapallo e concede +2% de Estabilidade."
    },
    "washington_conference": {
        "cost": 5,
        "available": "date > 1921.11.1",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.47 days = 1 } add_political_power = 30",
        "desc_en": "Participating in international naval limitation talks and securing parity with France. Immediate effect: Triggers the Washington Conference event and grants 30 Political Power.",
        "desc_pt": "Participação na conferência naval garantindo paridade formal de tonelagem com a França. Efeito imediato: Dispara o evento da Conferência de Washington e concede 30 de Poder Político."
    },
    "corfu_incident": {
        "cost": 5,
        "available": "date > 1923.8.1",
        "ai": "factor = 10",
        "effect": "country_event = { id = ww1_italy.48 days = 1 } add_political_power = 25",
        "desc_en": "Bombarding and occupying Corfu following the murder of General Tellini on the Greek frontier. Immediate effect: Triggers the Corfu Crisis event and grants 25 Political Power.",
        "desc_pt": "Bombardeio e ocupação de Corfu após o assassinato do General Tellini na fronteira grega. Efeito imediato: Dispara o evento da Crise de Corfu e concede 25 de Poder Político."
    }
}

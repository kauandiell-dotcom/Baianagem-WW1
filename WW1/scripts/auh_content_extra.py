"""Extra Austria-Hungary content: dated historical events, institutions, decisions and opinion modifiers.

Compiled by build_ww1_austria_hungary.py (after build_support) into separate files so the base
compiler output stays untouched. All numbers are bounded; nothing creates units, equipment or
manpower (see tests/test_ww1_austria_hungary.py).
"""
P = "AUH_ww1_"

def build_extra(root, locs):
    def put(path, text):
        p = root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text.strip() + "\n", encoding="utf-8")

    def loc(key, pt, en):
        locs[key] = (pt, en)

    def v(name, n):
        return f"add_to_variable = {{ auh_ww1_{name} = {n} }}"

    def timed(idea, days):
        return f"add_timed_idea = {{ idea = {P}{idea} days = {days} }}"

    # ------------------------------------------------------------------ ideas
    # name: (pt, en, modifier, pt_desc, en_desc, permanent)
    ideas = {
        "inst_staff_college": ("Escola de Estado-Maior", "Staff College", "experience_gain_army_factor = .05 planning_speed = .03",
                          "Oficiais formados em Viena aprendem mais com a campanha e planejam um pouco mais depressa: +5% de experiência terrestre e +3% de planejamento.",
                          "Vienna-trained officers learn more from the campaign and plan slightly faster: +5% army experience gain and +3% planning speed.", True),
        "inst_sapper_school": ("Escola de sapadores", "Sapper School", "max_dig_in_factor = .05 consumer_goods_factor = .005",
                          "Engenheiros militares preparam melhores posições defensivas: +5% de entrincheiramento máximo, com um pequeno custo civil.",
                          "Military engineers prepare better defensive positions: +5% maximum entrenchment, at a small civilian cost.", True),
        "inst_pilot_school": ("Escola de pilotos", "Pilot School", "experience_gain_air_factor = .05",
                         "Um curso regular de pilotagem acelera a formação: +5% de experiência aérea.",
                         "A regular flying course speeds training: +5% air experience gain.", True),
        "inst_investment_board": ("Junta de investimentos", "Investment Board", "industrial_capacity_factory = .02 consumer_goods_factor = .01",
                             "Crédito e contratos coordenados entre Viena e Budapeste: +2% de capacidade industrial, com +1% de bens de consumo exigidos.",
                             "Credit and contracts coordinated between Vienna and Budapest: +2% industrial capacity, with +1% consumer goods demanded.", True),
        "subsidised_arsenals": ("Subsídio aos arsenais", "Arsenal Subsidy", "production_factory_efficiency_gain_factor = .04 consumer_goods_factor = .02",
                            "Encomendas antecipadas aos arsenais: +4% de ganho de eficiência da produção, com +2% de bens de consumo exigidos.",
                            "Advance orders to the arsenals: +4% production efficiency gain, with +2% consumer goods demanded.", False),
        "replanned_deployment": ("Mobilização replanejada", "Replanned Deployment", "planning_speed = -.06 dig_in_speed_factor = .04",
                                 "Os planos de concentração foram refeitos depois do caso Redl: −6% de planejamento, +4% de velocidade de entrincheiramento.",
                                 "Concentration plans were rewritten after the Redl affair: −6% planning speed, +4% entrenchment speed.", False),
        "fortress_inspection": ("Cinturão de fortalezas inspecionado", "Fortress Belt Inspected", "dig_in_speed_factor = .06 supply_consumption_factor = .02",
                                "Guarnições e depósitos das fortalezas foram conferidos: +6% de velocidade de entrincheiramento, +2% de consumo de suprimentos.",
                                "Fortress garrisons and depots were inspected: +6% entrenchment speed, +2% supply consumption.", False),
        "front_crisis": ("Crise na frente", "Front-Line Crisis", "army_org_factor = -.05 planning_speed = -.05",
                         "Reservas gastas e planos desfeitos: −5% de organização do exército e −5% de planejamento.",
                         "Spent reserves and broken plans: −5% army organisation and −5% planning speed.", False),
        "strike_wave": ("Onda de greves", "Strike Wave", "industrial_capacity_factory = -.04",
                        "Paralisações nas fábricas: −4% de capacidade industrial.",
                        "Factory stoppages: −4% industrial capacity.", False),
        "naval_unrest": ("Inquietação na marinha", "Naval Unrest", "naval_speed_factor = -.05 refit_speed = -.10",
                         "Tripulações descontentes atrasam as saídas e as reformas: −5% de velocidade naval e −10% de velocidade de reequipagem.",
                         "Discontented crews delay sorties and refits: −5% naval speed and −10% refit speed.", False),
        "winter_training": ("Manobras de inverno", "Winter Manoeuvres", "training_time_army_factor = -.05 consumer_goods_factor = .01",
                              "Unidades treinadas em campo: −5% no tempo de treinamento do exército, com +1% de bens de consumo exigidos.",
                              "Units trained in the field: −5% army training time, with +1% consumer goods demanded.", False),
    }
    body = ["ideas = { country = {"]
    for name, (pt, en, mod, dpt, den, perm) in ideas.items():
        loc(P + name, pt, en)
        loc(P + name + "_desc", dpt, den)
        body.append(f" {P+name} = {{ picture = AUH_ww1_{name} allowed = {{ original_tag = AUS }} removal_cost = -1 modifier = {{ {mod} }} }}")
    body.append("} }")
    put("common/ideas/ww1_austria_hungary_extra_ideas.txt", "\n".join(body))

    # --------------------------------------------------------- opinion modifiers
    opinions = {
        "alliance_renewed": (15, "Aliança renovada com Viena", "Alliance renewed with Vienna"),
        "sofia_contacts": (12, "Contatos com Sófia", "Contacts with Sofia"),
        "porte_contacts": (12, "Missão em Constantinopla", "Mission to Constantinople"),
    }
    ob = ["opinion_modifiers = {"]
    for k, (val, pt, en) in opinions.items():
        ob.append(f" {P+k} = {{ value = {val} decay = 1 }}")
        loc(P + k, pt, en)
    ob.append("}")
    put("common/opinion_modifiers/ww1_austria_hungary_extra_opinions.txt", "\n".join(ob))

    # ------------------------------------------------------------------ events
    events = ["add_namespace = ww1_auh"]

    def event(n, title, desc, opts, picture, trigger=None, mtth=None, once=True, immediate="", cooldown=None):
        key = f"ww1_auh.{n}"
        loc(key + ".t", *title)
        loc(key + ".d", *desc)
        b = ["country_event = {", f" id = {key}", f" title = {key}.t", f" desc = {key}.d", f" picture = GFX_event_AUH_ww1_{picture}"]
        if trigger is None:
            b += [" is_triggered_only = yes"]
        else:
            b += [f" fire_only_once = {'yes' if once else 'no'}",
                  f" trigger = {{ tag = AUS has_country_flag = auh_ww1_initialised {trigger} }}",
                  f" mean_time_to_happen = {{ days = {mtth or 20} }}"]
        imm = immediate
        if cooldown:
            imm += f" set_country_flag = {{ flag = auh_ww1_evt_{n}_cooldown days = {cooldown} }}"
        if imm.strip():
            b += [" immediate = { " + imm.strip() + " }"]
        for i, opt in enumerate(opts):
            pt, en, effect, weight, *rest = opt
            cond = rest[0] if rest else ""
            k = key + "." + chr(97 + i)
            loc(k, pt, en)
            b += [" option = {", f"  name = {k}", f"  ai_chance = {{ base = {weight} }}"]
            if cond:
                b.append("  trigger = { " + cond + " }")
            b += ["  " + effect, "  if = { limit = { tag = AUS } auh_ww1_clamp_counters = yes auh_ww1_update_pressure = yes }", " }"]
        b.append("}")
        events.extend(b)

    cd = lambda n: f"NOT = {{ has_country_flag = auh_ww1_evt_{n}_cooldown }}"

    event(100, ("O projeto do exército e a obstrução húngara", "The Army Bill and Hungarian Obstruction"),
          ("Budapeste condiciona o aumento do contingente anual a concessões sobre a língua de comando e o Honvéd. O estado-maior quer o projeto; a delegação húngara quer cobrá-lo.",
           "Budapest ties the increase in the annual contingent to concessions over the language of command and the Honvéd. The general staff wants the bill; the Hungarian delegation wants to collect its price."),
          [("Aprovar o projeto com concessões a Budapeste.", "Pass the bill with concessions to Budapest.", v("consent", 4) + " " + v("cohesion", -3) + " add_political_power = -25 set_country_flag = auh_ww1_army_bill_passed", 55),
           ("Pedir à Coroa que imponha o projeto.", "Ask the Crown to impose the bill.", v("consent", -8) + " army_experience = 4 add_political_power = 25", 15),
           ("Adiar a votação para a sessão seguinte.", "Postpone the vote to the next session.", v("consent", 2) + " add_war_support = -0.01", 30)],
          "army_bill", trigger="date > 1912.2.1 date < 1913.6.1 has_war = no", mtth=15)

    event(101, ("A Liga Balcânica mobiliza", "The Balkan League Mobilises"),
          ("Sérvia, Bulgária, Grécia e Montenegro se unem contra o Império Otomano. A monarquia precisa decidir quanto custa demonstrar força na fronteira sul.",
           "Serbia, Bulgaria, Greece and Montenegro unite against the Ottoman Empire. The monarchy must decide how much a show of force on the southern border should cost."),
          [("Mobilizar parcialmente a Bósnia e a Galícia.", "Partially mobilise Bosnia and Galicia.", "add_political_power = -40 add_war_support = 0.02 army_experience = 3 " + v("provisions", -3), 35),
           ("Buscar a mediação das grandes potências.", "Seek mediation by the Great Powers.", v("cohesion", 2) + " add_political_power = -20 add_war_support = -0.01", 45),
           ("Consultar Berlim sobre o apoio aliado.", "Consult Berlin on allied support.", "add_political_power = -15 army_experience = 2 " + v("consent", 2), 20, "country_exists = GER NOT = { has_war_with = GER }")],
          "balkan_league", trigger="date > 1912.10.5 date < 1913.2.1 has_war = no", mtth=10)

    event(102, ("A crise de Escútari", "The Scutari Crisis"),
          ("Montenegro cerca Escútari apesar da decisão das potências de criar uma Albânia independente. A monarquia pode demonstrar força no Adriático ou aceitar uma solução de conferência.",
           "Montenegro besieges Scutari despite the Powers' decision to create an independent Albania. The monarchy may show force in the Adriatic or accept a conference solution."),
          [("Enviar uma demonstração naval ao Adriático.", "Send a naval demonstration to the Adriatic.", "navy_experience = 4 add_political_power = -40 " + v("consent", -2), 40),
           ("Aceitar o compromisso da conferência de Londres.", "Accept the London Conference compromise.", v("cohesion", 2) + " add_political_power = 10 add_war_support = -0.01", 40),
           ("Enviar um ultimato a Montenegro.", "Send an ultimatum to Montenegro.", "add_war_support = 0.02 add_political_power = -20 " + v("consent", -3), 20, "country_exists = MNT")],
          "scutari", trigger="date > 1913.4.1 date < 1914.1.1 has_war = no", mtth=10)

    event(103, ("O caso Redl", "The Redl Affair"),
          ("O coronel Alfred Redl, chefe de contraespionagem, vendia os planos de concentração do exército. Tudo o que o estado-maior sabe sobre a mobilização está comprometido.",
           "Colonel Alfred Redl, head of counter-intelligence, had been selling the army's concentration plans. Everything the general staff knows about mobilisation is compromised."),
          [("Refazer os planos de mobilização.", "Rewrite the mobilisation plans.", timed("replanned_deployment", 180) + " army_experience = 2 add_political_power = -30", 65),
           ("Abafar o escândalo e manter os planos.", "Hush up the scandal and keep the plans.", v("consent", -3) + " add_political_power = 15", 35)],
          "redl", trigger="date > 1913.5.25 date < 1914.4.1 has_war = no", mtth=8)

    event(104, ("O círculo do Belvedere", "The Belvedere Circle"),
          ("O arquiduque herdeiro reúne conselheiros que defendem reformas federais e uma monarquia menos dependente de Budapeste. Suas ideias dividem a corte.",
           "The heir to the throne gathers advisers who favour federal reforms and a monarchy less dependent on Budapest. His ideas divide the court."),
          [("Estudar as propostas do Belvedere.", "Study the Belvedere proposals.", v("cohesion", 3) + " " + v("consent", -3) + " add_political_power = -25", 45),
           ("Manter o herdeiro à distância.", "Keep the heir at a distance.", v("consent", 3) + " " + v("cohesion", -2), 55)],
          "belvedere", trigger="date > 1911.9.1 date < 1914.6.1 has_war = no NOT = { has_country_flag = auh_ww1_trialist_constitution }", mtth=40)

    event(105, ("Kolubara: a campanha sérvia fracassa", "Kolubara: The Serbian Campaign Fails"),
          ("O exército dos Bálcãs recua diante do contra-ataque sérvio e o comando pede reforços. Qualquer reforço virá de outra frente.",
           "The Balkan army retreats before the Serbian counter-attack and its command demands reinforcements. Any reinforcement will come from another front."),
          [("Reforçar os Bálcãs com tropas da Galícia.", "Reinforce the Balkans with troops from Galicia.", "army_experience = 3 add_war_support = -0.02 " + v("cohesion", -2), 40),
           ("Trocar o comando e manter a defensiva.", "Replace the command and hold the defensive.", "add_political_power = -30 add_war_support = -0.01 " + v("cohesion", 1), 60)],
          "kolubara", trigger="has_war_with = SER date > 1914.11.20 date < 1915.3.1", mtth=6)

    event(106, ("O inverno nos Cárpatos e Przemyśl", "The Carpathian Winter and Przemyśl"),
          ("Przemyśl está cercada e Conrad propõe romper o cerco por uma ofensiva de inverno. Os soldados têm pouca roupa, pouco pão e uma estrada de montanha.",
           "Przemyśl is surrounded and Conrad proposes a winter offensive to break the ring. The men have little clothing, little bread and one mountain road."),
          [("Ordenar a ofensiva de inverno.", "Order the winter offensive.", "army_experience = 5 add_war_support = -0.02 " + v("provisions", -4) + " " + timed("front_crisis", 60), 35),
           ("Manter a linha e preparar a rendição da fortaleza.", "Hold the line and prepare the fortress's surrender.", "add_political_power = -20 add_war_support = -0.015 army_experience = 2 " + v("cohesion", -2), 65)],
          "carpathian_winter", trigger="has_war_with = SOV date > 1915.1.10 date < 1915.4.1", mtth=6)

    event(107, ("Gorlice e Tarnów", "Gorlice and Tarnów"),
          ("A ofensiva austro-alemã rompe a frente russa. O comando alemão oferece dirigir a operação; aceitar traz vitória rápida, mas também dependência.",
           "The Austro-German offensive breaks the Russian front. The German command offers to direct the operation; accepting brings quick victory but also dependence."),
          [("Aceitar a direção alemã da operação.", "Accept German direction of the operation.", "add_war_support = 0.03 army_experience = 4 " + v("consent", -3), 55, "country_exists = GER NOT = { has_war_with = GER }"),
           ("Exigir participação austro-húngara no comando.", "Demand Austro-Hungarian participation in command.", v("consent", 2) + " add_political_power = -20 add_war_support = 0.01", 45)],
          "gorlice", trigger="has_war_with = SOV date > 1915.5.1 date < 1915.9.1", mtth=6)

    event(108, ("A ofensiva Brusilov", "The Brusilov Offensive"),
          ("Os russos rompem a frente da Galícia e da Bucovina. As reservas foram enviadas ao Trentino e qualquer solução custará algo em outro lugar.",
           "The Russians break the front in Galicia and Bukovina. The reserves were sent to the Trentino, and any solution will cost something elsewhere."),
          [("Pedir reforços alemães.", "Request German reinforcements.", v("consent", -4) + " add_war_support = -0.02 army_experience = 4", 45, "country_exists = GER NOT = { has_war_with = GER }"),
           ("Transferir divisões da frente italiana.", "Transfer divisions from the Italian front.", timed("front_crisis", 60) + " add_war_support = -0.03 army_experience = 2", 30, "has_war_with = ITA"),
           ("Recuar para a linha dos Cárpatos.", "Fall back to the Carpathian line.", v("cohesion", -2) + " add_war_support = -0.03 " + v("provisions", -2), 25)],
          "brusilov", trigger="has_war_with = SOV date > 1916.6.4 date < 1916.10.1", mtth=5)

    event(109, ("Filas de pão em Viena", "Bread Queues in Vienna"),
          ("As filas diante das padarias crescem a cada semana. A cidade espera que o governo escolha entre cozinhas municipais, requisição ou paciência.",
           "The queues outside the bakeries grow every week. The city waits for the government to choose between municipal kitchens, requisition or patience."),
          [("Abrir cozinhas municipais.", "Open municipal kitchens.", v("provisions", 4) + " " + v("cohesion", 2) + " add_political_power = -40", 50),
           ("Requisitar cereal húngaro.", "Requisition Hungarian grain.", v("provisions", 8) + " " + v("consent", -8), 30),
           ("Pedir paciência à população.", "Ask the population for patience.", "add_war_support = -0.01 " + v("cohesion", -3) + " add_political_power = 15", 20)],
          "bread_queues", trigger="has_war = yes date > 1916.11.1 check_variable = { auh_ww1_provisions < 50 } " + cd(109), mtth=12, once=False, cooldown=365)

    event(110, ("A greve de janeiro", "The January Strike"),
          ("Centenas de milhares de operários param nas fábricas de Viena, Wiener Neustadt e Budapeste. Pedem pão, paz e representação. O governo pode negociar ou reprimir.",
           "Hundreds of thousands of workers stop work in the factories of Vienna, Wiener Neustadt and Budapest. They ask for bread, peace and representation. The government may negotiate or repress."),
          [("Negociar com os conselhos operários.", "Negotiate with the workers' councils.", v("cohesion", 4) + " add_political_power = -35", 55),
           ("Reprimir as paralisações.", "Repress the stoppages.", v("cohesion", -5) + " " + timed("strike_wave", 90), 45)],
          "january_strike", trigger="has_war = yes date > 1918.1.14 date < 1918.4.1", mtth=4)

    event(111, ("A declaração da Epifania", "The Epiphany Declaration"),
          ("Deputados tchecos, eslovacos e eslovenos exigem autodeterminação dentro de um Estado democrático. A declaração enfraquece a lealdade do Reichsrat e desafia Budapeste.",
           "Czech, Slovak and Slovene deputies demand self-determination within a democratic state. The declaration weakens the Reichsrat's loyalty and challenges Budapest."),
          [("Abrir conversações sobre autonomia.", "Open talks on autonomy.", v("cohesion", 4) + " " + v("consent", -4) + " add_political_power = -30", 40),
           ("Ignorar a declaração.", "Ignore the declaration.", v("cohesion", -4) + " " + v("consent", 2), 60)],
          "epiphany", trigger="has_war = yes date > 1918.1.6 date < 1918.7.1", mtth=5)

    event(112, ("O motim de Cattaro", "The Cattaro Mutiny"),
          ("Marinheiros de várias nacionalidades hasteiam a bandeira vermelha nos navios de Cattaro. O motim pede pão, paz e melhor tratamento.",
           "Sailors of several nationalities raise the red flag on the ships at Cattaro. The mutiny asks for bread, peace and better treatment."),
          [("Investigar as queixas e fazer concessões.", "Investigate grievances and make concessions.", v("cohesion", 2) + " add_political_power = -25", 50),
           ("Suprimir o motim e punir os cabeças.", "Suppress the mutiny and punish the ringleaders.", v("cohesion", -3) + " navy_experience = 2 " + timed("naval_unrest", 120), 50)],
          "cattaro", trigger="has_war = yes date > 1918.2.1 date < 1918.6.1", mtth=4)

    event(113, ("A ofensiva do Piave", "The Piave Offensive"),
          ("O estado-maior quer uma ofensiva final no Piave antes da colheita italiana e da chegada de mais aliados. Os depósitos estão vazios.",
           "The staff wants a final offensive on the Piave before the Italian harvest and the arrival of more allies. The depots are empty."),
          [("Lançar a ofensiva.", "Launch the offensive.", "army_experience = 4 add_war_support = -0.03 " + v("provisions", -3) + " " + timed("front_crisis", 60), 35),
           ("Manter a linha e inspecionar as fortificações.", "Hold the line and inspect the fortifications.", timed("fortress_inspection", 120) + " add_war_support = -0.01", 65)],
          "piave", trigger="has_war_with = ITA date > 1918.6.10 date < 1918.9.1", mtth=4)

    event(114, ("O manifesto dos povos", "The Peoples' Manifesto"),
          ("Carlos pode proclamar uma federação de povos no Império. A medida é tardia, mas ainda muda a relação com as províncias.",
           "Karl may proclaim a federation of peoples within the Empire. The measure is late, but it still changes the relationship with the provinces."),
          [("Emitir o manifesto.", "Issue the manifesto.", v("cohesion", 6) + " " + v("consent", -6) + " add_political_power = -40 add_war_support = -0.02", 45),
           ("Recusar o manifesto.", "Refuse the manifesto.", v("cohesion", -5) + " " + v("consent", 3), 55)],
          "manifesto", trigger="has_war = yes date > 1918.10.10 date < 1919.1.1 has_country_flag = auh_ww1_karl_accession NOT = { has_country_flag = auh_ww1_federal_constitution }", mtth=3)

    event(115, ("O relatório da colheita", "The Harvest Report"),
          ("Os relatórios dos distritos agrícolas chegam a Viena. O governo precisa decidir se guarda o excedente, vende ou mantém reservas para o exército.",
           "Reports from the agricultural districts reach Vienna. The government must decide whether to store the surplus, sell it or keep reserves for the army."),
          [("Armazenar o excedente.", "Store the surplus.", v("provisions", 5) + " add_political_power = -15", 50),
           ("Vender o excedente e levantar crédito.", "Sell the surplus and raise credit.", "add_political_power = 30 " + v("provisions", -2), 25, "has_war = no"),
           ("Reservar grãos para o exército.", "Set grain aside for the army.", v("provisions", 6) + " " + v("consent", -4), 25, "has_war = yes")],
          "harvest", trigger="date > 1911.9.1 " + cd(115), mtth=20, once=False, cooldown=330)

    event(116, ("A sessão das delegações", "The Session of the Delegations"),
          ("As delegações de Viena e Budapeste se reúnem para votar os créditos comuns. A monarquia pode comprar a boa vontade ou governar por decreto.",
           "The delegations of Vienna and Budapest meet to vote the common credits. The monarchy may buy goodwill or govern by decree."),
          [("Fazer concessões orçamentárias.", "Make budget concessions.", v("consent", 4) + " add_political_power = -30", 65),
           ("Aprovar os créditos por decreto de emergência.", "Approve the credits by emergency decree.", v("consent", -6) + " add_political_power = 20", 35, "has_war = yes")],
          "delegations_session", trigger="date > 1911.11.1 check_variable = { auh_ww1_consent < 60 } NOT = { has_country_flag = auh_ww1_republic } " + cd(116), mtth=25, once=False, cooldown=365)

    event(117, ("A renovação da Tríplice Aliança", "The Renewal of the Triple Alliance"),
          ("Berlim e Roma propõem renovar antecipadamente a Tríplice Aliança. Uma convenção naval amplia a cooperação; um texto simples evita compromissos novos.",
           "Berlin and Rome propose renewing the Triple Alliance early. A naval convention expands cooperation; a plain text avoids new commitments."),
          [("Renovar com uma convenção naval.", "Renew with a naval convention.", "add_political_power = -20 navy_experience = 2 add_opinion_modifier = { target = GER modifier = AUH_ww1_alliance_renewed } add_opinion_modifier = { target = ITA modifier = AUH_ww1_alliance_renewed }", 45),
           ("Renovar sem compromissos adicionais.", "Renew without additional commitments.", v("consent", 2) + " add_opinion_modifier = { target = GER modifier = AUH_ww1_alliance_renewed }", 55)],
          "triple_alliance", trigger="date > 1912.12.1 date < 1913.4.1 has_war = no country_exists = GER country_exists = ITA", mtth=8)

    event(118, ("O relatório do governador da Bósnia", "The Governor's Report from Bosnia"),
          ("O governador informa que a Dieta bósnia é apoiada pela população, mas desconfiada pelos funcionários e pela polícia. A anexação não resolveu as queixas locais.",
           "The governor reports that the Bosnian Diet has popular support but is distrusted by officials and police. Annexation did not resolve local grievances."),
          [("Ampliar os poderes orçamentários da Dieta.", "Expand the Diet's budget powers.", v("cohesion", 3) + " " + v("consent", -2) + " add_political_power = -20", 55),
           ("Reforçar a gendarmaria.", "Strengthen the gendarmerie.", v("cohesion", -3) + " add_political_power = 15", 45)],
          "bosnia_report", trigger="date > 1911.10.1 date < 1914.6.1 has_war = no", mtth=30)

    put("events/ww1_austria_hungary_extra_events.txt", "\n".join(events))

    # --------------------------------------------------------------- decisions
    cats = {"crown", "economy", "military", "diplomacy"}
    decisions = {k: [] for k in cats}

    def decision(cat, key, pt, en, dpt, den, effect, visible, available="", pp=35, days=60, factories=0,
                 reenable=240, complete="", cancel="", ai=1):
        did = P + key
        loc(did, pt, en)
        loc(did + "_desc", dpt, den)
        b = [f" {did} = {{", f"  icon = GFX_decision_AUH_ww1_{key}", "  allowed = { original_tag = AUS }",
             f"  visible = {{ {visible} }}", f"  available = {{ has_capitulated = no {available} }}",
             f"  cost = {pp}", f"  days_remove = {days}", f"  days_re_enable = {reenable}", "  fire_only_once = no",
             f"  ai_will_do = {{ base = {ai} }}"]
        if factories:
            b.append(f"  civilian_factory_use = {factories}")
        b.append("  complete_effect = { " + complete + " }")
        b.append("  remove_effect = { " + effect + " auh_ww1_clamp_counters = yes auh_ww1_update_pressure = yes }")
        b.append("  cancel_trigger = { OR = { has_capitulated = yes " + cancel + " } }")
        b.append(" }")
        decisions[cat].extend(b)

    decision("economy", "arsenal_subsidy", "Subsidiar os arsenais", "Subsidise the Arsenals",
             "Duas fábricas civis por 90 dias financiam encomendas antecipadas: +4% de eficiência de produção por 120 dias, +2% de bens de consumo exigidos e um nível a mais de dívida. Requer limite de dívida livre.",
             "Two civilian factories for 90 days fund advance orders: +4% production efficiency for 120 days, +2% consumer goods demanded and one more debt level. Requires spare debt limit.",
             "", "has_completed_focus = AUH_ww1_skoda_contracts",
             "check_variable = { auh_ww1_debt < 5 } NOT = { has_idea = AUH_ww1_subsidised_arsenals } num_of_civilian_factories_available_for_projects > 1",
             pp=45, days=90, factories=2, reenable=240,
             complete=timed("subsidised_arsenals", 120) + " " + v("debt", 1))
    decision("military", "winter_manoeuvres", "Realizar manobras de inverno", "Hold Winter Manoeuvres",
             "Em paz, uma fábrica civil por 90 dias e 40 equipamentos de apoio financiam manobras: +5 de experiência terrestre e −5% no tempo de treinamento por 120 dias.",
             "In peacetime, one civilian factory for 90 days and 40 support equipment fund manoeuvres: +5 army experience and −5% training time for 120 days.",
             "army_experience = 5 " + timed("winter_training", 120), "has_completed_focus = AUH_ww1_mobilisation_tables",
             "has_war = no num_of_civilian_factories_available_for_projects > 0 has_equipment = { support_equipment > 39 }",
             pp=35, days=90, factories=1, reenable=240,
             complete="add_equipment_to_stockpile = { type = support_equipment amount = -40 }", cancel="has_war = yes")
    decision("military", "inspect_fortress_belt", "Inspecionar o cinturão de fortalezas", "Inspect the Fortress Belt",
             "Em guerra, uma fábrica civil por 45 dias confere guarnições e depósitos: +6% de velocidade de entrincheiramento e +2% de consumo de suprimentos por 120 dias.",
             "In war, one civilian factory for 45 days checks garrisons and depots: +6% entrenchment speed and +2% supply consumption for 120 days.",
             timed("fortress_inspection", 120), "has_completed_focus = AUH_ww1_przemysl_supply",
             "has_war = yes NOT = { has_idea = AUH_ww1_fortress_inspection } num_of_civilian_factories_available_for_projects > 0",
             pp=30, days=45, factories=1, reenable=180, cancel="has_war = no")
    decision("military", "mountain_cadres", "Formar quadros de alta montanha", "Train Mountain Cadres",
             "Uma fábrica civil por 90 dias e 30 equipamentos de apoio financiam a escola alpina: +4 de experiência terrestre. Nenhuma divisão é criada.",
             "One civilian factory for 90 days and 30 support equipment fund the Alpine school: +4 army experience. No division is created.",
             "army_experience = 4", "has_completed_focus = AUH_ww1_alpine_routes",
             "num_of_civilian_factories_available_for_projects > 0 has_equipment = { support_equipment > 29 }",
             pp=30, days=90, factories=1, reenable=240,
             complete="add_equipment_to_stockpile = { type = support_equipment amount = -30 }")
    decision("military", "pola_review", "Passar em revista a esquadra em Pola", "Review the Fleet at Pola",
             "Em paz, uma revista e exercícios de 30 dias concedem +4 de experiência naval.",
             "In peacetime, a 30-day review and exercises grant +4 navy experience.",
             "navy_experience = 4", "has_completed_focus = AUH_ww1_naval_programme", "has_war = no",
             pp=30, days=30, reenable=300, cancel="has_war = yes")
    decision("diplomacy", "sound_out_sofia", "Sondar Sófia", "Sound Out Sofia",
             "Uma missão de 45 dias melhora a opinião búlgara sobre nós, e a Bulgária também passa a ver a monarquia com mais simpatia. Não cria aliança.",
             "A 45-day mission improves Bulgarian opinion of us, and Bulgaria also views the monarchy more favourably. It creates no alliance.",
             "if = { limit = { country_exists = BUL } add_opinion_modifier = { target = BUL modifier = AUH_ww1_sofia_contacts } BUL = { add_opinion_modifier = { target = ROOT modifier = AUH_ww1_sofia_contacts } } }",
             "has_completed_focus = AUH_ww1_foreign_programme", "country_exists = BUL NOT = { has_war_with = BUL }",
             pp=40, days=45, reenable=365, cancel="OR = { NOT = { country_exists = BUL } has_war_with = BUL }")
    decision("diplomacy", "constantinople_mission", "Enviar uma missão a Constantinopla", "Send a Mission to Constantinople",
             "Uma missão de 45 dias melhora a opinião turca sobre nós, e a Turquia também passa a ver a monarquia com mais simpatia. Não cria aliança.",
             "A 45-day mission improves Turkish opinion of us, and Turkey also views the monarchy more favourably. It creates no alliance.",
             "if = { limit = { country_exists = TUR } add_opinion_modifier = { target = TUR modifier = AUH_ww1_porte_contacts } TUR = { add_opinion_modifier = { target = ROOT modifier = AUH_ww1_porte_contacts } } }",
             "has_completed_focus = AUH_ww1_consular_network", "country_exists = TUR NOT = { has_war_with = TUR }",
             pp=40, days=45, reenable=365, cancel="OR = { NOT = { country_exists = TUR } has_war_with = TUR }")
    decision("crown", "coronation_city_visit", "Visita imperial a Budapeste", "Imperial Visit to Budapest",
             "Uma visita de 30 dias à cidade da coroação de Santo Estêvão dá +4 de consentimento e custa −1 de confiança nas demais províncias.",
             "A 30-day visit to the city of the Crown of St Stephen grants +4 consent at a cost of −1 confidence in the other provinces.",
             v("consent", 4) + " " + v("cohesion", -1), "has_completed_focus = AUH_ww1_delegations",
             "check_variable = { auh_ww1_consent < 85 }", pp=45, days=30, reenable=300)
    decision("crown", "governors_conference", "Reunir os governadores provinciais", "Convene the Provincial Governors",
             "Uma conferência de 60 dias dá +4 de confiança provincial e −1 de consentimento, pois Budapeste vê a reunião com desconfiança.",
             "A 60-day conference grants +4 provincial confidence and −1 consent, as Budapest views the meeting with suspicion.",
             v("cohesion", 4) + " " + v("consent", -1), "has_completed_focus = AUH_ww1_crownland_hearings",
             "check_variable = { auh_ww1_cohesion < 85 }", pp=35, days=60, reenable=240)
    out = [f"{P}economy = {{"]
    out += decisions["economy"] + ["}", f"{P}military = {{"] + decisions["military"] + ["}", f"{P}diplomacy = {{"] + decisions["diplomacy"] + ["}", f"{P}crown = {{"] + decisions["crown"] + ["}"]
    put("common/decisions/ww1_auh_extra.txt", "\n".join(out))
    return dict(events=sum(1 for e in events if e.startswith("country_event")), ideas=len(ideas),
                decisions=sum(len([l for l in d if l.startswith(" AUH_ww1_")]) for d in decisions.values()))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Appends complete, authentic bilingual localization (English & Brazilian Portuguese)
for all Ottoman WW1 events (ww1_ottoman.1 to 30), new ideas, decisions, and tooltips.
Preserves UTF-8 BOM.
"""

from pathlib import Path

# Event definitions dictionary
EVENTS_LOC = {
    # 1. Dreadnoughts
    "ww1_ottoman.1.t": ("The British Dreadnought Requisition Crisis", "A Crise da Requisição dos Dreadnoughts Britânicos"),
    "ww1_ottoman.1.d": ("In late July 1914, First Lord of the Admiralty Winston Churchill ordered the seizure of Sultan Osman-ı Evvel and Reşadiye in British shipyards. Financed through private penny donations across Anatolia, the confiscation provoked outrage across the Ottoman Empire.", "Em fins de julho de 1914, o Primeiro Lorde do Almirantado Winston Churchill ordenou a apreensão dos encouraçados Sultan Osman-ı Evvel e Reşadiye nos estaleiros de Newcastle. Financiados por coletas públicas de moedas em cada vila da Anatólia, o confisco britânico despertou uma onda furiosa de indignação popular."),
    "ww1_ottoman.1.a": ("Perfidious Albion has robbed the nation! We will remember!", "A Pérfida Albion roubou o povo! Jamais esqueceremos esta afronta!"),
    "ww1_ottoman.1.b": ("File formal diplomatic protests and demand indemnities.", "Apresentar protestos diplomáticos formais e exigir indenização."),

    # 2. Savior Officers
    "ww1_ottoman.2.t": ("The Savior Officers' Ultimatum", "O Ultimato dos Oficiais Salvadores"),
    "ww1_ottoman.2.d": ("Dissident army officers under the Halâskâr Zâbitân movement have issued an ultimatum to the Sublime Porte, demanding the resignation of the Unionist cabinet and free elections.", "Oficiais dissidentes do exército, organizados na liga Halâskâr Zâbitân, emitiram um ultimato severo à Sublime Porta exigindo a renúncia imediata do gabinete unionista e garantias de eleições livres."),
    "ww1_ottoman.2.a": ("Yield to the officers and invite the liberal opposition.", "Ceder aos oficiais e convidar a oposição liberal para o gabinete."),
    "ww1_ottoman.2.b": ("The CUP vanguard will not compromise with factional mutineers!", "A vanguarda unionista não cederá a conspiradores faccionais!"),

    # 3. Raid on the Sublime Porte
    "ww1_ottoman.3.t": ("The Raid on the Sublime Porte", "O Ataque ao Sublime Porte (Bab-ı Ali Baskını)"),
    "ww1_ottoman.3.d": ("Enver Bey and armed Unionist officers stormed the government council at the Sublime Porte, forcing Grand Vizier Kâmil Pasha to sign his resignation at gunpoint. The Committee of Union and Progress now holds uncontested executive mastery.", "Enver Bey e oficiais armados do CUP invadiram a sala do conselho de ministros na Sublime Porta, forçando o Grão-Vizir Kâmil Pasha a assinar sua renúncia sob a mira de pistolas. O Comitê de União e Progresso assume o controle total do destino nacional."),
    "ww1_ottoman.3.a": ("Consolidate the triumvirate of Enver, Talat, and Cemal!", "Consolidar o triunvirato de Enver, Talat e Cemal!"),
    "ww1_ottoman.3.b": ("Seek constitutional harmony with the Sultan and parliament.", "Buscar harmonia constitucional com o Sultão e o parlamento."),

    # 4. Arab Congress
    "ww1_ottoman.4.t": ("The First Arab Congress of Paris", "O Primeiro Congresso Árabe de Paris"),
    "ww1_ottoman.4.d": ("Arab delegates assembled in Paris to formulate demands for decentralization, official recognition of the Arabic language in schools and courts, and local military service within Arab provinces.", "Delegados árabes reuniram-se em Paris formulando reivindicações de descentralização administrativa, reconhecimento oficial da língua árabe em tribunais e escolas, e serviço militar regionalizado dentro das províncias árabes."),
    "ww1_ottoman.4.a": ("Accept cultural and administrative decentralization.", "Aceitar a descentralização cultural e administrativa dos vilaietes."),
    "ww1_ottoman.4.b": ("Imperial unity permits no centrifugal concessions!", "A unidade imperial não tolera concessões centrífugas!"),

    # 5. Liman von Sanders
    "ww1_ottoman.5.t": ("The German Military Mission of Liman von Sanders", "A Missão Militar Alemã de Liman von Sanders"),
    "ww1_ottoman.5.d": ("Lieutenant General Otto Liman von Sanders has arrived at Constantinople at the head of a comprehensive German military mission charged with restructuring Ottoman army corps, sparking bitter diplomatic protests in Saint Petersburg.", "O Tenente-General Otto Liman von Sanders chegou a Constantinopla chefiando uma missão militar de elite para reformar os corpos de exército otomanos, provocando furiosos protestos diplomáticos por parte de São Petersburgo."),
    "ww1_ottoman.5.a": ("Empower von Sanders and German staff advisors.", "Empoderar von Sanders e os instrutores prussianos na reorganização."),
    "ww1_ottoman.5.b": ("Restrict the mission to advisory instruction only.", "Restringir a missão a funções estritamente pedagógicas e consultivas."),

    # 6. Admiral Limpus
    "ww1_ottoman.6.t": ("The British Naval Mission of Admiral Limpus", "A Missão Naval Britânica do Almirante Limpus"),
    "ww1_ottoman.6.d": ("Rear-Admiral Arthur Limpus has supervised modern dockyard management and gunnery training for the Ottoman fleet, proposing extensive dreadnought refits.", "O Contra-Almirante Arthur Limpus supervisiona as reformas da frota otomana e o treinamento tático nos estaleiros do Chifre de Ouro, sugerindo novas modernizações navais."),
    "ww1_ottoman.6.a": ("Deepen naval contracts with British shipyards.", "Aprofundar os contratos com os estaleiros britânicos."),
    "ww1_ottoman.6.b": ("Develop sovereign Ottoman naval capabilities.", "Priorizar a autonomia soberana da marinha otomana."),

    # 7. OPDA / Debt
    "ww1_ottoman.7.t": ("The Ottoman Public Debt Administration (OPDA)", "A Administração da Dívida Pública (Düyun-ı Umumiye)"),
    "ww1_ottoman.7.d": ("Foreign bondholder representatives in the OPDA hold mortgages over salt, silk, and tobacco revenues. The Porte faces a historic crossroads between fiscal subservience and financial independence.", "Os representantes dos credores estrangeiros na Düyun-ı Umumiye controlam os monopólios fiscais mais lucrativos do império. A Porta encara o dilema entre submissão financeira e soberania fiscal."),
    "ww1_ottoman.7.a": ("Reclaim state monopoly revenues unilaterally!", "Reivindicar unilateralmente as receitas dos monopólios estatais!"),
    "ww1_ottoman.7.b": ("Renegotiate coupon interest rates amicably.", "Renegociar taxas de cupons e juros de forma amigável."),

    # 8. Capitulations
    "ww1_ottoman.8.t": ("Unilateral Abrogation of the Capitulations", "A Abolição Unilateral das Capitulações"),
    "ww1_ottoman.8.d": ("The Porte has issued an imperial irade declaring the immediate abolition of extraterritorial privileges, consular courts, and foreign tax immunities that have hobbled the empire for centuries.", "A Sublime Porta promulgou um irade imperial proclamando a extinção definitiva de todas as imunidades fiscais, privilégios consulares e capitulações que acorrentavam o império há séculos."),
    "ww1_ottoman.8.a": ("The chains of centuries are broken! Long live sovereignty!", "As correntes de séculos foram quebradas! Viva a soberania imperial!"),

    # 9. Taurus Tunnels
    "ww1_ottoman.9.t": ("The Taurus Mountains Railway Breach", "A Passagem das Montanhas Taurus"),
    "ww1_ottoman.9.d": ("German and Ottoman engineers have successfully linked the railway tunnels through the precipitous Taurus and Amanus mountains, connecting Constantinople directly to Syria and Mesopotamia.", "Engenheiros otomanos e alemães completaram a perfuração dos túneis nos Montes Taurus e Amanus, unindo os trilhos de ferro de Constantinopla diretamente à Síria e à Mesopotâmia."),
    "ww1_ottoman.9.a": ("The iron artery of the Empire is open!", "A artéria de ferro do Império está aberta!"),

    # 10. Goeben and Breslau
    "ww1_ottoman.10.t": ("Arrival of SMS Goeben and Breslau", "A Chegada do SMS Goeben e Breslau"),
    "ww1_ottoman.10.d": ("The German Mediterranean Division under Admiral Wilhelm Souchon has evaded the British fleet and anchored off the Dardanelles, requesting entry into the sovereign Straits.", "A esquadra alemã do Almirante Wilhelm Souchon despistou a frota britânica no Mediterrâneo e ancorou nos Dardanelos, solicitando permissão imediata para atravessar os Estreitos."),
    "ww1_ottoman.10.a": ("Fictitiously purchase the warships: Welcome Yavuz and Midilli!", "Comprar simbolicamente os navios: Sejam bem-vindos Yavuz e Midilli!"),
    "ww1_ottoman.10.b": ("Intern the warships under international law.", "Internar as belonaves alemãs em respeito à neutralidade."),

    # 11. Closing Straits
    "ww1_ottoman.11.t": ("The Dardanelles Straits Regime", "O Fechamento dos Estreitos dos Dardanelos"),
    "ww1_ottoman.11.d": ("To protect the imperial capital from hostile battlefleets, the Porte considers closing the Straits to all foreign merchantmen and warships, cutting off the Russian Empire's Black Sea lifeline.", "Para salvaguardar a capital imperial contra armadas hostis, a Sublime Porta cogita fechar os Estreitos a todo tráfego estrangeiro, bloqueando a artéria vital russa no Mar Negro."),
    "ww1_ottoman.11.a": ("Mine the Straits and close the Dardanelles!", "Semear minas e fechar os Dardanelos hermeticamente!"),
    "ww1_ottoman.11.b": ("Keep commercial transit open under strict inspections.", "Manter o trânsito comercial aberto sob inspeção alfandegária."),

    # 12. Secret Alliance
    "ww1_ottoman.12.t": ("The Secret Germano-Ottoman Alliance", "O Tratado Secreto Teuto-Otomano"),
    "ww1_ottoman.12.d": ("On August 2, 1914, Grand Vizier Said Halim Pasha and German Ambassador Baron von Wangenheim signed a secret treaty of alliance pledging mutual defense against Russian aggression.", "Em 2 de agosto de 1914, o Grão-Vizir Said Halim Pasha e o embaixador alemão von Wangenheim firmaram um tratado de aliança defensiva mútua contra a agressão russa."),
    "ww1_ottoman.12.a": ("Ratify our military destiny alongside Germany!", "Ratificar nosso destino militar ao lado da Alemanha!"),
    "ww1_ottoman.12.b": ("Maintain strategic reservation and armed neutrality.", "Reter reservas estratégicas e preservar neutralidade armada."),

    # 13. Black Sea Raid
    "ww1_ottoman.13.t": ("The Black Sea Raid", "A Incursão de Souchon no Mar Negro"),
    "ww1_ottoman.13.d": ("Admiral Souchon has led Yavuz, Midilli, and Ottoman torpedo boats into the Black Sea, bombarding the Russian naval bases of Sevastopol, Odessa, and Novorossiysk.", "O Almirante Souchon conduziu o Yavuz, o Midilli e torpedeiros otomanos para o Mar Negro, bombardeando os portos russos de Sebastopol, Odessa e Novorossiysk."),
    "ww1_ottoman.13.a": ("The die is cast: We enter the Great War!", "A sorte está lançada: Entramos na Grande Guerra!"),
    "ww1_ottoman.13.b": ("Disavow the raid as an unauthorized German act!", "Repudiar a incursão como um ato alemão não autorizado!"),

    # 14. Holy Jihad
    "ww1_ottoman.14.t": ("Proclamation of Holy Jihad (Cihad-ı Ekber)", "A Proclamação da Guerra Santa (Cihad-ı Ekber)"),
    "ww1_ottoman.14.d": ("Sultan Mehmed V, in his role as Caliph of all Muslims, has proclaimed a sacred duty of jihad against the Entente powers oppressing Muslim lands in India, North Africa, and Central Asia.", "O Sultão Mehmed V, investido como Califa de todos os Muçulmanos, proclamou solenemente o Cihad-ı Ekber convocando todos os crentes a se levantarem contra a tirania imperialista da Entente."),
    "ww1_ottoman.14.a": ("Raise the Sacred Banner of the Prophet!", "Erguer o Estandarte Sagrado do Profeta!"),
    "ww1_ottoman.14.b": ("Emphasize civic and constitutional patriotic solidarity.", "Enfatizar a solidariedade cívica de todas as comunidades do império."),

    # 15. Sarikamis
    "ww1_ottoman.15.t": ("The Battle of Sarıkamış & The Third Army", "A Batalha de Sarıkamış e a Lição do 3º Exército"),
    "ww1_ottoman.15.d": ("Enver Pasha's ambitious winter offensive against Russian positions in the Allahuekber mountains faced blinding blizzards and catastrophic supply breakdowns.", "A audaciosa ofensiva de inverno de Enver Pasha nas montanhas congeladas de Allahuekber enfrentou nevascas mortais e falhas logísticas nas rotas de Erzurum."),
    "ww1_ottoman.15.a": ("Reorganize the Caucasus front with defensive prudence.", "Reorganizar a frente do Cáucaso com prudência defensiva."),
    "ww1_ottoman.15.b": ("Demand an all-out assault through the mountain passes!", "Ordenar o avanço total pelas gargantas montanhosas!"),

    # 16. 18 March Çanakkale
    "ww1_ottoman.16.t": ("18 March: The Naval Triumph of Çanakkale", "18 de Março: O Triunfo Naval de Çanakkale"),
    "ww1_ottoman.16.d": ("Allied dreadnoughts attempting to force the Dardanelles struck minefields laid by the Nusret and faced lethal plunging fire from coastal fortresses. Three battleships were sunk and three crippled.", "Os encouraçados aliados que tentavam forçar os Dardanelos colidiram com as minas clandestinas do Nusret e enfrentaram o fogo fulminante dos fortes de Çanakkale. Três couraçados afundaram e três foram desativados."),
    "ww1_ottoman.16.a": ("Çanakkale Geçilmez! The Straits are impenetrable!", "Çanakkale Geçilmez! Os Dardanelos são intransponíveis!"),

    # 17. Gallipoli / Kut
    "ww1_ottoman.17.t": ("The Epic Triumph of Gallipoli", "O Triunfo Épico de Galípoli"),
    "ww1_ottoman.17.d": ("Allied invasion armies at Anzac Cove, Suvla Bay, and Cape Helles have been completely repulsed through the tenacity of Ottoman defenders under Mustafa Kemal and Esad Pasha. The invaders have evacuated in defeat.", "As forças expedicionárias aliadas em Anzac, Suvla e Cabo Helles foram rechaçadas pela resistência heróica das divisões otomanas lideradas por Mustafa Kemal e Esad Pasha. O invasor evacuou derrotado."),
    "ww1_ottoman.17.a": ("Victory belongs to the steadfast soldiers of Islam!", "A vitória pertence aos inabaláveis soldados do Império!"),

    # 18. Locust / Famine
    "ww1_ottoman.18.t": ("The Great Locust Plague of the Levant", "A Grande Praga de Gafanhotos no Levante"),
    "ww1_ottoman.18.d": ("Devastating swarms of desert locusts stripped crops bare across Syria, Lebanon, and Palestine in 1915, triggering catastrophic bread shortages and threatening the food security of the Fourth Army.", "Enxames devastadores de gafanhotos devoraram as colheitas da Síria, Líbano e Palestina em 1915, deflagrando uma severa crise de subsistência que ameaça as linhas de abastecimento do Quarto Exército."),
    "ww1_ottoman.18.a": ("Deploy imperial grain reserves and relief brigades.", "Distribuir as reservas de trigo imperial e socorrer as populações."),
    "ww1_ottoman.18.b": ("Ration food strictly: The army comes first!", "Racionar impiedosamente: A prioridade absoluta é a frente militar!"),

    # 19. Arab Revolt
    "ww1_ottoman.19.t": ("The Arab Revolt in the Hejaz", "A Erupção da Revolta Árabe no Hejaz"),
    "ww1_ottoman.19.d": ("Sharif Hussein of Mecca, incited by British promises and gold, has fired a rifle shot from his palace window in Mecca, proclaiming rebellion against Ottoman sovereignty.", "Sharif Hussein de Meca, seduzido pelo ouro e promessas do Alto Comissariado britânico no Cairo, disparou um tiro de rifle de sua janela proclamando a insurreição contra a soberania otomana."),
    "ww1_ottoman.19.a": ("Garrison Medina and rally loyal bedouin tribes!", "Guarnecer Medina e convocar as tribos beduínas leais!"),
    "ww1_ottoman.19.b": ("Offer generous autonomy terms to Arab notables.", "Oferecer termos generosos de autonomia aos notáveis árabes."),

    # 20. Fakhri Pasha Medina
    "ww1_ottoman.20.t": ("Fakhri Pasha's Legendary Stand at Medina", "A Defesa Lendária de Medina por Fakhri Pasha"),
    "ww1_ottoman.20.d": ("Major General Fahreddin Pasha, 'The Tiger of the Desert', has refused repeated surrender demands, defending the Prophet's Mosque in Medina through years of total siege with heroic devotion.", "O Major-General Fahreddin Pasha, o 'Tigre do Deserto', rejeitou todas as ordens de capitulação, defendendo o túmulo do Profeta em Medina sob cerco implacável com bravura inabalável."),
    "ww1_ottoman.20.a": ("The sacred trust of Medina shall never fall!", "A custódia sagrada de Medina jamais cairá!"),

    # 21. Gaza-Beersheba
    "ww1_ottoman.21.t": ("The Defense of the Gaza-Beersheba Line", "A Defesa da Linha de Gaza-Beersheba"),
    "ww1_ottoman.21.d": ("Ottoman divisions reinforced by Austrian heavy batteries have entrenched along the desert frontier of Palestine, repulsing British advances from the Sinai.", "Divisões otomanas reforçadas por artilharia pesada austro-húngara entrincheiraram-se na linha de Gaza-Beersheba, bloqueando os avanços da Força Expedicionária Egípcia britânica."),
    "ww1_ottoman.21.a": ("Hold the gates of Jerusalem at all costs!", "Defender as portas de Jerusalém a qualquer custo!"),

    # 22. Baku Liberation
    "ww1_ottoman.22.t": ("The Army of Islam Liberates Baku", "O Exército do Islã de Nuri Pasha Liberta Baku"),
    "ww1_ottoman.22.d": ("Nuri Pasha's newly formed Army of Islam has driven British and Bolshevik detachments out of Baku, securing the petroleum wealth of the Caspian Sea and forging solidarity with Azerbaijan.", "O Exército do Islã comandado por Nuri Pasha expulsou destacamentos britânicos e bolcheviques de Baku, garantindo as ricas reservas petrolíferas do Cáspio e unindo-se aos azeris."),
    "ww1_ottoman.22.a": ("The Caspian petroleum is secured for the Empire!", "O petróleo do Cáspio está garantido para o Império!"),

    # 23. Mehmed VI
    "ww1_ottoman.23.t": ("Ascension of Sultan Mehmed VI Vahideddin", "Ascensão do Sultão Mehmed VI Vahideddin"),
    "ww1_ottoman.23.d": ("Following the demise of Sultan Mehmed V Reshad in July 1918, his brother Mehmed VI Vahideddin has ascended the imperial throne, pledging to protect the realm amidst turbulent war skies.", "Após o falecimento de Mehmed V Reshad em julho de 1918, seu irmão Mehmed VI Vahideddin sobe ao trono imperial jurando defender o Estado Otomano em meio às tempestades da guerra."),
    "ww1_ottoman.23.a": ("May Allah grant wisdom to the Padishah!", "Que Deus conceda sabedoria e força ao Padishah!"),

    # 24. National Bank
    "ww1_ottoman.24.t": ("Founding of the Osmanlı İtibar-ı Millî Bankası", "Fundação do Osmanlı İtibar-ı Millî Bankası"),
    "ww1_ottoman.24.d": ("The Porte has chartered the National Credit Bank to mobilize domestic capital, replace foreign-dominated financial syndicates, and issue banknotes backed by national treasuries.", "A Sublime Porta fundou o Banco de Crédito Nacional para mobilizar as poupanças domésticas, substituir credores estrangeiros e emitir moeda soberana lastreada na produção nacional."),
    "ww1_ottoman.24.a": ("A monumental pillar of economic independence!", "Um pilar monumental para nossa independência econômica!"),

    # 25. Mesopotamian Oil
    "ww1_ottoman.25.t": ("The Petroleum Wealth of Mesopotamia", "O Petróleo da Mesopotâmia: Kirkuk e Mosul"),
    "ww1_ottoman.25.d": ("Exploration geologists have confirmed vast petroleum deposits beneath the hills of Mosul and Kirkuk. The government debates whether to establish a state monopoly or grant joint concessions.", "Geólogos confirmaram jazidas de petróleo gigantescas nos vales de Mosul e Kirkuk. O governo debate entre estatização total sob monopólio imperial ou concessões bilaterais protegidas."),
    "ww1_ottoman.25.a": ("Nationalize all concessions under the Sublime Porte!", "Estatizar todas as reservas petrolíferas sob o controle da Porta!"),
    "ww1_ottoman.25.b": ("License concessions with guaranteed imperial royalties.", "Conceder licenças de exploração com royalties garantidos à Coroa."),

    # 26. Yemen Da'an
    "ww1_ottoman.26.t": ("The Treaty of Da'an & Yemen's Loyalty", "O Tratado de Da'an e a Lealdade do Iêmen"),
    "ww1_ottoman.26.d": ("Through the Treaty of Da'an, the Ottoman Empire has recognized the Zaidi Imam Yahya's internal religious autonomy in exchange for absolute political loyalty to the Caliphate, securing the southern frontier.", "Por meio do Tratado de Da'an, a Sublime Porta reconheceu a autonomia religiosa interna do Imam Yahya no Iêmen em troca de fidelidade incondicional ao Califado, garantindo a paz no sul."),
    "ww1_ottoman.26.a": ("The southern gateway to the Red Sea is pacified.", "O bastião meridional do Mar Vermelho está pacificado."),

    # 27. Turco-Arab Federation
    "ww1_ottoman.27.t": ("The Turco-Arab Federal Compact", "A Ratificação do Pacto Federal Turco-Árabe"),
    "ww1_ottoman.27.d": ("Delegates from Damascus, Baghdad, Beirut, and Jerusalem have signed a historic charter transforming the empire into a dual Ottoman-Arab commonwealth with shared legislative authority.", "Notáveis e representantes de Damasco, Bagdá, Beirute e Jerusalém assinaram a carta histórica transformando o império em uma federação turco-árabe com representação igualitária."),
    "ww1_ottoman.27.a": ("Brothers in faith and history, united forever!", "Irmãos de fé e de história, unidos para sempre!"),

    # 28. Eternal Triumph
    "ww1_ottoman.28.t": ("The Triumph of the Eternal State", "O Triunfo do Estado Eterno (Devlet-i Aliyye)"),
    "ww1_ottoman.28.d": ("Having weathered six years of world conflict, economic siege, and external conspiracies, the Ottoman Empire emerges as a victorious, modernized major power respected across the globe.", "Tendo superado seis anos de cerco mundial, guerras de trincheira e pressões externas, o Império Otomano ressurge vitorioso e renovado como uma grande potência moderna respeitada no mundo."),
    "ww1_ottoman.28.a": ("Devlet-i Aliyye-i Osmaniyye ebed-müddet!", "O Império Otomano permanecerá eterno!"),

    # 29. Misak-i Milli
    "ww1_ottoman.29.t": ("The National Pact (Misak-ı Millî)", "O Pacto Nacional (Misak-ı Millî)"),
    "ww1_ottoman.29.d": ("Parliament has unanimously adopted the Misak-ı Millî declaration, affirming that territories populated by an Ottoman majority within armistice borders form an indivisible homeland.", "O parlamento otomano aprovou solenemente o Misak-ı Millî, declarando que todos os territórios habitados por maioria otomana constituem uma pátria una, soberana e indivisível."),
    "ww1_ottoman.29.a": ("Not one inch of the motherland shall be surrendered!", "Nem um palmo da pátria será entregue a agressores!"),

    # 30. Brest-Litovsk
    "ww1_ottoman.30.t": ("The Restitution of Kars, Ardahan, and Batum", "A Restituição de Kars, Ardahan e Batum"),
    "ww1_ottoman.30.d": ("Under the terms of the Treaty of Brest-Litovsk, Soviet Russia has retroceded the historic provinces of Kars, Ardahan, and Batum lost in 1878, restoring the eastern imperial border.", "Nos termos ratificados de Brest-Litovsk, a Rússia soviética restituiu as províncias históricas de Kars, Ardahan e Batum perdidas na guerra de 1878, redefinindo as fronteiras orientais."),
    "ww1_ottoman.30.a": ("Our ancestral soil has returned to the fold!", "O solo dos nossos ancestrais retornou ao seio imperial!"),
}

IDEAS_LOC = {
    "TUR_milli_iktisat_economy": ("National Economy (Milli İktisat)", "Economia Nacional (Milli İktisat)"),
    "TUR_milli_iktisat_economy_desc": ("Promotion of domestic enterprise, industrialization, and elimination of parasitic commercial middle-men.", "Promoção da indústria doméstica, cooperativas nacionais e eliminação de intermediários comerciais estrangeiros."),
    "TUR_tax_farming_abolished": ("Abolition of Tax Farming (İltizam)", "Fim do Sistema de Arrecadação İltizam"),
    "TUR_tax_farming_abolished_desc": ("Direct provincial revenue collection by civil bureaucrats replaces extortionate private tax farmers.", "Arrecadação fiscal direta por funcionários da fazenda pública em substituição a coletores privados gananciosos."),
    "TUR_monetary_gold_lira": ("Gold Lira Monetary Standard", "Padrão Lira de Ouro Soberano"),
    "TUR_monetary_gold_lira_desc": ("A stable national currency backed by bullion shields the Ottoman economy from foreign speculative panic.", "Uma moeda nacional estável lastreada em ouro protege as finanças imperiais contra ataques especulativos externos."),
    "TUR_munitions_directorate_idea": ("Imperial Munitions Directorate", "Diretoria Imperial de Munições"),
    "TUR_munitions_directorate_idea_desc": ("Centralized coordination of foundries, cartridge works, and powder mills maximizes ammunition output.", "Coordenação centralizada de fundições de artilharia, cartucheiras e fábricas de pólvora para abastecer as frentes de combate."),
    "TUR_heavy_ordnance_idea": ("Krupp Heavy Siege Ordnance", "Artilharia Pesada de Assédio Krupp"),
    "TUR_heavy_ordnance_idea_desc": ("Modern heavy howitzers and fortress guns provide overwhelming counter-battery superiority.", "Obuses modernos e peças de cerco fornecem superioridade avassaladora de contrabateria nas frentes de trincheira."),
    "TUR_prusso_ottoman_tactics": ("Prusso-Ottoman Tactical Doctrines", "Doutrinas Táticas Prusso-Otomanas"),
    "TUR_prusso_ottoman_tactics_desc": ("Rigorous staff planning, tactical decentralization, and flexible operational maneuver.", "Planejamento rigoroso do Estado-Maior, descentralização de comandos e manobra operacional disciplinada."),
    "TUR_red_crescent_logistics": ("Red Crescent Medical Logistics", "Logística do Crescente Vermelho"),
    "TUR_red_crescent_logistics_desc": ("Field hospitals, stretcher battalions, and hygienic standards save thousands of wounded soldiers.", "Hospitais de campanha, batalhões de maqueiros e profilaxia médica salvam vidas preciosas nas frentes montanhosas e desérticas."),
    "TUR_breadbasket_idea": ("Imperial Breadbasket Reserves", "Reservas do Celeiro Imperial"),
    "TUR_breadbasket_idea_desc": ("Strategic grain stores protect both urban populations and army corps from famine and blockades.", "Silos estratégicos e regulação de cereais protegem as cidades e o exército contra a fome e o bloqueio marítimo."),
    "TUR_reformed_ottoman_corps": ("Reformed Ottoman Corps", "Corpos de Exército Otomanos Reformados"),
    "TUR_reformed_ottoman_corps_desc": ("Reorganized along modern triangular division standards with organic artillery and communications.", "Divisões reorganizadas no padrão triangular moderno com artilharia divisionária integrada e comunicações por rádio."),
    "TUR_mesopotamian_oil_production": ("Mesopotamian Petroleum Fields", "Campos Petrolíferos da Mesopotâmia"),
    "TUR_mesopotamian_oil_production_desc": ("Abundant oil from Kirkuk and Mosul supplies the fleet and armed forces with continuous domestic fuel.", "O petróleo abundante de Kirkuk e Mosul abastece a frota e as ferrovias militares com combustível doméstico contínuo."),
}

DECISIONS_LOC = {
    "TUR_emergency_imperial_rally": ("Emergency Imperial Cohesion Rally", "Rally de Emergência da Coesão Imperial"),
    "TUR_emergency_imperial_rally_desc": ("Mobilize public proclamations, local notables, and patriotic assemblies to restore imperial cohesion.", "Mobilizar proclamações cívicas, clérigos e notáveis provinciais para restaurar a coesão imperial em tempos de crise."),
    "TUR_pacify_levant_notables": ("Pacify Provincial Notables of the Levant", "Apaziguar Notáveis Provinciais do Levante"),
    "TUR_pacify_levant_notables_desc": ("Grant budgetary concessions and municipal privileges to Syrian and Iraqi leaders to keep the provinces peaceful.", "Conceder privilégios municipais e créditos a líderes das províncias árabes para garantir a estabilidade interna."),
}

def update_loc():
    en_file = Path("localisation/english/ww1_ottoman_l_english.yml")
    pt_file = Path("localisation/braz_por/ww1_ottoman_l_braz_por.yml")

    en_content = en_file.read_bytes().decode("utf-8")
    pt_content = pt_file.read_bytes().decode("utf-8")

    en_lines = []
    pt_lines = []

    # Process events
    for k, (en_val, pt_val) in EVENTS_LOC.items():
        if f"{k}:" not in en_content:
            en_lines.append(f' {k}:0 "{en_val}"')
        if f"{k}:" not in pt_content:
            pt_lines.append(f' {k}:0 "{pt_val}"')

    # Process ideas
    for k, (en_val, pt_val) in IDEAS_LOC.items():
        if f"{k}:" not in en_content:
            en_lines.append(f' {k}:0 "{en_val}"')
        if f"{k}:" not in pt_content:
            pt_lines.append(f' {k}:0 "{pt_val}"')

    # Process decisions
    for k, (en_val, pt_val) in DECISIONS_LOC.items():
        if f"{k}:" not in en_content:
            en_lines.append(f' {k}:0 "{en_val}"')
        if f"{k}:" not in pt_content:
            pt_lines.append(f' {k}:0 "{pt_val}"')

    # Append to files preserving UTF-8 BOM
    if en_lines:
        new_en = en_content.rstrip() + "\n\n # --- Expanded WW1 Narrative & Systemic Keys ---\n" + "\n".join(en_lines) + "\n"
        en_file.write_bytes(b"\xef\xbb\xbf" + new_en.encode("utf-8"))
        print(f"Added {len(en_lines)} keys to {en_file}")

    if pt_lines:
        new_pt = pt_content.rstrip() + "\n\n # --- Expanded WW1 Narrative & Systemic Keys ---\n" + "\n".join(pt_lines) + "\n"
        pt_file.write_bytes(b"\xef\xbb\xbf" + new_pt.encode("utf-8"))
        print(f"Added {len(pt_lines)} keys to {pt_file}")

if __name__ == "__main__":
    update_loc()

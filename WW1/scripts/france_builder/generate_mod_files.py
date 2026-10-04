import os
import sys
import codecs

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from france_builder.data_foci import FRENCH_FOCI
from france_builder.data_ideas import FRENCH_IDEAS
from france_builder.data_decisions import FRENCH_CATEGORIES, FRENCH_DECISIONS_CODE
from france_builder.data_events import FRENCH_EVENTS_CODE

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def generate_focus_tree():
    out_path = os.path.join(BASE_DIR, "common", "national_focus", "france.txt")
    print(f"Generating Focus Tree: {out_path}")
    
    with open(out_path, "w", encoding="utf-8") as out:
        out.write("# =========================================================================\n")
        out.write("# FRENCH REPUBLIC NATIONAL FOCUS TREE (1911-1918) — COMPLETE OVERHAUL\n")
        out.write(f"# Total Focuses: {len(FRENCH_FOCI)}\n")
        out.write("# =========================================================================\n\n")
        out.write("focus_tree = {\n")
        out.write("\tid = french_focus_tree\n")
        out.write("\tcountry = {\n")
        out.write("\t\tfactor = 0\n")
        out.write("\t\tmodifier = {\n")
        out.write("\t\t\tadd = 10\n")
        out.write("\t\t\ttag = FRA\n")
        out.write("\t\t}\n")
        out.write("\t}\n")
        out.write("\tdefault = no\n")
        out.write("\treset_on_civilwar = no\n")
        out.write("\tcontinuous_focus_position = { x = 60 y = 1800 }\n\n")

        for f in FRENCH_FOCI:
            out.write("\tfocus = {\n")
            out.write(f"\t\tid = {f['id']}\n")
            out.write(f"\t\ticon = GFX_{f['id']}\n")
            out.write(f"\t\tcost = {f['cost']}\n")
            out.write(f"\t\tx = {f['x']}\n")
            out.write(f"\t\ty = {f['y']}\n")

            # Prereqs
            for p in f.get('prereq', []):
                if isinstance(p, list):
                    out.write("\t\tprerequisite = {\n")
                    for sub_p in p:
                        out.write(f"\t\t\tfocus = {sub_p}\n")
                    out.write("\t\t}\n")
                else:
                    out.write(f"\t\tprerequisite = {{ focus = {p} }}\n")

            # Mutually exclusive
            for m in f.get('mut_ex', []):
                out.write(f"\t\tmutually_exclusive = {{ focus = {m} }}\n")

            # allow_branch
            if f.get('allow_branch'):
                out.write(f"\t\tallow_branch = {{\n")
                for ab_line in f['allow_branch'].splitlines():
                    out.write(f"\t\t\t{ab_line.strip()}\n")
                out.write("\t\t}\n")

            # available
            if f.get('available'):
                out.write(f"\t\tavailable = {{\n")
                for av_line in f['available'].splitlines():
                    out.write(f"\t\t\t{av_line.strip()}\n")
                out.write("\t\t}\n")

            out.write("\t\tai_will_do = { factor = 10 }\n")

            # completion_reward
            out.write("\t\tcompletion_reward = {\n")
            reward = f.get('reward', 'add_political_power = 50')
            for r_line in reward.splitlines():
                if r_line.strip():
                    out.write(f"\t\t\t{r_line.strip()}\n")
            out.write("\t\t}\n")

            out.write("\t}\n\n")

        out.write("}\n")
    print(f"Successfully generated focus tree with {len(FRENCH_FOCI)} focuses.")

def generate_ideas():
    out_path = os.path.join(BASE_DIR, "common", "ideas", "ww1_france_ideas.txt")
    print(f"Generating Ideas: {out_path}")
    with open(out_path, "w", encoding="utf-8") as out:
        out.write("# =========================================================================\n")
        out.write("# FRENCH REPUBLIC NATIONAL SPIRITS & IDEAS (1911-1918)\n")
        out.write(f"# Total Ideas: {len(FRENCH_IDEAS)}\n")
        out.write("# =========================================================================\n\n")
        out.write("ideas = {\n")
        out.write("\tcountry = {\n")
        for iid, idef in FRENCH_IDEAS.items():
            out.write(f"\t\t{iid} = {{\n")
            out.write(f"\t\t\tpicture = {iid}\n")
            out.write("\t\t\tallowed = { always = no }\n")
            out.write("\t\t\tmodifier = {\n")
            for mod_name, mod_val in idef.get("modifier", {}).items():
                out.write(f"\t\t\t\t{mod_name} = {mod_val}\n")
            out.write("\t\t\t}\n")
            out.write("\t\t}\n\n")
        out.write("\t}\n")
        out.write("}\n")
    print(f"Successfully generated {len(FRENCH_IDEAS)} ideas.")

def generate_decisions():
    cat_path = os.path.join(BASE_DIR, "common", "decisions", "categories", "ww1_france_categories.txt")
    print(f"Generating Decision Categories: {cat_path}")
    with open(cat_path, "w", encoding="utf-8") as out:
        out.write("# =========================================================================\n")
        out.write("# FRENCH REPUBLIC DECISION CATEGORIES\n")
        out.write("# =========================================================================\n\n")
        for cid, cdef in FRENCH_CATEGORIES.items():
            out.write(f"{cid} = {{\n")
            out.write(f"\ticon = {cdef.get('icon', 'generic_democracy')}\n")
            out.write(f"\tpicture = {cdef.get('picture', 'decision_cat_generic')}\n")
            out.write(f"\tpriority = {cdef.get('priority', 100)}\n")
            out.write(f"\tallowed = {{ original_tag = FRA }}\n")
            out.write("}\n\n")

    dec_path = os.path.join(BASE_DIR, "common", "decisions", "ww1_france_decisions.txt")
    print(f"Generating Decisions: {dec_path}")
    with open(dec_path, "w", encoding="utf-8") as out:
        out.write(FRENCH_DECISIONS_CODE)
    print("Successfully generated decisions.")

def generate_events():
    evt_path = os.path.join(BASE_DIR, "events", "ww1_france_events.txt")
    print(f"Generating Events: {evt_path}")
    with open(evt_path, "w", encoding="utf-8") as out:
        out.write(FRENCH_EVENTS_CODE)
    print("Successfully generated events.")

def generate_localisation():
    en_path = os.path.join(BASE_DIR, "localisation", "english", "ww1_france_l_english.yml")
    pt_path = os.path.join(BASE_DIR, "localisation", "braz_por", "ww1_france_l_braz_por.yml")
    print(f"Generating Localisation: {en_path} and {pt_path}")

    # English Localisation
    with open(en_path, "wb") as f_en:
        f_en.write(codecs.BOM_UTF8)
        content_en = []
        content_en.append("l_english:\n")
        content_en.append(" # ========================================================================\n")
        content_en.append(" # FRENCH FOCUS TREE LOCALISATION\n")
        content_en.append(" # ========================================================================\n")
        for f in FRENCH_FOCI:
            fid = f['id']
            title = f.get('title', fid).replace('"', "'")
            desc = f.get('desc', '').replace('"', "'")
            content_en.append(f' {fid}:0 "{title}"\n')
            content_en.append(f' {fid}_desc:0 "{desc}"\n')

        content_en.append("\n # ========================================================================\n")
        content_en.append(" # FRENCH IDEAS LOCALISATION\n")
        content_en.append(" # ========================================================================\n")
        for iid, idef in FRENCH_IDEAS.items():
            name = idef.get('name', iid).replace('"', "'")
            desc = idef.get('desc', '').replace('"', "'")
            content_en.append(f' {iid}:0 "{name}"\n')
            content_en.append(f' {iid}_desc:0 "{desc}"\n')

        content_en.append("\n # ========================================================================\n")
        content_en.append(" # FRENCH DECISION CATEGORIES\n")
        content_en.append(" # ========================================================================\n")
        for cid, cdef in FRENCH_CATEGORIES.items():
            name = cdef.get('name', cid).replace('"', "'")
            desc = cdef.get('desc', '').replace('"', "'")
            content_en.append(f' {cid}:0 "{name}"\n')
            content_en.append(f' {cid}_desc:0 "{desc}"\n')

        content_en.append("\n # ========================================================================\n")
        content_en.append(" # FRENCH DECISIONS & MISSIONS\n")
        content_en.append(" # ========================================================================\n")
        dec_locs_en = {
            "FRA_execute_plan_xvii_mission": ("Execute Plan XVII Operational Breakthrough", "Joffre's grand offensive into the lost provinces of Alsace and Lorraine. We must capture Strasbourg and Colmar within 25 days!"),
            "FRA_prep_first_army_belfort": ("Mobilize 1st Army at Belfort", "Concentrate infantry corps and mountain artillery at the Belfort gap to spearhead the breakthrough into Mulhouse."),
            "FRA_prep_second_army_morhange": ("Deploy 2nd Army at Nancy & Morhange", "General Castelnau's army must breach the German frontier fortresses and liberate Sarrebourg."),
            "FRA_prep_eastern_railway_priority": ("Eastern Railway Mobilization Priority", "Grant Compagnie de l'Est top priority to move 50 trainloads of artillery shells per day to the Lorraine front."),
            "FRA_requisition_parisian_taxis": ("Requisition Parisian Taxis de la Marne", "Order police to requisition 600 Renault AG-1 taxis in Paris to rush infantry reinforcements to the Ourcq."),
            "FRA_deploy_gallieni_mobile_reserves": ("Deploy Gallieni's Capital Reserves", "Sortie the garrisons of the Camp Retranché de Paris to smash von Kluck's exposed western flank."),
            "FRA_fortify_paris_camp_retranche": ("Fortify Camp Retranché de Paris", "Dig trenches and lay wire across the outer Parisian belt to ensure the capital can withstand any siege."),
            "FRA_activate_la_voie_sacree": ("Organize La Voie Sacrée Logistical Convoy", "Mobilize thousands of Berliet trucks on the Bar-le-Duc artery to supply 50,000 tons of ammunition weekly to Verdun."),
            "FRA_rotate_frontline_divisions_noria": ("Execute Pétain's Noria Rotation", "Cycle exhausted divisions out of the Verdun cauldron after 10 days to preserve manpower and morale."),
            "FRA_concentrate_heavy_artillery_meuse": ("Concentrate Heavy Artillery on the Meuse", "Deploy hundreds of Schneider 155mm howitzers to silence German battery fire on Dead Man's Hill."),
            "FRA_petain_welfare_and_leave_reform": ("Pétain's Soldier Welfare & Leave Reforms", "Guarantee home leave and rest camps to alleviate the deep despair of the front poilus."),
            "FRA_improve_trench_soup_and_wine": ("Improve Warm Trench Rations & Wine ('Le Pinard')", "Ensure insulated food marmites reach the front trenches with hot food and generous daily rations of wine."),
            "FRA_measured_justice_and_pardons": ("Measured Justice & Clemency Protocols", "Pardon the vast majority of deceived conscripts while executing only ringleaders to restore trust in command."),
            "FRA_draconian_decimation_repression": ("Draconian Decimation & Executions", "Enforce brutal military code to shoot mutineers pour encourager les autres. High risk of national strike!"),
            "FRA_issue_national_defense_bonds": ("Issue National Defense War Bonds", "'Pour la France, Versez Votre Or!' Mobilize citizen gold savings to fund the war effort without hyperinflation."),
            "FRA_expand_munitionnettes_workforce": ("Mobilize the 'Munitionnettes' Workforce", "Recruit hundreds of thousands of patriotic French women to machine 75mm shells in Paris armaments factories."),
            "FRA_equip_doughboys_with_french_equipment": ("Equip US Doughboys with French Arms", "Supply arriving American divisions with Canon de 75mm guns, Chauchat light machine guns, and Renault FT tanks."),
        }
        for dkey, (dtitle, ddesc) in dec_locs_en.items():
            content_en.append(f' {dkey}:0 "{dtitle}"\n')
            content_en.append(f' {dkey}_desc:0 "{ddesc}"\n')

        content_en.append("\n # ========================================================================\n")
        content_en.append(" # FRENCH EVENTS LOCALISATION\n")
        content_en.append(" # ========================================================================\n")
        events_loc_en = {
            "ww1_france.1.t": "Agadir Crisis: The Panther in Agadir",
            "ww1_france.1.d": "On July 1, 1911, the German gunboat SMS Panther cast anchor off the Moroccan port of Agadir under the pretext of defending German commercial interests. Berlin seeks to challenge French paramountcy in Morocco.",
            "ww1_france.1.a": "Stand firm and consult our British allies",
            "ww1_france.1.b": "Negotiate a bilateral colonial compromise directly",
            "ww1_france.2.t": "British Support: The Mansion House Speech",
            "ww1_france.2.d": "Chancellor David Lloyd George delivers a resolute speech at Mansion House: Britain will not allow its allies to be treated as of no account when European peace is at stake.",
            "ww1_france.2.a": "The Entente Cordiale stands unbreakable",
            "ww1_france.3.t": "German Territorial Demands over Equatorial Africa",
            "ww1_france.3.d": "Berlin demands vast territories across French Congo and Oubangui-Chari in exchange for recognizing French claims in Morocco.",
            "ww1_france.3.a": "Accede to territory swap for recognition in Morocco",
            "ww1_france.3.b": "Reject all German blackmail!",
            "ww1_france.4.t": "The Franco-German Accord of 1911",
            "ww1_france.4.d": "After months of tense negotiations, France cedes a corridor in the Congo to German Cameroon in return for undisputed French protectorate rights over Morocco.",
            "ww1_france.4.a": "A bitter compromise, but peace is preserved",
            "ww1_france.10.t": "Treaty of Fez: The French Protectorate",
            "ww1_france.10.d": "Sultan Abdelhafid signs the Treaty of Fez establishing the French Protectorate in Morocco under General Hubert Lyautey.",
            "ww1_france.10.a": "France expands its civilizing mission",
            "ww1_france.20.t": "Passage of the Three-Year Conscription Law",
            "ww1_france.20.d": "The National Assembly votes to extend compulsory military service from two to three years, countering Germany's growing demographic dominance.",
            "ww1_france.20.a": "France stands ready to defend herself",
            "ww1_france.30.t": "Election of Raymond Poincaré as President",
            "ww1_france.30.d": "Conservative statesman Raymond Poincaré is elected President of the Third Republic, pledging unwavering resolve against German aggression.",
            "ww1_france.30.a": "A president of resolute resolve",
            "ww1_france.40.t": "The Assassination of Jean Jaurès",
            "ww1_france.40.d": "July 31, 1914: Nationalist fanatic Raoul Villain shoots socialist peace leader Jean Jaurès at Café du Croissant. France loses its greatest voice for peace on the eve of catastrophe.",
            "ww1_france.40.a": "Our last voice for peace has been silenced...",
            "ww1_france.41.t": "Order for General Mobilization: August 1, 1914",
            "ww1_france.41.d": "Church bells ring across every village in France. Over three million reservists take their rifles and march to the railway stations with flowers in their gun barrels.",
            "ww1_france.41.a": "L'Union Sacrée! Pour la Patrie!",
            "ww1_france.50.t": "Battle of the Frontiers: Carnage in Alsace-Lorraine",
            "ww1_france.50.d": "August 1914: Charging against fortified German machine guns in red trousers, French armies suffer catastrophic casualties. The offensive doctrine collapses under lead and shrapnel.",
            "ww1_france.50.a": "Order the fighting retreat to save the armies!",
            "ww1_france.51.t": "Plan XVII Triumphs: Alsace and Lorraine Liberated!",
            "ww1_france.51.d": "Against all odds, French armies rupture the German front and march into Strasbourg and Metz! The tricolor flies once more across the Rhine!",
            "ww1_france.51.a": "The lost provinces are redeemed!",
            "ww1_france.52.t": "Plan XVII Repulsed: The Frontier Stalemate",
            "ww1_france.52.d": "Heavy German counter-attacks halt the French advance with severe losses. Both sides dig in for a war of attrition.",
            "ww1_france.52.a": "Consolidate defensive lines along the Meuse",
            "ww1_france.61.t": "The Miracle of the Marne: Taxis Save Paris",
            "ww1_france.61.d": "General Gallieni requisitions 600 Parisian taxis to rush 6,000 reserves to the Ourcq. Joffre strikes von Kluck's exposed flank, halting the German march on Paris.",
            "ww1_france.61.a": "Paris is saved! The invader is thrown back!",
            "ww1_france.71.t": "The Furnace of Verdun: Falkenhayn Strikes",
            "ww1_france.71.d": "February 21, 1916: 1,400 German guns unleash hell on the Meuse forts to bleed France white. Verdun becomes the sacred altar of French defiance.",
            "ww1_france.71.a": "Ils ne passeront pas! Verdun will hold!",
            "ww1_france.81.t": "Catastrophe on the Chemin des Dames",
            "ww1_france.81.d": "April 1917: General Nivelle's promised rupture is pulverized on the limestone slopes of Craonne. Over 100,000 casualties in days break the army's endurance.",
            "ww1_france.81.a": "Relieve Nivelle immediately before total collapse!",
            "ww1_france.91.t": "The Poilus Mutinies of 1917",
            "ww1_france.91.d": "Sixty-eight divisions mutiny. The soldiers refuse suicidal butchery while swearing to defend their trenches against any German advance.",
            "ww1_france.91.a": "Appoint Pétain to restore discipline through compassion",
            "ww1_france.91.b": "Crush the mutineers with iron military tribunals!",
            "ww1_france.92.t": "Pétain Restores Hope to the Frontline",
            "ww1_france.92.d": "Guaranteed leaves, warm food, and elastic defense restore the morale of the French Army: 'I am waiting for the tanks and the Americans.'",
            "ww1_france.92.a": "Order and faith are restored",
            "ww1_france.101.t": "Georges Clemenceau: 'Je fais la guerre!'",
            "ww1_france.101.d": "November 1917: 'Le Tigre' takes power as Prime Minister, weeding out defeatists and inspiring the nation to victory: 'Domestic policy: I wage war. Foreign policy: I wage war. Always, I wage war!'",
            "ww1_france.101.a": "Victory at all costs!",
            "ww1_france.111.t": "The Yanks are Coming: First US Troops in France",
            "ww1_france.111.d": "General John J. Pershing arrives in Paris: 'Lafayette, we are here!' Doughboys begin rigorous training with French equipment.",
            "ww1_france.111.a": "Welcome to the sons of Washington!",
            "ww1_france.131.t": "The Armistice of Rethondes: Victory in the West!",
            "ww1_france.131.d": "November 11, 1918: In Marshal Foch's railway carriage in the Forest of Compiègne, Germany signs the unconditional armistice. The guns fall silent.",
            "ww1_france.131.a": "Vive la France! Vive la République!",
            "ww1_france.132.t": "The Sacred Return of Alsace-Lorraine",
            "ww1_france.132.d": "After 47 years of grief and yearning, the lost provinces of Alsace and Lorraine return home to the motherland. The nightmare of 1870 is finally erased.",
            "ww1_france.132.a": "The tricolor flies forever over Strasbourg and Metz!",
        }
        for ekey, etext in events_loc_en.items():
            content_en.append(f' {ekey}:0 "{etext}"\n')

        f_en.write("".join(content_en).encode("utf-8"))

    # Portuguese Localisation
    with open(pt_path, "wb") as f_pt:
        f_pt.write(codecs.BOM_UTF8)
        content_pt = []
        content_pt.append("l_braz_por:\n")
        content_pt.append(" # ========================================================================\n")
        content_pt.append(" # LOCALIZAÇÃO DA ÁRVORE DE FOCOS FRANCESA (PORTUGUÊS)\n")
        content_pt.append(" # ========================================================================\n")
        for f in FRENCH_FOCI:
            fid = f['id']
            title = f.get('title', fid).replace('"', "'")
            desc = f.get('desc', '').replace('"', "'")
            content_pt.append(f' {fid}:0 "{title}"\n')
            content_pt.append(f' {fid}_desc:0 "{desc}"\n')

        content_pt.append("\n # ========================================================================\n")
        content_pt.append(" # LOCALIZAÇÃO DOS ESPÍRITOS NACIONAIS FRANCESES\n")
        content_pt.append(" # ========================================================================\n")
        for iid, idef in FRENCH_IDEAS.items():
            name = idef.get('name', iid).replace('"', "'")
            desc = idef.get('desc', '').replace('"', "'")
            content_pt.append(f' {iid}:0 "{name}"\n')
            content_pt.append(f' {iid}_desc:0 "{desc}"\n')

        content_pt.append("\n # ========================================================================\n")
        content_pt.append(" # CATEGORIAS DE DECISÃO FRANCESAS\n")
        content_pt.append(" # ========================================================================\n")
        for cid, cdef in FRENCH_CATEGORIES.items():
            name = cdef.get('name', cid).replace('"', "'")
            desc = cdef.get('desc', '').replace('"', "'")
            content_pt.append(f' {cid}:0 "{name}"\n')
            content_pt.append(f' {cid}_desc:0 "{desc}"\n')

        content_pt.append("\n # ========================================================================\n")
        content_pt.append(" # DECISÕES E MISSÕES FRANCESAS\n")
        content_pt.append(" # ========================================================================\n")
        dec_locs_pt = {
            "FRA_execute_plan_xvii_mission": ("Executar Rompimento Operacional do Plano XVII", "A grande ofensiva de Joffre para recuperar as províncias perdidas da Alsácia e Lorena. Devemos capturar Estrasburgo e Colmar em 25 dias!"),
            "FRA_prep_first_army_belfort": ("Mobilizar 1º Exército em Belfort", "Concentrar corpos de infantaria e artilharia de montanha no desfiladeiro de Belfort para abrir caminho até Mulhouse."),
            "FRA_prep_second_army_morhange": ("Desdobrar 2º Exército em Nancy e Morhange", "O exército do General Castelnau deve romper as fortificações de fronteira alemãs e libertar Sarrebourg."),
            "FRA_prep_eastern_railway_priority": ("Prioridade Ferroviária na Linha do Leste", "Conceder prioridade máxima à Compagnie de l'Est para transportar 50 comboios de munição de artilharia por dia até o front da Lorena."),
            "FRA_requisition_parisian_taxis": ("Requisitar os Táxis Parisienses do Marne", "Ordenar à polícia que requisite 600 táxis Renault AG-1 em Paris para enviar reforços de infantaria com urgência ao Ourcq."),
            "FRA_deploy_gallieni_mobile_reserves": ("Lançar as Reservas Móveis de Gallieni", "Mobilizar a guarnição do Campo Entrincheirado de Paris para esmagar o flanco direito exposto de von Kluck."),
            "FRA_fortify_paris_camp_retranche": ("Fortificar o Campo Entrincheirado de Paris", "Cavar trincheiras e estender arame farpado no cinturão externo de Paris para resistir a qualquer cerco."),
            "FRA_activate_la_voie_sacree": ("Organizar o Comboio Logístico da Voie Sacrée", "Mobilizar milhares de caminhões Berliet na artéria Bar-le-Duc para fornecer 50.000 toneladas de munição por semana a Verdun."),
            "FRA_rotate_frontline_divisions_noria": ("Executar a Rotação de Nória de Pétain", "Fazer a rotação das divisões exaustas para fora do caldeirão de Verdun após 10 dias, preservando o moral e o efetivo."),
            "FRA_concentrate_heavy_artillery_meuse": ("Concentrar Artilharia Pesada no Mosa", "Desdobrar centenas de obuseiros Schneider de 155mm para silenciar as baterias alemãs no Homem Morto."),
            "FRA_petain_welfare_and_leave_reform": ("Reforma de Bem-Estar e Licenças de Pétain", "Garantir licenças para casa e centros de descanso para aliviar o desespero dos soldados na frente de batalha."),
            "FRA_improve_trench_soup_and_wine": ("Melhorar a Sopa Quente e Vinho ('Le Pinard')", "Garantir que marmitas térmicas cheguem às trincheiras com comida quente e generosas rações de vinho."),
            "FRA_measured_justice_and_pardons": ("Protocolos de Justiça Medida e Clemência", "Perdoar a grande maioria dos recrutas enganados, executando apenas os líderes rebeldes para restaurar a confiança no comando."),
            "FRA_draconian_decimation_repression": ("Decimação Draconiana e Execuções Sumárias", "Aplicar o código militar com mão de ferro para fuzilar amotinados pour encourager les autres. Alto risco de greve geral!"),
            "FRA_issue_national_defense_bonds": ("Emitir Títulos da Defesa Nacional", "'Pela França, Entreguem Seu Ouro!' Mobilizar as reservas populares para financiar a guerra sem gerar hiperinflação."),
            "FRA_expand_munitionnettes_workforce": ("Mobilizar a Força de Trabalho das 'Munitionnettes'", "Recrutar centenas de milhares de mulheres patriotas para fabricar projéteis de 75mm nas fábricas de armamento de Paris."),
            "FRA_equip_doughboys_with_french_equipment": ("Equipar os Doughboys com Armamento Francês", "Fornecer às divisões americanas recém-chegadas canhões de 75mm, fuzis-metralhadoras Chauchat e tanques leves Renault FT."),
        }
        for dkey, (dtitle, ddesc) in dec_locs_pt.items():
            content_pt.append(f' {dkey}:0 "{dtitle}"\n')
            content_pt.append(f' {dkey}_desc:0 "{ddesc}"\n')

        content_pt.append("\n # ========================================================================\n")
        content_pt.append(" # EVENTOS FRANCESES (PORTUGUÊS)\n")
        content_pt.append(" # ========================================================================\n")
        events_loc_pt = {
            "ww1_france.1.t": "Crise de Agadir: O Panther em Agadir",
            "ww1_france.1.d": "Em 1 de julho de 1911, a canhoneira alemã SMS Panther ancorou no porto marroquino de Agadir sob o pretexto de defender interesses comerciais alemães. Berlim desafia a supremacia francesa no Marrocos.",
            "ww1_france.1.a": "Manter firmeza e consultar os aliados britânicos",
            "ww1_france.1.b": "Negociar diretamente um compromisso colonial bilateral",
            "ww1_france.2.t": "Apoio Britânico: O Discurso de Mansion House",
            "ww1_france.2.d": "O Chanceler David Lloyd George profere um discurso resoluto em Mansion House: a Grã-Bretanha não permitirá que seus aliados sejam tratados como insignificantes quando a paz europeia estiver em jogo.",
            "ww1_france.2.a": "A Entente Cordiale permanece inabalável",
            "ww1_france.3.t": "Demandas Territoriais Alemãs sobre a África Equatorial",
            "ww1_france.3.d": "Berlim exige vastos territórios no Congo Francês e em Oubangui-Chari em troca de reconhecer as reivindicações francesas no Marrocos.",
            "ww1_france.3.a": "Aceitar troca territorial em troca do reconhecimento no Marrocos",
            "ww1_france.3.b": "Rejeitar toda chantagem alemã!",
            "ww1_france.4.t": "O Acordo Franco-Alemão de 1911",
            "ww1_france.4.d": "Após meses de negociações tensas, a França cede um corredor no Congo ao Camarões Alemão em troca de direitos incontestados de protetorado sobre o Marrocos.",
            "ww1_france.4.a": "Um compromisso amargo, mas a paz é preservada",
            "ww1_france.10.t": "Tratado de Fez: O Protetorado Francês",
            "ww1_france.10.d": "O Sultão Abdelhafid assina o Tratado de Fez estabelecendo o Protetorado Francês no Marrocos sob a administração do General Hubert Lyautey.",
            "ww1_france.10.a": "A França expande sua missão civilizadora",
            "ww1_france.20.t": "Aprovação da Lei dos Três Anos de Serviço Militar",
            "ww1_france.20.d": "A Assembleia Nacional vota para estender o serviço militar obrigatório de dois para três anos, equilibrando o crescimento demográfico da Alemanha.",
            "ww1_france.20.a": "A França está pronta para se defender",
            "ww1_france.30.t": "Eleição de Raymond Poincaré para a Presidência",
            "ww1_france.30.d": "O estadista conservador Raymond Poincaré é eleito Presidente da Terceira República, prometendo firmeza inabalável contra a agressão alemã.",
            "ww1_france.30.a": "Um presidente de firme determinação",
            "ww1_france.40.t": "O Assassinato de Jean Jaurès",
            "ww1_france.40.d": "31 de julho de 1914: O fanático nacionalista Raoul Villain atira no líder socialista e pacifista Jean Jaurès no Café du Croissant. A França perde sua maior voz pela paz às vésperas do abismo.",
            "ww1_france.40.a": "Nossa última voz pela paz foi silenciada...",
            "ww1_france.41.t": "Ordem de Mobilização Geral: 1 de Agosto de 1914",
            "ww1_france.41.d": "Os sinos das igrejas dobram por todas as aldeias da França. Mais de três milhões de reservistas pegam seus fuzis e marcham para as estações de trem.",
            "ww1_france.41.a": "L'Union Sacrée! Pela Pátria!",
            "ww1_france.50.t": "Batalha das Fronteiras: Carnificina na Alsácia-Lorena",
            "ww1_france.50.d": "Agosto de 1914: Avançando contra metralhadoras alemãs entrincheiradas de calças vermelhas, os exércitos franceses sofrem perdas estarrecedoras. A doutrina da ofensiva desmorona.",
            "ww1_france.50.a": "Ordenar o recuo de combate para salvar os exércitos!",
            "ww1_france.51.t": "Vitória do Plano XVII: Alsácia e Lorena Libertadas!",
            "ww1_france.51.d": "Contra todas as probabilidades, os exércitos franceses rompem o front alemão e marcham em Estrasburgo e Metz! O tricolor volta a tremular sobre o Reno!",
            "ww1_france.51.a": "As províncias perdidas foram redimidas!",
            "ww1_france.52.t": "Plano XVII Repelido: O Impasse da Fronteira",
            "ww1_france.52.d": "Fortes contra-ataques alemães contêm o avanço francês com pesadas baixas. Ambos os lados cavam trincheiras para uma guerra de atrito.",
            "ww1_france.52.a": "Consolidar linhas defensivas ao longo do Mosa",
            "ww1_france.61.t": "O Milagre do Marne: Os Táxis Salvam Paris",
            "ww1_france.61.d": "O General Gallieni requisita 600 táxis parisienses para transportar 6.000 soldados de infantaria ao Ourcq. Joffre contra-ataca o flanco de von Kluck, salvando a capital.",
            "ww1_france.61.a": "Paris está salva! O invasor foi repelido!",
            "ww1_france.71.t": "A Fornalha de Verdun: O Ataque de Falkenhayn",
            "ww1_france.71.d": "21 de fevereiro de 1916: 1.400 canhões alemães despejam fogo sobre os fortes do Mosa para sangrar a França até a morte. Verdun se torna o altar do sacrifício francês.",
            "ww1_france.71.a": "Ils ne passeront pas! Verdun resistirá!",
            "ww1_france.81.t": "Catástrofe no Chemin des Dames",
            "ww1_france.81.d": "Abril de 1917: A grande ofensiva de ruptura do General Robert Nivelle é pulverizada nas encostas rochosas de Craonne. Mais de 100.000 baixas em poucos dias quebram o limite das tropas.",
            "ww1_france.81.a": "Exonerar Nivelle imediatamente antes do colapso total!",
            "ww1_france.91.t": "Os Motins dos Poilus de 1917",
            "ww1_france.91.d": "Sessenta e oito divisões se amotinam. Os soldados recusam investidas suicidas, prometendo contudo defender as trincheiras contra qualquer ataque alemão.",
            "ww1_france.91.a": "Nomear Pétain para restaurar a disciplina através da compaixão",
            "ww1_france.91.b": "Esmagar os amotinados com tribunais militares implacáveis!",
            "ww1_france.92.t": "Pétain Restaura a Esperança no Front",
            "ww1_france.92.d": "Licenças garantidas, refeições quentes e defesa elástica restauram a moral do Exército Francês: 'Espero pelos tanques e pelos americanos.'",
            "ww1_france.92.a": "A ordem e a fé estão restauradas",
            "ww1_france.101.t": "Georges Clemenceau: 'Je fais la guerre!'",
            "ww1_france.101.d": "Novembro de 1917: 'O Tigre' assume como Primeiro-Ministro, expurgando derrotistas e inspirando a nação: 'Política interna: eu faço a guerra. Política externa: eu faço a guerra. Sempre, eu faço a guerra!'",
            "ww1_france.101.a": "Vitória a qualquer custo!",
            "ww1_france.111.t": "Os Americanos Chegam: Primeiras Tropas dos EUA na França",
            "ww1_france.111.d": "O General John J. Pershing desembarca em Paris: 'Lafayette, nous voilà!' As tropas americanas iniciam treinamento rigoroso com equipamento francês.",
            "ww1_france.111.a": "Bem-vindos aos filhos de Washington!",
            "ww1_france.131.t": "O Armistício de Rethondes: Vitória no Ocidente!",
            "ww1_france.131.d": "11 de novembro de 1918: No vagão do Marechal Foch na floresta de Compiègne, a Alemanha assina os termos do armistício incondicional. As armas silenciam.",
            "ww1_france.131.a": "Viva a França! Viva a República!",
            "ww1_france.132.t": "O Retorno Sagrado da Alsácia-Lorena",
            "ww1_france.132.d": "Após 47 anos de luto e espera, as províncias da Alsácia e Lorena retornam à mãe-pátria. A mancha de 1870 está finalmente apagada.",
            "ww1_france.132.a": "O tricolor tremula para sempre sobre Estrasburgo e Metz!",
        }
        for ekey, etext in events_loc_pt.items():
            content_pt.append(f' {ekey}:0 "{etext}"\n')

        f_pt.write("".join(content_pt).encode("utf-8"))

    print("Localisation generated successfully for English and Brazilian Portuguese.")

if __name__ == "__main__":
    generate_focus_tree()
    generate_ideas()
    generate_decisions()
    generate_events()
    generate_localisation()

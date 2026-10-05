import os
import sys
import codecs

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from france_builder.data_foci import FRENCH_FOCI
from france_builder.data_ideas import FRENCH_IDEAS
from france_builder.data_decisions import FRENCH_CATEGORIES, FRENCH_DECISIONS_CODE
from france_builder.data_events import FRENCH_EVENTS_CODE
from france_builder.data_event_loc import EVENTS_LOC_EN, EVENTS_LOC_PT

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
        out.write("\tcontinuous_focus_position = { x = 40 y = 4300 }\n\n")

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
        for ekey, etext in EVENTS_LOC_EN.items():
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
        for ekey, etext in EVENTS_LOC_PT.items():
            content_pt.append(f' {ekey}:0 "{etext}"\n')

        f_pt.write("".join(content_pt).encode("utf-8"))

    print("Localisation generated successfully for English and Brazilian Portuguese.")

if __name__ == "__main__":
    generate_focus_tree()
    generate_ideas()
    generate_decisions()
    generate_events()
    generate_localisation()

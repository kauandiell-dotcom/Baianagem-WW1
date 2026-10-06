"""Import country-owned art from installed Workshop copies; donors remain read-only.

Exact paths, no fuzzy substitution or image generation. Contact sheets are review aids.
Bindings and decoded hashes preserve provenance independently of shared manifests.
"""
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
import hashlib,json,sys
from build_ww1_austria_hungary import ROOT,FOCI

WORKSHOP=Path('E:/SteamLibrary/steamapps/workshop/content/394360')
T='3365515312';K='2076426030';E='2716194283'

def sources(mod,text):
    return [(mod,line.strip()) for line in text.strip().splitlines() if line.strip()]

politics=sources(K,"""
AUS_habsburg_throne.png
AUS_ausgleich.png
AUS_1867_right.png
AUS_Office_Objectivity.png
AUS_early_ausgleich.png
AUS_istvan_tisza.png
AUS_Habsburg_Compromises.png
AUS_common_army.png
AUS_Careful_Craft_Compromise.png
AUS_habsburg_law.png
AUS_cultural_associations.png
AUS_Cabinet_Lander.png
AUS_illyrian_question.png
AUS_south_slavs.png
AUS_sarajevo_agreement.png
AUS_magyar_conservatives.png
AUS_onethirds_agreement.png
AUS_inter_imperial_trade.png
AUS_cultural_exchange.png
AUS_communities_of_interaction.png
AUS_danubian_federation.png
AUS_All_Angles_Federal_Reconstitution.png
AUS_Austria_Individuality_Acceptance.png
AUS_federal_council.png
AUS_Cultural_Economic_Excellence.png
AUS_these_united_states.png
AUS_reform_common_army.png
AUS_Federalism_Survives.png
AUS_bohemian_dap.png
AUS_Bohemian_Detente.png
AUS_Autonomy_Lander.png
AUS_broad_traditional_communion.png
AUS_Tithes_Real_Education.png
AUS_cultural_conservatism.png
AUS_Reform_Imperial_Lander.png
AUS_Ensure_Integrity_Economy_Culture.png
AUS_community_to_stand.png
AUS_south_slavic_revolts.png
AUS_civilian_oversight.png
AUS_judiciary.png
""")
# Exact country assets absent in this donor are intentionally explicit equivalents.
politics[38]=(E,'kaiserreich/generic_civilian_oversight.dds')

economy=sources(K,"""
AUS_economic_school.png
AUS_nonmarxist_economics.png
AUS_methodology.png
AUS_deal_companies.png
AUS_skoda.png
AUS_steel_kernel.png
AUS_bohler_steel.png
AUS_steyr.png
AUS_military_economic.png
AUS_merge_constituent_companies.png
AUS_agriculture.png
AUS_recovery_food.png
AUS_agrarian_means.png
AUS_agrarian_soldiers_focus.png
AUS_Farm_Factory_Fraternity.png
AUS_agrarian_icon.png
AUS_kfjb_rail.png
AUS_lokomotivfabrik_steg.png
AUS_railwaymen_support.png
AUS_Repair_Danubian_Highways.png
AUS_Advertise_To_Metal_Rail_Unions.png
AUS_Ascertain_Course_Tomorrows_Tracks.png
AUS_Catastrophe_Insurances.png
AUS_Recivilizing_Desolation.png
AUS_corp_workers_representative.png
AUS_bring_together_classes.png
AUS_agrarian_means_2.png
AUS_conservative_laborer.png
AUS_berlin_stock_market.png
AUS_honest_modest.png
AUS_economic_school_2.png
AUS_stately_modesty.png
AUS_Leash_Wily_Hands_Of_Capitalism.png
AUS_Kickstart_Broken_Banks.png
AUS_vienna_university.png
AUS_new_school.png
AUS_danubian_waterwheel.png
AUS_galicia_oil.png
AUS_kapsch_sohne.png
AUS_Reconstruct_Private_Business.png
""")
economy[4]=(E,'NW/z_goal_tatra_skoda.dds')
economy[7]=(K,'AUS_hirtenberg_ammo.png')
economy[30]=(T,'generic_finance.png')

army=sources(K,"""
AUS_armeeoberkommando.png
AUS_kriegsschule.png
AUS_Unbyzantify_Gemeinsamen_Armee.png
AUS_reconstructive_mobilization.png
AUS_crown_jewel_armed_forces.png
AUS_mannlicher.png
AUS_all_austrian_army.png
AUS_hoch_und_deutschmeister.png
AUS_kickstart_military.png
AUS_hirtenberg_ammo.png
AUS_Glorify_Styrian_Courage.png
AUS_kaisertreuen.png
AUS_tactical_flexibility.png
AUS_militargrenze.png
AUS_field_factory.png
AUS_hotzendorf_army.png
AUS_great_soldier.png
AUS_gebirgstruppe.png
AUS_aufklarungstruppe.png
AUS_Adorn_Decisive_Gilded_Gauntlet.png
AUS_Steel_Backed_Benevolence.png
AUS_Intelligent_Moderations.png
AUS_Support_Steidles_Concrete_Politicking.png
AUS_Ancestor_Ice_Kings.png
AUS_kaiserschuetzen.png
AUS_Legacy_Kaiserjagers.png
AUS_Man_Minded_Infrastructure_Repaving.png
AUS_Kriegsveteranenfursorge.png
AUS_graf_and_stift.png
AUS_lion_isonzo.png
AUS_Glorify_Styrian_Courage_alt.png
AUS_raumverteidigung.png
AUS_serbi_dio_laustriaco_regno.png
AUS_boryslaw_oil.png
AUS_fifth_army.png
AUS_hotzendorf.png
AUS_kaisers_men_of_honor.png
AUS_kapsch_sohne.png
AUS_charge_of_faithful.png
AUS_Lessons_Great_Europeans.png
AUS_poor_military.png
AUS_luftfahrtruppen.png
AUS_fliegerkompanie_41j.png
AUS_lohner.png
AUS_airforce.png
AUS_hansa_brandenburg.png
AUS_floridsdorf.png
AUS_seefliegerkorps.png
AUS_Realschule_Reformation.png
AUS_Inductionist_Chassis.png
""")
# Military/political period-neutral symbols reviewed in their native compositions.
for i,source in {
5:(T,'AUH/AUS_common_army.png'),9:(T,'focus_generic_munitions.png'),
14:(T,'focus_medical_corps.png'),15:(T,'generic_mountain_artillery.png'),
16:(T,'AUH/the_army_question.png'),19:(T,'focus_sichuan_artillery.png'),
22:(E,'kaiserreich/generic_radio_equipment.dds'),25:(T,'generic_mountain_warfare.png'),
28:(E,'kaiserreich/generic_support_equipment.dds'),
31:(T,'focus_fortification.png'),36:(E,'kaiserreich/generic_army_cooperation.dds'),
37:(E,'kaiserreich/generic_secret_documents.dds'),38:(T,'generic_cavalry.png'),
39:(E,'kaiserreich/generic_army_high_command.dds'),44:(T,'goal_generic_air_fighter.dds'),
47:(T,'focus_generic_seaplane.png'),49:(T,'focus_generic_education_tgwr.png')}.items():army[i]=source

diplomacy=sources(K,"""
AUS_Economic_Foreign_Policy.png
AUS_agents_agencies.png
AUS_Overtly_Avoidance_Neighborly_Ire.png
AUS_Legacy_Grandfather_Franz_Josef.png
AUS_Reappraise_Our_Political_Standing.png
AUS_Network_In_Germany.png
AUS_GER_military_goods.png
AUS_Economic_Foreign_Policy_2.png
AUS_four_old_friends.png
AUS_indivisible_inseparable.png
AUS_Propose_Germanic_Customs_Union.png
AUS_placate_neighbor.png
AUS_Arrest_Anti_Habsburg_Unpatriotic_Sentiments.png
AUS_Repair_Danubian_Highways_2.png
AUS_good_neighbor_albania.png
AUS_avoid_weltkrieg.png
AUS_anti_war.png
AUS_handshake.png
AUS_cultural_political_union.png
AUS_anchors_aweigh.png
AUS_tyrolit.png
AUS_belligerent_neighbors.png
AUS_Preserve_Habsburg_Institutions_Governance.png
AUS_Neutralize_Romania.png
AUS_field_over_factory.png
AUS_south_german_industry.png
AUS_volga_danube.png
AUS_homeland_protected.png
AUS_aid_post_habsburg.png
AUS_karls_vision.png
AUS_peace_in_our_time.png
AUS_Great_Peace_Great_Empire.png
AUS_avoid_weltkrieg_2.png
AUS_Blank_Check_Investigations_Rogue_Politickers.png
AUS_Foster_Cooperation_Along_Danube.png
""")
for i,source in {
7:(T,'focus_german_equipment.png'),10:(T,'focus_deal_with_german_empire.png'),
11:(T,'focus_deal_with_serbia.png'),13:(T,'AUH/pacify_bosnian_terrorism.png'),
15:(T,'focus_generic_befriend_montenegro.png'),17:(E,'kaiserreich/generic_deals.dds'),
18:(T,'AUH/suppress_italy.png'),23:(T,'focus_deal_with_romania.png'),
26:(T,'focus_deal_with_russia.png'),30:(E,'kaiserreich/generic_government_deals.dds'),
32:(E,'focus_generic_diplomatic_treaty.dds')}.items():diplomacy[i]=source

navy=sources(T,"""
focus_naval_support.png
generic_navy_act.png
generic_naval_ship.png
focus_battleship_renewed.png
focus_otto_naval_train.png
focus_battlefleet.png
focus_battleship_production.png
generic_naval_ship_transfer.png
generic_shipyard.png
generic_expand_the_naval_industry.png
focus_generic_seaplane_tender.png
focus_GER_navy_ww1.png
generic_titantic.png
focus_generic_zeppelin.png
AUH/industrial_expansion.png
focus_forest_railway.png
generic_news.png
goal_generic_air_fighter2.dds
focus_generic_money_deal.png
Generic_Develop_Rail_Network.png
""")
for i,source in {0:(K,'AUS_kriegsmarine.png'),4:(E,'kaiserreich/generic_naval_academy.dds'),
5:(E,'kaiserreich/generic_naval_command.dds'),7:(K,'AUS_bless_winds.png'),
10:(E,'kaiserreich/generic_coastal_navy.dds'),11:(E,'kaiserreich/generic_naval_submarine2.dds'),
12:(E,'kaiserreich/generic_naval_industry.dds'),13:(E,'kaiserreich/generic_design_equipment_standards.dds'),
14:(E,'kaiserreich/generic_naval_base.dds'),15:(E,'kaiserreich/generic_coastal_navy2.dds'),
16:(T,'focus_generic_seaplane_tender.png'),17:(E,'kaiserreich/generic_sea_and_air.dds'),
18:(E,'kaiserreich/generic_transports.dds')}.items():navy[i]=source

postwar=sources(K,"""
AUS_aggressive_reconstruction.png
AUS_veteran_pensions.png
AUS_Relocate_Restore_Hampered_Industries.png
AUS_Call_Off_Volksmilizen.png
AUS_Kriegsveteranenfursorge_2.png
AUS_combat_unemployment.png
AUS_burgertum.png
AUS_repair_pride.png
AUS_Reconstruct_Private_Business_2.png
AUS_Cultural_Capital_Germans.png
AUS_nonmarxist_economics_2.png
AUS_Replace_Constitution.png
AUS_Let_Ballot_Speak_For_Me.png
AUS_mend_schisms.png
AUS_Grossosterreich.png
""")
for i,source in {4:(E,'kaiserreich/generic_recovery.dds'),8:(E,'kaiserreich/generic_build_housing.dds'),
10:(E,'kaiserreich/generic_debt_negotiations.dds'),11:(K,'AUS_Rewrite_Catastrophe_Constitution.png')}.items():postwar[i]=source

groups=[politics,economy,army,diplomacy,navy,postwar]
assert [len(g) for g in groups]==[40,40,50,35,20,15]

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def decoded(image):return hashlib.sha256(image.convert('RGBA').tobytes()).hexdigest()

def main():
    # Revisions after contact-sheet review use exact per-focus overrides.
    overrides_path=ROOT/'docs/auh_visual_overrides.json'
    overrides=json.loads(overrides_path.read_text(encoding='utf-8')) if overrides_path.exists() else {}
    selected=[];missing=[]
    for focus,(mod,rel) in zip(FOCI,[x for g in groups for x in g]):
        if focus['id'] in overrides:mod,rel=overrides[focus['id']]
        path=WORKSHOP/mod/'gfx/interface/goals'/rel
        if not path.is_file():missing.append((focus['id'],str(path)))
        selected.append((focus['id'],path,mod,rel))
    if missing:
        print(json.dumps({'missing':missing},ensure_ascii=False,indent=2));return 1
    records=[];sprites=['spriteTypes = {'];seen={};duplicates=[]
    for fid,path,mod,rel in selected:
        image=Image.open(path).convert('RGBA');px=decoded(image)
        if px in seen:duplicates.append((fid,seen[px]))
        seen[px]=fid
        dest=ROOT/'gfx/interface/goals/ww1_auh'/f'{fid}.dds';dest.parent.mkdir(parents=True,exist_ok=True)
        # Fit preserves the full icon and its transparency; no distortion/recolouring.
        image=ImageOps.contain(image,(82,82),Image.Resampling.LANCZOS)
        out=Image.new('RGBA',(82,82));out.alpha_composite(image,((82-image.width)//2,(82-image.height)//2));out.save(dest)
        texture=dest.relative_to(ROOT).as_posix()
        name='GFX_focus_'+fid
        sprites.append(f' spriteType = {{ name = "{name}" texturefile = "{texture}" }}')
        sprites.append(f' spriteType = {{ name = "{name}_shine" texturefile = "{texture}" effectFile = "gfx/FX/buttonstate.lua" animation = {{ animationmaskfile = "{texture}" animationtexturefile = "gfx/interface/goals/shine_overlay.dds" animationrotation = -90.0 animationlooping = no animationtime = .75 animationdelay = 0.0 animationblendmode = "add" animationtype = "scrolling" animationrotationoffset = {{ x = 0.0 y = 0.0 }} animationtexturescale = {{ x = 1.0 y = 1.0 }} }} }}')
        records.append(dict(focus=fid,donor_id=mod,source_relative='gfx/interface/goals/'+rel,source_sha256=digest(path),source_rgba_sha256=px,texture=texture))
    families=['budget','languages','arsenals','logistics','staff','council','rationing','labour','diplomacy','fleet','repair','veterans','administration','cabinet','shifts','harvest','rotation','exhausted','food','debt','operation','credit']
    refs=['AUS_ausgleich.png','AUS_Unbyzantify_Gemeinsamen_Armee.png','AUS_bohler_steel.png','AUS_lokomotivfabrik_steg.png','AUS_armeeoberkommando.png','generic_council.png','AUS_agrarian_icon.png','AUS_bring_together_classes.png','AUS_Economic_Foreign_Policy.png','AUS_kriegsmarine.png','AUS_anchors_aweigh.png','AUS_veteran_pensions.png','AUS_Office_Objectivity.png','AUS_Cabinet_Lander.png','AUS_raised_working_week.png','AUS_agrarian_soldiers_focus.png','AUS_kaisers_men_of_honor.png','AUS_poor_military.png','AUS_recovery_food.png','AUS_berlin_stock_market.png','AUS_fifth_army.png','generic_balanced_budget.png']
    for family,rel in zip(families,refs):
        src=WORKSHOP/K/'gfx/interface/goals'/rel
        if not src.is_file():raise FileNotFoundError(src)
        dest=ROOT/'gfx/interface/ideas/ww1_auh'/f'{family}.dds';dest.parent.mkdir(parents=True,exist_ok=True)
        im=ImageOps.contain(Image.open(src).convert('RGBA'),(64,64),Image.Resampling.LANCZOS)
        out=Image.new('RGBA',(64,64));out.alpha_composite(im,((64-im.width)//2,(64-im.height)//2));out.save(dest)
        sprites.append(f' spriteType = {{ name = "GFX_idea_AUH_ww1_{family}" texturefile = "{dest.relative_to(ROOT).as_posix()}" }}')
    for cat,family in [('crown','council'),('economy','budget'),('projects','logistics'),('military','staff'),('diplomacy','diplomacy')]:
        sprites.append(f' spriteType = {{ name = "GFX_decision_AUH_ww1_{cat}" texturefile = "gfx/interface/ideas/ww1_auh/{family}.dds" }}')
    epics={'council':'AUS/report_event_auh_imperial_council.png','karl':'AUS/report_event_karl_i_coronation.png','naval':'AUS/ww1_austria_1.png','reconstruction':'AUS/news_event_auh_trialism.png','food':'AUS/news_event_auh_collapse.png'}
    for key,rel in epics.items():
        src=WORKSHOP/T/'gfx/event_pictures'/rel
        dest=ROOT/'gfx/event_pictures/ww1_auh'/f'{key}.dds';dest.parent.mkdir(parents=True,exist_ok=True)
        ImageOps.fit(Image.open(src).convert('RGBA'),(450,250),Image.Resampling.LANCZOS).save(dest)
        sprites.append(f' spriteType = {{ name = "GFX_event_AUH_ww1_{key}" texturefile = "{dest.relative_to(ROOT).as_posix()}" }}')
    tisza='gfx/interface/ideas/HUN/idea_HUN_Istvan_Tisza.png'
    sprites.append(f' spriteType = {{ name = "GFX_idea_AUH_ww1_tisza" texturefile = "{tisza}" }}')
    sprites.append('}')
    (ROOT/'interface/ww1_austria_hungary_assets.gfx').write_text('\n'.join(sprites)+'\n',encoding='utf-8')
    (ROOT/'docs/auh_visual_bindings.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for page in range(6):
        batch=records[page*36:(page+1)*36];sheet=Image.new('RGB',(1080,1080),(30,32,36));d=ImageDraw.Draw(sheet)
        for i,r in enumerate(batch):
            x=(i%6)*180;y=(i//6)*180
            im=Image.open(ROOT/r['texture']).convert('RGBA');sheet.paste(im,(x+49,y+15),im)
            label=r['focus'].removeprefix('AUH_ww1_');d.text((x+8,y+107),str(page*36+i+1)+' '+label[:23],fill='white')
            d.text((x+8,y+125),r['source_relative'].split('/')[-1][:24],fill=(185,190,200))
        sheet.save(ROOT/f'docs/auh_art_review_{page+1}.png')
    print(json.dumps({'focus_sprites':len(records),'exact_duplicate_art':duplicates,'ideas':len(families),'review_sheets':6},ensure_ascii=False));return 0

if __name__=='__main__':sys.exit(main())

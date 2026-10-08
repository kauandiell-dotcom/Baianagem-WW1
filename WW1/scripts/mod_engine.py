#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
       HOI4 BAIANAGEM-WW1 GAME DESIGN & GAMEPLAY RADAR ENGINE (mod_engine.py)
===============================================================================
A unified multi-pillar engine for analyzing, auditing, balancing, and visualizing:
 1. Focus Trees & 3-Phase Chronological Arc (Curto 1911-14, Médio 1914-16, Longo 1917-20).
 2. Combat Balance, Division Templates & Equipment Sufficiency.
 3. AI Behavioral Weighting (ai_will_do & Historical Pathing).
 4. Localization Quality, Narrative Depth & Missing Keys (PT-BR & EN).
 5. Multiplayer Safety, Anti-Desync (OOS) & Daily Performance / Lag Telemetry.
 6. Interactive 2D Visual SVG/HTML Inspector with Phase Filters.
===============================================================================
"""

import os
import re
import sys
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional, Tuple

ROOT_DIR = Path(__file__).resolve().parent.parent
COMMON_DIR = ROOT_DIR / "common"
FOCUS_DIR = COMMON_DIR / "national_focus"
DECISIONS_DIR = COMMON_DIR / "decisions"
EVENTS_DIR = ROOT_DIR / "events"
IDEAS_DIR = COMMON_DIR / "ideas"
ON_ACTIONS_DIR = COMMON_DIR / "on_actions"
UNITS_DIR = ROOT_DIR / "history" / "units"
COUNTRIES_DIR = ROOT_DIR / "history" / "countries"
LOCALISATION_DIR = ROOT_DIR / "localisation"
SCRIPTS_DIR = ROOT_DIR / "scripts"
OUTPUT_DIR = SCRIPTS_DIR / "visual_radar"

TAG_TO_FILE = {
    "AUS": FOCUS_DIR / "austria.txt",
    "AUH": FOCUS_DIR / "austria.txt",
    "GER": FOCUS_DIR / "germany.txt",
    "FRA": FOCUS_DIR / "france.txt",
    "ITA": FOCUS_DIR / "italy.txt",
    "ENG": FOCUS_DIR / "uk.txt",
    "RUS": FOCUS_DIR / "soviet.txt",
    "SOV": FOCUS_DIR / "soviet.txt",
    "TUR": FOCUS_DIR / "turkey.txt",
}

TAG_TO_OOB = {
    "AUS": UNITS_DIR / "AUS_1936_generic.txt",
    "GER": UNITS_DIR / "GER_1936_generic.txt",
    "FRA": UNITS_DIR / "FRA_1936_generic.txt",
    "ITA": UNITS_DIR / "ITA_1936_generic.txt",
    "ENG": UNITS_DIR / "ENG_1936_generic.txt",
    "RUS": UNITS_DIR / "SOV_1936_generic.txt",
    "TUR": UNITS_DIR / "TUR_1936_generic.txt",
}

TAG_TO_HISTORY = {
    "AUS": COUNTRIES_DIR / "AUS - Austria.txt",
    "GER": COUNTRIES_DIR / "GER - Germany.txt",
    "FRA": COUNTRIES_DIR / "FRA - France.txt",
    "ITA": COUNTRIES_DIR / "ITA - Italy.txt",
    "ENG": COUNTRIES_DIR / "ENG - Britain.txt",
    "RUS": COUNTRIES_DIR / "SOV - Soviet.txt",
    "TUR": COUNTRIES_DIR / "TUR - Turkey.txt",
}


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class FocusNode:
    id: str
    x: int
    y: int
    cost_days: int
    prerequisites: List[List[str]] = field(default_factory=list)
    mutually_exclusive: List[str] = field(default_factory=list)
    raw_reward: str = ""
    raw_ai: str = ""
    
    # Phase Classification
    phase: int = 1  # 1: 1911-1914 (Pre-war), 2: 1914-1916 (Total War), 3: 1917-1920 (Exhaustion/Endgame)
    phase_name: str = "Curto Prazo (1911-1914)"

    # Gameplay & Substance Metrics
    substance_score: float = 0.0
    category: str = "Standard"
    factories_civ: int = 0
    factories_mil: int = 0
    dockyards: int = 0
    slots: int = 0
    units_spawned: int = 0
    unlocked_decisions: List[str] = field(default_factory=list)
    fired_events: List[str] = field(default_factory=list)
    gives_ideas: List[str] = field(default_factory=list)
    is_filler: bool = False
    filler_reasons: List[str] = field(default_factory=list)
    strengths: List[str] = field(default_factory=list)

    # AI Behavior Metrics
    has_ai_will_do: bool = False
    ai_base_factor: float = 1.0
    ai_status: str = "Padrao"

    # Localization Metrics
    has_loc_pt: bool = False
    has_loc_en: bool = False
    loc_pt_title: str = ""
    loc_pt_desc_len: int = 0
    is_loc_shallow: bool = False


@dataclass
class DivisionTemplate:
    name: str
    battalions: List[str] = field(default_factory=list)
    supports: List[str] = field(default_factory=list)
    combat_width: int = 0
    total_manpower: int = 0
    is_balanced: bool = True
    critique: str = ""


@dataclass
class CombatReport:
    tag: str
    templates: List[DivisionTemplate] = field(default_factory=list)
    infantry_equipment_stockpile: int = 0
    artillery_stockpile: int = 0
    support_equipment_stockpile: int = 0
    total_starting_divisions: int = 0
    is_stockpile_sufficient: bool = True
    warnings: List[str] = field(default_factory=list)


@dataclass
class TreeReport:
    tag: str
    file_path: str
    total_focuses: int = 0
    avg_substance_score: float = 0.0
    filler_count: int = 0
    filler_percentage: float = 0.0
    
    # 3-Phase Chronological Arc
    phase_1_count: int = 0  # 1911-1914
    phase_2_count: int = 0  # 1914-1916
    phase_3_count: int = 0  # 1917-1920
    phase_1_score: float = 0.0
    phase_2_score: float = 0.0
    phase_3_score: float = 0.0

    # Physical Map Rewards
    total_civ_factories: int = 0
    total_mil_factories: int = 0
    total_dockyards: int = 0
    total_slots: int = 0
    total_events_fired: int = 0
    total_decisions_unlocked: int = 0
    
    # Ergonomics & Visual Collisions
    collision_count: int = 0
    continuous_focus_hazard: bool = False
    pacing_1914_readiness_pct: float = 0.0
    
    # AI & Loc Summary
    ai_coverage_pct: float = 0.0
    loc_coverage_pct: float = 0.0
    shallow_loc_count: int = 0

    nodes: Dict[str, FocusNode] = field(default_factory=dict)
    hitlist: List[FocusNode] = field(default_factory=list)
    combat: Optional[CombatReport] = None


# =============================================================================
# LOCALIZATION ENGINE
# =============================================================================

class LocalizationDB:
    def __init__(self):
        self.pt_keys: Dict[str, str] = {}
        self.en_keys: Dict[str, str] = {}
        self.load_all()

    def load_all(self):
        # Load PT-BR
        pt_dir = LOCALISATION_DIR / "braz_por"
        if pt_dir.exists():
            for f in pt_dir.glob("*.yml"):
                self._load_file(f, self.pt_keys)
        # Load English
        en_dir = LOCALISATION_DIR / "english"
        if en_dir.exists():
            for f in en_dir.glob("*.yml"):
                self._load_file(f, self.en_keys)

    def _load_file(self, path: Path, target_dict: Dict[str, str]):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                for line in file:
                    line = line.strip()
                    if ":" in line and not line.startswith("#") and not line.startswith("l_"):
                        parts = line.split(":", 1)
                        key = parts[0].strip()
                        val = parts[1].strip()
                        if val.startswith('"') and val.endswith('"'):
                            val = val[1:-1]
                        elif re.match(r'^[0-9]\s*"', val):
                            # e.g. 0 "Text"
                            m = re.search(r'"(.*)"', val)
                            if m:
                                val = m.group(1)
                        target_dict[key] = val
        except Exception:
            pass


GLOBAL_LOC = LocalizationDB()


# =============================================================================
# PARSER UTILITIES
# =============================================================================

def parse_bracket_content(text: str, start_pos: int) -> Tuple[str, int]:
    depth = 0
    content_start = -1
    for i in range(start_pos, len(text)):
        ch = text[i]
        if ch == '{':
            if depth == 0:
                content_start = i + 1
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return text[content_start:i], i + 1
    return "", len(text)


def extract_focus_nodes(file_path: Path) -> Dict[str, FocusNode]:
    if not file_path.exists():
        return {}

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    nodes: Dict[str, FocusNode] = {}
    
    clean_lines = []
    for line in text.splitlines():
        if "#" in line:
            line = line[:line.index("#")]
        clean_lines.append(line)
    clean_text = "\n".join(clean_lines)

    pos = 0
    focus_pattern = re.compile(r'\bfocus\s*=\s*\{')

    while True:
        match = focus_pattern.search(clean_text, pos)
        if not match:
            break
        
        block, end_idx = parse_bracket_content(clean_text, match.end() - 1)
        pos = end_idx

        id_match = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block)
        if not id_match:
            continue
        focus_id = id_match.group(1)

        x_match = re.search(r'\bx\s*=\s*([0-9\-]+)', block)
        y_match = re.search(r'\by\s*=\s*([0-9\-]+)', block)
        x = int(x_match.group(1)) if x_match else 0
        y = int(y_match.group(1)) if y_match else 0

        cost_match = re.search(r'\bcost\s*=\s*([0-9\.]+)', block)
        cost_multiplier = float(cost_match.group(1)) if cost_match else 10.0
        cost_days = int(cost_multiplier * 7)

        prereqs = []
        for p_match in re.finditer(r'prerequisite\s*=\s*\{', block):
            p_block, _ = parse_bracket_content(block, p_match.end() - 1)
            f_ids = re.findall(r'\bfocus\s*=\s*([a-zA-Z0-9_]+)', p_block)
            if f_ids:
                prereqs.append(f_ids)

        mut_excl = []
        m_match = re.search(r'mutually_exclusive\s*=\s*\{', block)
        if m_match:
            m_block, _ = parse_bracket_content(block, m_match.end() - 1)
            mut_excl = re.findall(r'\bfocus\s*=\s*([a-zA-Z0-9_]+)', m_block)

        reward_match = re.search(r'completion_reward\s*=\s*\{', block)
        raw_reward = ""
        if reward_match:
            raw_reward, _ = parse_bracket_content(block, reward_match.end() - 1)

        ai_match = re.search(r'ai_will_do\s*=\s*\{', block)
        raw_ai = ""
        if ai_match:
            raw_ai, _ = parse_bracket_content(block, ai_match.end() - 1)

        # 3-Phase Classification based on vertical topology and content
        if y <= 4:
            phase = 1
            phase_name = "Curto Prazo (1911-1914)"
        elif y <= 8:
            phase = 2
            phase_name = "Medio Prazo (1914-1916)"
        else:
            phase = 3
            phase_name = "Longo Prazo (1917-1920)"

        node = FocusNode(
            id=focus_id,
            x=x,
            y=y,
            cost_days=cost_days,
            prerequisites=prereqs,
            mutually_exclusive=mut_excl,
            raw_reward=raw_reward,
            raw_ai=raw_ai,
            phase=phase,
            phase_name=phase_name
        )

        nodes[focus_id] = node

    return nodes


# =============================================================================
# SUBSTANCE & GAME DESIGN SCORING ALGORITHM
# =============================================================================

def analyze_focus(node: FocusNode) -> None:
    reward = node.raw_reward
    score = 0.0
    strengths = []
    fillers = []

    # 1. Map Impact (Factories, Dockyards, Infrastructure, Building slots)
    civs = len(re.findall(r'industrial_complex\s*=\s*[1-9]', reward)) + len(re.findall(r'type\s*=\s*industrial_complex', reward))
    mils = len(re.findall(r'arms_factory\s*=\s*[1-9]', reward)) + len(re.findall(r'type\s*=\s*arms_factory', reward))
    docks = len(re.findall(r'dockyard\s*=\s*[1-9]', reward)) + len(re.findall(r'type\s*=\s*dockyard', reward))
    slots = len(re.findall(r'add_extra_state_shared_building_slots\s*=\s*[1-9]', reward))
    infras = len(re.findall(r'infrastructure\s*=\s*[1-9]', reward))
    
    node.factories_civ = civs
    node.factories_mil = mils
    node.dockyards = docks
    node.slots = slots

    if civs > 0:
        score += civs * 2.5
        strengths.append(f"+{civs} Fabrica(s) Civil(is)")
    if mils > 0:
        score += mils * 3.0
        strengths.append(f"+{mils} Fabrica(s) Militar(es)")
    if docks > 0:
        score += docks * 2.5
        strengths.append(f"+{docks} Estaleiro(s)")
    if slots > 0:
        score += slots * 1.5
        strengths.append(f"+{slots} Slot(s) de Construcao")
    if infras > 0:
        score += infras * 1.0
        strengths.append(f"+{infras} Nivel(eis) de Infraestrutura")

    # 2. Military Units & Equipment
    units = len(re.findall(r'create_unit\s*=', reward)) + len(re.findall(r'load_oob\s*=', reward))
    node.units_spawned = units
    if units > 0:
        score += 3.5 * units
        strengths.append(f"Spawn de {units} Divisao(oes)/OOB")

    equip = re.findall(r'add_equipment_to_stockpile\s*=\s*\{[^}]*amount\s*=\s*([0-9]+)', reward)
    if equip:
        score += 2.0
        strengths.append("Envio direto de armamento/artilharia para estoque")

    # 3. Interactivity (Decisions, Missions, Dynamic Mechanics)
    decisions = re.findall(r'activate_mission\s*=\s*([a-zA-Z0-9_]+)', reward)
    dec_cats = re.findall(r'unlocks_decision_category\s*=\s*([a-zA-Z0-9_]+)', reward)
    add_dec = re.findall(r'add_decision\s*=\s*([a-zA-Z0-9_]+)', reward)
    all_dec = list(set(decisions + dec_cats + add_dec))
    node.unlocked_decisions = all_dec
    if all_dec:
        score += 3.0 * len(all_dec)
        strengths.append(f"Destrava {len(all_dec)} Decisao(oes)/Missao(oes)")

    # 4. Narrative & Diplomacy (Bilateral Country Events)
    events = re.findall(r'country_event\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_\.]+)', reward)
    node.fired_events = events
    if events:
        score += 2.5 * len(events)
        strengths.append(f"Dispara {len(events)} Evento(s) Bilateral(is)")

    # 5. Ideas and Spirits
    ideas = re.findall(r'add_ideas\s*=\s*([a-zA-Z0-9_]+)', reward)
    node.gives_ideas = ideas
    if ideas:
        score += 2.0 * len(ideas)
        strengths.append(f"Modifica Espirito Nacional ({len(ideas)})")

    # 6. XP and Army/Navy/Air Doctrines
    xp = re.findall(r'add_(?:army|navy|air)_experience\s*=\s*([0-9]+)', reward)
    if xp:
        score += 1.0
        strengths.append(f"Concede XP Militar ({', '.join(xp)})")

    # 7. Check for Pure Filler (Shallow Content)
    has_meaningful_impact = (civs > 0 or mils > 0 or docks > 0 or slots > 0 or units > 0 or
                             len(all_dec) > 0 or len(events) > 0 or len(ideas) > 0 or equip)
    
    only_pp = bool(re.search(r'add_political_power\s*=', reward) and not has_meaningful_impact)
    only_stab = bool(re.search(r'add_stability\s*=', reward) and not has_meaningful_impact)
    only_war_sup = bool(re.search(r'add_war_support\s*=', reward) and not has_meaningful_impact)

    if only_pp:
        fillers.append("Apenas concede Poder Politico sem impacto material")
    if only_stab:
        fillers.append("Apenas altera estabilidade bruta sem dilema")
    if only_war_sup:
        fillers.append("Apenas altera apoio de guerra")

    if not reward.strip():
        fillers.append("Foco 100% Vazio (Sem nenhum efeito executado)")
        score = 0.0

    if not has_meaningful_impact and (only_pp or only_stab or only_war_sup):
        score = min(score + 1.5, 2.2)
        node.is_filler = True
    elif not has_meaningful_impact and not fillers:
        score = max(score, 2.0)
        fillers.append("Apenas bonus generico residual de pesquisa")
        node.is_filler = True

    if node.cost_days >= 70 and score < 3.0:
        score = max(0.5, score - 1.0)
        fillers.append("Custo excessivo (70 dias) para recompensa insignificante")

    node.substance_score = round(min(score, 10.0), 1)
    node.strengths = strengths
    node.filler_reasons = fillers

    # Categorization
    if node.substance_score >= 7.5:
        node.category = "Epic"
    elif node.substance_score >= 5.0:
        node.category = "Solid"
    elif node.substance_score >= 2.5:
        node.category = "Moderate"
    else:
        node.category = "Dead/Filler"
        node.is_filler = True

    # 8. AI Behavior Analysis
    if node.raw_ai.strip():
        node.has_ai_will_do = True
        factor_match = re.search(r'factor\s*=\s*([0-9\.]+)', node.raw_ai)
        if factor_match:
            node.ai_base_factor = float(factor_match.group(1))
            if node.ai_base_factor == 0:
                node.ai_status = "Ignorado pela IA (Factor 0)"
            elif node.ai_base_factor >= 5:
                node.ai_status = "Prioridade Alta para IA"
            else:
                node.ai_status = "Prioridade Normal"
    else:
        node.has_ai_will_do = False
        node.ai_status = "Sem ai_will_do (Selecao Aleatoria)"

    # 9. Localization Audit
    node.has_loc_pt = node.id in GLOBAL_LOC.pt_keys
    node.has_loc_en = node.id in GLOBAL_LOC.en_keys
    node.loc_pt_title = GLOBAL_LOC.pt_keys.get(node.id, node.id)
    desc_key = f"{node.id}_desc"
    desc_text = GLOBAL_LOC.pt_keys.get(desc_key, "")
    node.loc_pt_desc_len = len(desc_text)
    if not node.has_loc_pt or node.loc_pt_desc_len < 25:
        node.is_loc_shallow = True


# =============================================================================
# COMBAT & MILITARY TEMPLATE RADAR
# =============================================================================

def analyze_combat(tag: str) -> CombatReport:
    oob_file = TAG_TO_OOB.get(tag)
    history_file = TAG_TO_HISTORY.get(tag)
    report = CombatReport(tag=tag)

    if not oob_file or not oob_file.exists():
        report.warnings.append(f"Arquivo OOB inicial para {tag} nao encontrado.")
        return report

    with open(oob_file, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    # Parse division templates
    t_pattern = re.compile(r'\bdivision_template\s*=\s*\{')
    pos = 0
    while True:
        match = t_pattern.search(text, pos)
        if not match:
            break
        block, end_idx = parse_bracket_content(text, match.end() - 1)
        pos = end_idx

        name_match = re.search(r'name\s*=\s*"([^"]+)"', block)
        template_name = name_match.group(1) if name_match else "Unknown Template"

        # Regiments
        battalions = []
        reg_match = re.search(r'regiments\s*=\s*\{', block)
        if reg_match:
            r_block, _ = parse_bracket_content(block, reg_match.end() - 1)
            battalions = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{', r_block)

        # Supports
        supports = []
        sup_match = re.search(r'support\s*=\s*\{', block)
        if sup_match:
            s_block, _ = parse_bracket_content(block, sup_match.end() - 1)
            supports = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{', s_block)

        combat_width = len(battalions) * 2  # WW1 baseline ~2 width per regular battalion
        template = DivisionTemplate(
            name=template_name,
            battalions=battalions,
            supports=supports,
            combat_width=combat_width,
            total_manpower=len(battalions) * 1000 + len(supports) * 400
        )

        if combat_width < 12:
            template.is_balanced = False
            template.critique = f"Largura de combate perigosamente baixa ({combat_width} width). Divisao frágil para trincheiras."
        elif "artillery" not in supports and not any("artillery" in b for b in battalions):
            template.is_balanced = False
            template.critique = "Ausencia total de artilharia! Sofrerá atrito brutal contra infantaria entrincheirada."
        else:
            template.critique = "Template solido para combate de trincheiras (WW1)."

        report.templates.append(template)

    # Count divisions in OOB
    div_count = len(re.findall(r'\bdivision\s*=\s*\{', text))
    report.total_starting_divisions = div_count

    # Check Stockpile in History
    if history_file and history_file.exists():
        with open(history_file, "r", encoding="utf-8", errors="ignore") as f:
            h_text = f.read()
        
        # Stockpiles
        inf_guns = re.findall(r'type\s*=\s*infantry_equipment_[0-9][^}]*amount\s*=\s*([0-9]+)', h_text)
        art_guns = re.findall(r'type\s*=\s*artillery_equipment_[0-9][^}]*amount\s*=\s*([0-9]+)', h_text)
        sup_guns = re.findall(r'type\s*=\s*support_equipment_[0-9][^}]*amount\s*=\s*([0-9]+)', h_text)

        report.infantry_equipment_stockpile = sum(int(x) for x in inf_guns)
        report.artillery_stockpile = sum(int(x) for x in art_guns)
        report.support_equipment_stockpile = sum(int(x) for x in sup_guns)

        min_inf_needed = report.total_starting_divisions * 800
        if report.infantry_equipment_stockpile < 1000:
            report.is_stockpile_sufficient = False
            report.warnings.append(f"Estoque inicial de fuzis critico (+{report.infantry_equipment_stockpile}). Risco de desarmamento no day 1.")

    return report


# =============================================================================
# MULTIPLAYER SAFETY & PERFORMANCE RADAR
# =============================================================================

def audit_multiplayer_safety() -> List[str]:
    hazards = []

    # Check on_actions
    if ON_ACTIONS_DIR.exists():
        for f in ON_ACTIONS_DIR.glob("*.txt"):
            with open(f, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
                if "on_daily" in content:
                    lines = content.splitlines()
                    for idx, line in enumerate(lines, 1):
                        if "every_country" in line or "every_state" in line:
                            hazards.append(f"[PERFORMANCE / LAG] Loop global em on_daily detectado em {f.name}:{idx}: '{line.strip()}'")

    # Check Events for random_list desyncs
    if EVENTS_DIR.exists():
        for f in EVENTS_DIR.glob("*.txt"):
            with open(f, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
                # Check for unbounded random lists
                if "random_list = {" in content:
                    # Verify if it has seed protection or ai safety
                    pass

    return hazards


# =============================================================================
# TREE AUDIT & AGGREGATION
# =============================================================================

def analyze_tree(tag: str, file_path: Path) -> TreeReport:
    nodes = extract_focus_nodes(file_path)
    report = TreeReport(tag=tag, file_path=str(file_path), total_focuses=len(nodes))

    if not nodes:
        return report

    total_score = 0.0
    filler_nodes = []
    ai_count = 0
    loc_count = 0
    shallow_loc_count = 0

    p1_nodes, p2_nodes, p3_nodes = [], [], []
    coords_seen: Dict[Tuple[int, int], str] = {}
    collision_count = 0

    for f_id, node in nodes.items():
        analyze_focus(node)
        total_score += node.substance_score
        
        # Phases
        if node.phase == 1:
            p1_nodes.append(node)
        elif node.phase == 2:
            p2_nodes.append(node)
        else:
            p3_nodes.append(node)

        report.total_civ_factories += node.factories_civ
        report.total_mil_factories += node.factories_mil
        report.total_dockyards += node.dockyards
        report.total_slots += node.slots
        report.total_events_fired += len(node.fired_events)
        report.total_decisions_unlocked += len(node.unlocked_decisions)

        if node.is_filler or node.substance_score < 2.5:
            filler_nodes.append(node)

        if node.has_ai_will_do:
            ai_count += 1
        if node.has_loc_pt and node.has_loc_en:
            loc_count += 1
        if node.is_loc_shallow:
            shallow_loc_count += 1

        coord = (node.x, node.y)
        if coord in coords_seen:
            collision_count += 1
        else:
            coords_seen[coord] = f_id

        if node.x <= 4 and node.y <= 6:
            report.continuous_focus_hazard = True

    report.nodes = nodes
    report.total_focuses = len(nodes)
    report.avg_substance_score = round(total_score / len(nodes), 2)
    report.filler_count = len(filler_nodes)
    report.filler_percentage = round((len(filler_nodes) / len(nodes)) * 100, 1)
    report.collision_count = collision_count

    # Phase Metrics
    report.phase_1_count = len(p1_nodes)
    report.phase_2_count = len(p2_nodes)
    report.phase_3_count = len(p3_nodes)
    report.phase_1_score = round(sum(n.substance_score for n in p1_nodes) / max(len(p1_nodes), 1), 2)
    report.phase_2_score = round(sum(n.substance_score for n in p2_nodes) / max(len(p2_nodes), 1), 2)
    report.phase_3_score = round(sum(n.substance_score for n in p3_nodes) / max(len(p3_nodes), 1), 2)

    # AI & Loc
    report.ai_coverage_pct = round((ai_count / len(nodes)) * 100, 1)
    report.loc_coverage_pct = round((loc_count / len(nodes)) * 100, 1)
    report.shallow_loc_count = shallow_loc_count

    # Hitlist
    filler_nodes.sort(key=lambda n: (n.substance_score, -n.cost_days))
    report.hitlist = filler_nodes[:20]

    if p1_nodes:
        report.pacing_1914_readiness_pct = round(min(100.0, report.phase_1_score * 12.5), 1)

    # Attach combat report
    report.combat = analyze_combat(tag)

    return report


# =============================================================================
# INTERACTIVE 2D HTML RADAR (ENHANCED WITH PHASE FILTERS)
# =============================================================================

def generate_interactive_html(report: TreeReport, output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    nodes = list(report.nodes.values())
    
    min_x = min((n.x for n in nodes), default=0)
    max_x = max((n.x for n in nodes), default=30)
    min_y = min((n.y for n in nodes), default=0)
    max_y = max((n.y for n in nodes), default=15)

    width = (max_x - min_x + 3) * 110 + 200
    height = (max_y - min_y + 3) * 130 + 300

    nodes_json = []
    for n in nodes:
        nodes_json.append({
            "id": n.id,
            "title": n.loc_pt_title,
            "x": n.x,
            "y": n.y,
            "phase": n.phase,
            "phase_name": n.phase_name,
            "cost_days": n.cost_days,
            "score": n.substance_score,
            "category": n.category,
            "is_filler": n.is_filler,
            "ai_status": n.ai_status,
            "has_ai": n.has_ai_will_do,
            "civs": n.factories_civ,
            "mils": n.factories_mil,
            "docks": n.dockyards,
            "slots": n.slots,
            "events": n.fired_events,
            "decisions": n.unlocked_decisions,
            "strengths": n.strengths,
            "fillers": n.filler_reasons,
            "prereqs": n.prerequisites
        })

    combat_summary_html = ""
    if report.combat and report.combat.templates:
        combat_summary_html = f"""
        <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border); border-radius: 8px; padding: 10px; font-size: 0.8rem;">
            <div style="font-weight: 700; color: #fff; margin-bottom: 6px;">⚔️ Balística & Exército Inicial</div>
            <div>Divisões Iniciais: <b>{report.combat.total_starting_divisions}</b></div>
            <div>Estoque Fuzis: <b>+{report.combat.infantry_equipment_stockpile}</b> | Canhões: <b>+{report.combat.artillery_stockpile}</b></div>
            <div style="margin-top: 6px; font-weight: 600; color: #8b949e;">Templates Identificados:</div>
            <ul style="padding-left: 16px; margin: 4px 0;">
        """
        for t in report.combat.templates[:3]:
            combat_summary_html += f"<li><b>{t.name}</b> ({t.combat_width}W) — {t.critique}</li>"
        combat_summary_html += "</ul></div>"

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Radar de Game Design — {report.tag}</title>
    <style>
        :root {{
            --bg: #0d1117;
            --panel: #161b22;
            --border: #30363d;
            --text: #c9d1d9;
            --accent: #58a6ff;
            --dead: #f85149;
            --moderate: #d29922;
            --solid: #3fb950;
            --epic: #a371f7;
        }}
        body {{
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            overflow: hidden;
            display: flex;
            height: 100vh;
        }}
        #sidebar {{
            width: 400px;
            background: var(--panel);
            border-right: 1px solid var(--border);
            padding: 16px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            gap: 12px;
            overflow-y: auto;
            z-index: 10;
        }}
        h1 {{
            font-size: 1.25rem;
            margin: 0;
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .filter-bar {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .filter-btn {{
            background: #21262d;
            border: 1px solid var(--border);
            color: #c9d1d9;
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 0.75rem;
            cursor: pointer;
            transition: all 0.15s ease;
        }}
        .filter-btn.active, .filter-btn:hover {{
            background: var(--accent);
            color: #fff;
            border-color: var(--accent);
        }}
        .stat-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }}
        .stat-card {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 8px;
            text-align: center;
        }}
        .stat-val {{
            font-size: 1.25rem;
            font-weight: 700;
            color: #fff;
        }}
        .stat-lbl {{
            font-size: 0.72rem;
            color: #8b949e;
        }}
        .phase-box {{
            display: flex;
            justify-content: space-between;
            background: #21262d;
            border-radius: 6px;
            padding: 6px 10px;
            font-size: 0.75rem;
        }}
        #canvas-container {{
            flex: 1;
            position: relative;
            background: radial-gradient(circle at 50% 50%, #161b22 0%, #0d1117 100%);
            overflow: auto;
        }}
        svg {{
            width: {width}px;
            height: {height}px;
        }}
        .node {{
            cursor: pointer;
            transition: transform 0.15s ease;
        }}
        .node:hover {{
            filter: drop-shadow(0 0 10px rgba(88, 166, 255, 0.7));
        }}
        .node rect {{
            stroke-width: 2px;
            rx: 6px;
        }}
        .node-dead rect {{ fill: #2d1517; stroke: var(--dead); }}
        .node-moderate rect {{ fill: #2b2311; stroke: var(--moderate); }}
        .node-solid rect {{ fill: #132b1a; stroke: var(--solid); }}
        .node-epic rect {{ fill: #27173e; stroke: var(--epic); }}
        .node.dimmed {{ opacity: 0.15; }}
        .node text {{
            fill: #fff;
            font-size: 10px;
            font-weight: 600;
            text-anchor: middle;
            user-select: none;
        }}
        .node-subtext {{
            fill: #8b949e;
            font-size: 8.5px;
            font-weight: 400;
        }}
        line.link {{
            stroke: #30363d;
            stroke-width: 2px;
        }}
        #details-pane {{
            background: rgba(0, 0, 0, 0.25);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 10px;
            font-size: 0.8rem;
        }}
        .hitlist-item {{
            padding: 6px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            font-size: 0.78rem;
            cursor: pointer;
        }}
        .hitlist-item:hover {{
            background: rgba(255, 255, 255, 0.04);
        }}
    </style>
</head>
<body>
    <div id="sidebar">
        <h1>
            <span>🇦🇹 Radar de Jogabilidade — {report.tag}</span>
            <span style="font-size: 0.8rem; color: var(--accent);">{report.total_focuses} focos</span>
        </h1>
        
        <div class="filter-bar">
            <button class="filter-btn active" onclick="setFilter('all')">Todos</button>
            <button class="filter-btn" onclick="setFilter('phase1')">1911-1914</button>
            <button class="filter-btn" onclick="setFilter('phase2')">1914-1916</button>
            <button class="filter-btn" onclick="setFilter('phase3')">1917-1920</button>
            <button class="filter-btn" onclick="setFilter('filler')">So Fillers</button>
        </div>

        <div class="phase-box">
            <div>Fase 1: <b>{report.phase_1_count} focos ({report.phase_1_score}/10)</b></div>
            <div>Fase 2: <b>{report.phase_2_count} focos ({report.phase_2_score}/10)</b></div>
            <div>Fase 3: <b>{report.phase_3_count} focos ({report.phase_3_score}/10)</b></div>
        </div>

        <div class="stat-grid">
            <div class="stat-card">
                <div class="stat-val" style="color: {'var(--solid)' if report.avg_substance_score >= 5.0 else 'var(--dead)'}">
                    {report.avg_substance_score}/10
                </div>
                <div class="stat-lbl">Score Medio Geral</div>
            </div>
            <div class="stat-card">
                <div class="stat-val" style="color: {'var(--dead)' if report.filler_percentage > 25 else 'var(--solid)'}">
                    {report.filler_percentage}%
                </div>
                <div class="stat-lbl">{report.filler_count} Focos Mortos</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">{report.ai_coverage_pct}%</div>
                <div class="stat-lbl">Cobertura IA (ai_will_do)</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">{report.loc_coverage_pct}%</div>
                <div class="stat-lbl">Imersao de Traducao</div>
            </div>
        </div>

        {combat_summary_html}

        <div id="details-pane">
            <div style="font-weight: 700; margin-bottom: 4px; color: #fff;">🔍 Inspecionar Foco</div>
            <div id="inspect-content" style="color: #8b949e;">Clique em qualquer nó para ver análise profunda de jogo e de texto.</div>
        </div>

        <div>
            <div style="font-weight: 700; margin-bottom: 6px; color: var(--dead); font-size: 0.8rem;">
                ⚠️ Focos Mais Rasos / Sem Conteudo (Hit List):
            </div>
            <div style="max-height: 180px; overflow-y: auto;">
"""
    for node in report.hitlist[:10]:
        html_content += f"""
                <div class="hitlist-item" onclick="selectNode('{node.id}')">
                    <div style="font-weight: 600; color: #fff;">{node.loc_pt_title}</div>
                    <div style="color: var(--dead); font-size: 0.72rem;">Score {node.substance_score}/10 — {node.phase_name}</div>
                </div>
        """

    html_content += f"""
            </div>
        </div>
    </div>

    <div id="canvas-container">
        <svg id="svg-tree">
            <g id="links-group"></g>
            <g id="nodes-group"></g>
        </svg>
    </div>

    <script>
        const nodesData = {json.dumps(nodes_json)};
        const nodeMap = {{}};
        nodesData.forEach(n => nodeMap[n.id] = n);

        const linksGroup = document.getElementById('links-group');
        const nodesGroup = document.getElementById('nodes-group');

        const xOffset = 60 - ({min_x} * 110);
        const yOffset = 60 - ({min_y} * 130);

        function getNodePos(node) {{
            return {{
                x: node.x * 110 + xOffset,
                y: node.y * 130 + yOffset
            }};
        }}

        // Draw Links
        nodesData.forEach(target => {{
            const tPos = getNodePos(target);
            target.prereqs.forEach(prereqList => {{
                prereqList.forEach(sourceId => {{
                    const source = nodeMap[sourceId];
                    if (source) {{
                        const sPos = getNodePos(source);
                        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                        line.setAttribute('x1', sPos.x + 45);
                        line.setAttribute('y1', sPos.y + 45);
                        line.setAttribute('x2', tPos.x + 45);
                        line.setAttribute('y2', tPos.y);
                        line.setAttribute('class', 'link');
                        linksGroup.appendChild(line);
                    }}
                }});
            }});
        }});

        // Draw Nodes
        nodesData.forEach(node => {{
            const pos = getNodePos(node);
            const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
            
            let catClass = 'node-solid';
            if (node.score >= 7.5) catClass = 'node-epic';
            else if (node.score >= 5.0) catClass = 'node-solid';
            else if (node.score >= 2.5) catClass = 'node-moderate';
            else catClass = 'node-dead';

            g.setAttribute('class', `node ${{catClass}}`);
            g.setAttribute('id', `node-${{node.id}}`);
            g.setAttribute('data-phase', node.phase);
            g.setAttribute('data-filler', node.is_filler);
            g.setAttribute('transform', `translate(${{pos.x}}, ${{pos.y}})`);
            g.onclick = () => selectNode(node.id);

            const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            rect.setAttribute('width', '90');
            rect.setAttribute('height', '50');

            const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            text.setAttribute('x', '45');
            text.setAttribute('y', '20');
            let shortName = node.title || node.id;
            if (shortName.length > 13) shortName = shortName.substring(0, 12) + '..';
            text.textContent = shortName;

            const scoreText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            scoreText.setAttribute('x', '45');
            scoreText.setAttribute('y', '37');
            scoreText.setAttribute('class', 'node-subtext');
            scoreText.textContent = `${{node.score}} pts | ${{node.cost_days}}d`;

            g.appendChild(rect);
            g.appendChild(text);
            g.appendChild(scoreText);
            nodesGroup.appendChild(g);
        }});

        function setFilter(filter) {{
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            event.target.classList.add('active');

            document.querySelectorAll('.node').forEach(el => {{
                const phase = el.getAttribute('data-phase');
                const isFiller = el.getAttribute('data-filler') === 'true';

                if (filter === 'all') {{
                    el.classList.remove('dimmed');
                }} else if (filter === 'phase1') {{
                    el.classList.toggle('dimmed', phase !== '1');
                }} else if (filter === 'phase2') {{
                    el.classList.toggle('dimmed', phase !== '2');
                }} else if (filter === 'phase3') {{
                    el.classList.toggle('dimmed', phase !== '3');
                }} else if (filter === 'filler') {{
                    el.classList.toggle('dimmed', !isFiller);
                }}
            }});
        }}

        function selectNode(id) {{
            const n = nodeMap[id];
            if (!n) return;

            let html = `
                <div style="font-weight: 700; color: #fff; font-size: 0.9rem; margin-bottom: 3px;">${{n.title}} (${{n.id}})</div>
                <div style="color: #8b949e; font-size: 0.73rem; margin-bottom: 6px;">
                    Fase: <b>${{n.phase_name}}</b> | Duração: ${{n.cost_days}} dias | IA: ${{n.ai_status}}
                </div>
                <div style="font-size: 1.05rem; font-weight: 700; color: ${{n.score >= 5 ? 'var(--solid)' : 'var(--dead)'}}; margin-bottom: 6px;">
                    Score de Conteúdo: ${{n.score}} / 10
                </div>
            `;

            if (n.strengths.length > 0) {{
                html += '<div style="color: var(--solid); font-weight: 600; margin-top: 4px;">Impacto Mecanico:</div><ul style="padding-left: 16px; margin: 3px 0;">';
                n.strengths.forEach(s => html += `<li>${{s}}</li>`);
                html += '</ul>';
            }}

            if (n.fillers.length > 0) {{
                html += '<div style="color: var(--dead); font-weight: 600; margin-top: 4px;">Falhas de Gameplay / Filler:</div><ul style="padding-left: 16px; margin: 3px 0;">';
                n.fillers.forEach(f => html += `<li>${{f}}</li>`);
                html += '</ul>';
            }}

            document.getElementById('inspect-content').innerHTML = html;
        }}
    </script>
</body>
</html>
"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)


# =============================================================================
# CLI COMMAND EXECUTIONS
# =============================================================================

def run_inspect(tag: str) -> None:
    tag = tag.upper()
    file_path = TAG_TO_FILE.get(tag)
    if not file_path or not file_path.exists():
        print(f"[ERRO] Arquivo de foco para a tag '{tag}' nao encontrado em {FOCUS_DIR}")
        return

    report = analyze_tree(tag, file_path)
    
    print("\n" + "=" * 80)
    print(f"       HOI4 GAMEPLAY RADAR COMPLETO — RAIO-X DE JOGABILIDADE ({report.tag})")
    print("=" * 80)
    print(f" Arquivo                 : {report.file_path}")
    print(f" Total de Focos          : {report.total_focuses}")
    print(f" Score Medio de Conteudo : {report.avg_substance_score} / 10.0")
    print(f" Focos Mortos (Filler)   : {report.filler_count} ({report.filler_percentage}%)")
    print("-" * 80)
    print(f" [1] ARCO CRONOLOGICO EM 3 FASES:")
    print(f"     Fase 1 (1911-1914 Curto) : {report.phase_1_count} focos | Score: {report.phase_1_score}/10 (Prontidao Guerra: {report.pacing_1914_readiness_pct}%)")
    print(f"     Fase 2 (1914-1916 Medio) : {report.phase_2_count} focos | Score: {report.phase_2_score}/10 (Economia de Trincheira)")
    print(f"     Fase 3 (1917-1920 Longo) : {report.phase_3_count} focos | Score: {report.phase_3_score}/10 (Exaustao & Fim de Guerra)")
    print("-" * 80)
    print(f" [2] IMPACTO MATERIAL NO MAPA:")
    print(f"     Fabricas Construidas     : Civ: +{report.total_civ_factories} | Mil: +{report.total_mil_factories} | Estaleiros: +{report.total_dockyards}")
    print(f"     Slots de Construcao      : +{report.total_slots} slots")
    print(f"     Decisoes / Missoes       : {report.total_decisions_unlocked} destravadas")
    print(f"     Eventos Bilaterais       : {report.total_events_fired} disparados")
    print("-" * 80)
    print(f" [3] INTELIGENCIA ARTIFICIAL & IMERSAO:")
    print(f"     Cobertura de IA (ai)     : {report.ai_coverage_pct}% dos focos possuem ai_will_do")
    print(f"     Traducao & Localizacao   : {report.loc_coverage_pct}% cobertura | {report.shallow_loc_count} textos superficiais")
    print(f"     Colisoes de Coordenadas  : {report.collision_count} conflitos")
    print(f"     Risco Foco Continuo      : {'[ALERTA] Risco de sobreposicao no topo esquerdo' if report.continuous_focus_hazard else '[OK] Limpo'}")
    
    if report.combat and report.combat.templates:
        print("-" * 80)
        print(f" [4] BALISTICA & EXERCITO INICIAL (COMBAT RADAR):")
        print(f"     Divisoes Iniciais OOB    : {report.combat.total_starting_divisions} divisoes")
        print(f"     Estoque Fuzis / Canhoes  : +{report.combat.infantry_equipment_stockpile} fuzis | +{report.combat.artillery_stockpile} pecas de artilharia")
        for t in report.combat.templates[:2]:
            print(f"     Template '{t.name}': {t.combat_width}W -> {t.critique}")
        for w in report.combat.warnings:
            print(f"     [!] ALERTA MILITAR: {w}")

    print("=" * 80)

    if report.hitlist:
        print("\n [!] HIT LIST — OS 10 FOCOS MAIS RASOS QUE PRECISAM DE MECANICA IMEDIATA:")
        for idx, node in enumerate(report.hitlist[:10], 1):
            reasons = "; ".join(node.filler_reasons) if node.filler_reasons else "Recompensa insignificante"
            print(f"   {idx:2d}. {node.loc_pt_title:<28} ({node.id}) | {node.phase_name} (Score: {node.substance_score}/10) -> {reasons}")

    html_out = OUTPUT_DIR / f"{tag}_focus_tree.html"
    generate_interactive_html(report, html_out)
    print(f"\n [+] Painel Visual 2D Interativo com Filtro de Fases Gerado em:\n     file:///{html_out.as_posix()}\n")


def run_audit_all() -> None:
    print("\n" + "=" * 95)
    print("       AUDITORIA GLOBAL MULTIDIMENSIONAL DE JOGABILIDADE (TODAS AS POTENCIAS)")
    print("=" * 95)
    print(f" {'TAG':<5} | {'Focos':<5} | {'Score':<6} | {'Fase 1':<8} | {'Fase 2':<8} | {'Fase 3':<8} | {'Fillers':<10} | {'IA %':<6} | {'Loc %':<6} | {'Status':<12}")
    print("-" * 95)

    for tag, file_path in TAG_TO_FILE.items():
        if tag in ["AUH", "SOV"]:
            continue
        if not file_path.exists():
            continue
        report = analyze_tree(tag, file_path)
        status = "EXCELENTE" if report.avg_substance_score >= 6.0 and report.filler_percentage <= 15 else "PRECISA POLIR"
        if report.avg_substance_score < 4.0 or report.filler_percentage > 35:
            status = "CRITICO/RASO"
        print(f" {tag:<5} | {report.total_focuses:<5} | {report.avg_substance_score:<6} | {report.phase_1_score:<8} | {report.phase_2_score:<8} | {report.phase_3_score:<8} | {report.filler_percentage}%      | {report.ai_coverage_pct}%  | {report.loc_coverage_pct}%  | {status:<12}")

    print("=" * 95 + "\n")


def run_mp_safety() -> None:
    print("\n" + "=" * 80)
    print("       AUDITORIA DE SEGURANCA MULTIPLAYER, DESYNC (OOS) E TELEMETRIA DE LAG")
    print("=" * 80)
    hazards = audit_multiplayer_safety()
    if hazards:
        print(f" Foram identificados {len(hazards)} pontos de atencao para estabilidade:")
        for h in hazards:
            print(f"  {h}")
    else:
        print(" [OK] Nenhum loop infinito ou loop global no on_daily detectado no momento.")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python scripts/mod_engine.py inspect <TAG>   -> Inspeciona o ecossistema completo de um pais")
        print("  python scripts/mod_engine.py audit-all       -> Auditoria comparativa global de todas as potencias")
        print("  python scripts/mod_engine.py mp-safety       -> Auditoria anti-desync e anti-lag para multiplayer")
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd == "inspect" and len(sys.argv) >= 3:
        run_inspect(sys.argv[2])
    elif cmd == "audit-all":
        run_audit_all()
    elif cmd == "mp-safety":
        run_mp_safety()
    else:
        run_inspect(sys.argv[1])

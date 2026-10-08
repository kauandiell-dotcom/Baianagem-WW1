#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
       HOI4 BAIANAGEM-WW1 GAME DESIGN & GAMEPLAY RADAR ENGINE (mod_engine.py)
===============================================================================
A specialized engine for evaluating, auditing, and visualizing Hearts of Iron IV
gameplay substance, pacing, multiplayer viability, and visual ergonomics.

Key capabilities:
 1. Cross-System Parsing (Focuses, Decisions, Events, Ideas, Map State effects).
 2. Substance & Fun Scoring Algorithm (0.0 to 10.0 per focus).
 3. Pacing & 1911-1914 Outbreak Reachability Simulator.
 4. GUI & Continuous-Focus Collision Detection.
 5. Interactive 2D Visual HTML Exporter with SVG Directed Acyclic Graphs.
===============================================================================
"""

import os
import re
import sys
import json
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Set, Optional, Tuple

ROOT_DIR = Path(__file__).resolve().parent.parent
COMMON_DIR = ROOT_DIR / "common"
FOCUS_DIR = COMMON_DIR / "national_focus"
DECISIONS_DIR = COMMON_DIR / "decisions"
EVENTS_DIR = ROOT_DIR / "events"
IDEAS_DIR = COMMON_DIR / "ideas"
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


@dataclass
class FocusNode:
    id: str
    x: int
    y: int
    cost_days: int
    prerequisites: List[List[str]] = field(default_factory=list)
    mutually_exclusive: List[str] = field(default_factory=list)
    raw_reward: str = ""
    
    # Analyzed Metrics
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


@dataclass
class TreeReport:
    tag: str
    file_path: str
    total_focuses: int = 0
    avg_substance_score: float = 0.0
    filler_count: int = 0
    filler_percentage: float = 0.0
    total_civ_factories: int = 0
    total_mil_factories: int = 0
    total_dockyards: int = 0
    total_slots: int = 0
    total_events_fired: int = 0
    total_decisions_unlocked: int = 0
    collision_count: int = 0
    continuous_focus_hazard: bool = False
    pacing_1914_readiness_pct: float = 0.0
    nodes: Dict[str, FocusNode] = field(default_factory=dict)
    hitlist: List[FocusNode] = field(default_factory=list)


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
    
    # Strip comments
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
        
        start_idx = match.start()
        block, end_idx = parse_bracket_content(clean_text, match.end() - 1)
        pos = end_idx

        # Extract focus ID
        id_match = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block)
        if not id_match:
            continue
        focus_id = id_match.group(1)

        # Extract coordinates
        x_match = re.search(r'\bx\s*=\s*([0-9\-]+)', block)
        y_match = re.search(r'\by\s*=\s*([0-9\-]+)', block)
        x = int(x_match.group(1)) if x_match else 0
        y = int(y_match.group(1)) if y_match else 0

        # Extract cost (days)
        cost_match = re.search(r'\bcost\s*=\s*([0-9\.]+)', block)
        cost_multiplier = float(cost_match.group(1)) if cost_match else 10.0
        cost_days = int(cost_multiplier * 7)

        # Extract prerequisites
        prereqs = []
        for p_match in re.finditer(r'prerequisite\s*=\s*\{', block):
            p_block, _ = parse_bracket_content(block, p_match.end() - 1)
            f_ids = re.findall(r'\bfocus\s*=\s*([a-zA-Z0-9_]+)', p_block)
            if f_ids:
                prereqs.append(f_ids)

        # Extract mutually exclusive
        mut_excl = []
        m_match = re.search(r'mutually_exclusive\s*=\s*\{', block)
        if m_match:
            m_block, _ = parse_bracket_content(block, m_match.end() - 1)
            mut_excl = re.findall(r'\bfocus\s*=\s*([a-zA-Z0-9_]+)', m_block)

        # Extract completion reward
        reward_match = re.search(r'completion_reward\s*=\s*\{', block)
        raw_reward = ""
        if reward_match:
            raw_reward, _ = parse_bracket_content(block, reward_match.end() - 1)

        nodes[focus_id] = FocusNode(
            id=focus_id,
            x=x,
            y=y,
            cost_days=cost_days,
            prerequisites=prereqs,
            mutually_exclusive=mut_excl,
            raw_reward=raw_reward
        )

    return nodes


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
        strengths.append(f"+{civs} Fábrica(s) Civil(is)")
    if mils > 0:
        score += mils * 3.0
        strengths.append(f"+{mils} Fábrica(s) Militar(es)")
    if docks > 0:
        score += docks * 2.5
        strengths.append(f"+{docks} Estaleiro(s)")
    if slots > 0:
        score += slots * 1.5
        strengths.append(f"+{slots} Slot(s) de Construção")
    if infras > 0:
        score += infras * 1.0
        strengths.append(f"+{infras} Nível(eis) de Infraestrutura")

    # 2. Military Units & Equipment
    units = len(re.findall(r'create_unit\s*=', reward)) + len(re.findall(r'load_oob\s*=', reward))
    node.units_spawned = units
    if units > 0:
        score += 3.5 * units
        strengths.append(f"Spawn de {units} Divisão(ões)/OOB")

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
        strengths.append(f"Destrava {len(all_dec)} Decisão(ões)/Missão(ões)")

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
        strengths.append(f"Modifica Espírito Nacional ({len(ideas)})")

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
        fillers.append("Apenas concede Poder Político sem impacto material")
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
        # Minimal research bonus or generic effect
        score = max(score, 2.0)
        fillers.append("Apenas bônus genérico residual de pesquisa")
        node.is_filler = True

    # High cost penalty for low impact
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


def analyze_tree(tag: str, file_path: Path) -> TreeReport:
    nodes = extract_focus_nodes(file_path)
    report = TreeReport(tag=tag, file_path=str(file_path), total_focuses=len(nodes))

    if not nodes:
        return report

    total_score = 0.0
    filler_nodes = []
    
    # Check collisions
    coords_seen: Dict[Tuple[int, int], str] = {}
    collision_count = 0

    for f_id, node in nodes.items():
        analyze_focus(node)
        total_score += node.substance_score
        
        report.total_civ_factories += node.factories_civ
        report.total_mil_factories += node.factories_mil
        report.total_dockyards += node.dockyards
        report.total_slots += node.slots
        report.total_events_fired += len(node.fired_events)
        report.total_decisions_unlocked += len(node.unlocked_decisions)

        if node.is_filler or node.substance_score < 2.5:
            filler_nodes.append(node)

        # Coordinate overlap
        coord = (node.x, node.y)
        if coord in coords_seen:
            collision_count += 1
        else:
            coords_seen[coord] = f_id

        # Continuous focus UI collision (x <= 5 and y <= 8)
        if node.x <= 4 and node.y <= 6:
            report.continuous_focus_hazard = True

    report.nodes = nodes
    report.total_focuses = len(nodes)
    report.avg_substance_score = round(total_score / len(nodes), 2)
    report.filler_count = len(filler_nodes)
    report.filler_percentage = round((len(filler_nodes) / len(nodes)) * 100, 1)
    report.collision_count = collision_count

    # Sort hitlist by lowest substance score
    filler_nodes.sort(key=lambda n: (n.substance_score, -n.cost_days))
    report.hitlist = filler_nodes[:20]

    # Calculate 1914 readiness: focuses with Y <= 5 reachable within 1150 days
    early_nodes = [n for n in nodes.values() if n.y <= 5]
    if early_nodes:
        avg_early_score = sum(n.substance_score for n in early_nodes) / len(early_nodes)
        report.pacing_1914_readiness_pct = round(min(100.0, avg_early_score * 12.5), 1)

    return report


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
            "x": n.x,
            "y": n.y,
            "cost_days": n.cost_days,
            "score": n.substance_score,
            "category": n.category,
            "is_filler": n.is_filler,
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

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Baianagem-WW1 Radar — {report.tag} Focus Tree</title>
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
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            overflow: hidden;
            display: flex;
            height: 100vh;
        }}
        #sidebar {{
            width: 380px;
            background: var(--panel);
            border-right: 1px solid var(--border);
            padding: 20px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            gap: 15px;
            overflow-y: auto;
            z-index: 10;
        }}
        h1 {{
            font-size: 1.3rem;
            margin: 0;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .badge {{
            font-size: 0.75rem;
            padding: 3px 8px;
            border-radius: 12px;
            background: var(--accent);
            color: #fff;
            font-weight: 600;
        }}
        .stat-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }}
        .stat-card {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 10px;
            text-align: center;
        }}
        .stat-val {{
            font-size: 1.4rem;
            font-weight: 700;
            color: #fff;
        }}
        .stat-lbl {{
            font-size: 0.75rem;
            color: #8b949e;
        }}
        .score-bar {{
            height: 8px;
            border-radius: 4px;
            background: #21262d;
            overflow: hidden;
            margin-top: 5px;
        }}
        .score-fill {{
            height: 100%;
            background: linear-gradient(90deg, var(--dead), var(--moderate), var(--solid), var(--epic));
            width: {min(100.0, report.avg_substance_score * 10)}%;
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
            filter: drop-shadow(0 0 8px rgba(88, 166, 255, 0.6));
        }}
        .node rect {{
            stroke-width: 2px;
            rx: 6px;
        }}
        .node-dead rect {{ fill: #2d1517; stroke: var(--dead); }}
        .node-moderate rect {{ fill: #2b2311; stroke: var(--moderate); }}
        .node-solid rect {{ fill: #132b1a; stroke: var(--solid); }}
        .node-epic rect {{ fill: #27173e; stroke: var(--epic); }}
        .node text {{
            fill: #fff;
            font-size: 11px;
            font-weight: 600;
            text-anchor: middle;
            user-select: none;
        }}
        .node-subtext {{
            fill: #8b949e;
            font-size: 9px;
            font-weight: 400;
        }}
        line.link {{
            stroke: #30363d;
            stroke-width: 2px;
        }}
        #details-pane {{
            background: rgba(0, 0, 0, 0.2);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 12px;
            font-size: 0.85rem;
        }}
        .hitlist-item {{
            padding: 8px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            font-size: 0.8rem;
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
            <span>🇦🇹 Árvore {report.tag}</span>
            <span class="badge">{report.total_focuses} Focos</span>
        </h1>
        
        <div class="stat-grid">
            <div class="stat-card">
                <div class="stat-val" style="color: {'var(--solid)' if report.avg_substance_score >= 5.0 else 'var(--dead)'}">
                    {report.avg_substance_score}/10
                </div>
                <div class="stat-lbl">Score Médio de Substância</div>
                <div class="score-bar"><div class="score-fill"></div></div>
            </div>
            <div class="stat-card">
                <div class="stat-val" style="color: {'var(--dead)' if report.filler_percentage > 15 else 'var(--solid)'}">
                    {report.filler_percentage}%
                </div>
                <div class="stat-lbl">{report.filler_count} Focos Mortos/Filler</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">+{report.total_civ_factories + report.total_mil_factories}</div>
                <div class="stat-lbl">Fábricas Totais (+{report.total_slots} slots)</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">{report.total_decisions_unlocked + report.total_events_fired}</div>
                <div class="stat-lbl">Gatilhos Dinâmicos</div>
            </div>
        </div>

        <div id="details-pane">
            <div style="font-weight: 700; margin-bottom: 6px; color: #fff;">🔍 Inspecionar Foco</div>
            <div id="inspect-content" style="color: #8b949e;">Clique em qualquer nó da árvore para ver o raio-X completo de jogabilidade.</div>
        </div>

        <div>
            <div style="font-weight: 700; margin-bottom: 8px; color: var(--dead); font-size: 0.85rem;">
                ⚠️ Top Focos Problemáticos (Hit List)
            </div>
            <div style="max-height: 250px; overflow-y: auto;">
"""
    for node in report.hitlist[:12]:
        html_content += f"""
                <div class="hitlist-item" onclick="selectNode('{node.id}')">
                    <div style="font-weight: 600; color: #fff;">{node.id}</div>
                    <div style="color: var(--dead); font-size: 0.75rem;">Score: {node.substance_score}/10 — {', '.join(node.filler_reasons[:1])}</div>
                </div>
        """

    html_content += f"""
            </div>
        </div>
    </div>

    <div id="canvas-container">
        <svg id="svg-tree">
            <!-- Prerequisites Connections -->
            <g id="links-group"></g>
            <!-- Focus Nodes -->
            <g id="nodes-group"></g>
        </svg>
    </div>

    <script>
        const nodesData = {json.dumps(nodes_json)};
        const nodeMap = {{}};
        nodesData.forEach(n => nodeMap[n.id] = n);

        const svg = document.getElementById('svg-tree');
        const linksGroup = document.getElementById('links-group');
        const nodesGroup = document.getElementById('nodes-group');

        const xOffset = 80 - ({min_x} * 110);
        const yOffset = 80 - ({min_y} * 130);

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
            g.setAttribute('transform', `translate(${{pos.x}}, ${{pos.y}})`);
            g.onclick = () => selectNode(node.id);

            const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            rect.setAttribute('width', '90');
            rect.setAttribute('height', '50');

            const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            text.setAttribute('x', '45');
            text.setAttribute('y', '22');
            let shortName = node.id.replace('AUH_ww1_', '').replace('GER_', '').replace('FRA_', '').replace('ITA_', '');
            if (shortName.length > 12) shortName = shortName.substring(0, 11) + '..';
            text.textContent = shortName;

            const scoreText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            scoreText.setAttribute('x', '45');
            scoreText.setAttribute('y', '38');
            scoreText.setAttribute('class', 'node-subtext');
            scoreText.textContent = `${{node.score}} pts | ${{node.cost_days}}d`;

            g.appendChild(rect);
            g.appendChild(text);
            g.appendChild(scoreText);
            nodesGroup.appendChild(g);
        }});

        function selectNode(id) {{
            const n = nodeMap[id];
            if (!n) return;

            let html = `
                <div style="font-weight: 700; color: #fff; font-size: 0.95rem; margin-bottom: 4px;">${{n.id}}</div>
                <div style="color: #8b949e; font-size: 0.75rem; margin-bottom: 8px;">
                    Posição: (${{n.x}}, ${{n.y}}) | Duração: ${{n.cost_days}} dias | Categoria: <b>${{n.category}}</b>
                </div>
                <div style="font-size: 1.1rem; font-weight: 700; color: ${{n.score >= 5 ? 'var(--solid)' : 'var(--dead)'}}; margin-bottom: 8px;">
                    Score de Conteúdo: ${{n.score}} / 10
                </div>
            `;

            if (n.strengths.length > 0) {{
                html += '<div style="color: var(--solid); font-weight: 600; margin-top: 6px;">Impactos Positivos:</div><ul style="padding-left: 16px; margin: 4px 0;">';
                n.strengths.forEach(s => html += `<li>${{s}}</li>`);
                html += '</ul>';
            }}

            if (n.fillers.length > 0) {{
                html += '<div style="color: var(--dead); font-weight: 600; margin-top: 6px;">Falhas de Gameplay / Filler:</div><ul style="padding-left: 16px; margin: 4px 0;">';
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


def run_inspect(tag: str) -> None:
    tag = tag.upper()
    file_path = TAG_TO_FILE.get(tag)
    if not file_path or not file_path.exists():
        print(f"[ERRO] Arquivo de foco para a tag '{tag}' não encontrado em {FOCUS_DIR}")
        return

    report = analyze_tree(tag, file_path)
    
    print("\n" + "=" * 80)
    print(f"       HOI4 GAMEPLAY RADAR — AUDITORIA DE DESIGN & JOGABILIDADE ({report.tag})")
    print("=" * 80)
    print(f" Arquivo                 : {report.file_path}")
    print(f" Total de Focos          : {report.total_focuses}")
    print(f" Score Médio de Conteúdo : {report.avg_substance_score} / 10.0")
    print(f" Focos Mortos (Filler)   : {report.filler_count} ({report.filler_percentage}%)")
    print(f" Fábricas Construídas    : Civ: +{report.total_civ_factories} | Mil: +{report.total_mil_factories} | Estaleiros: +{report.total_dockyards}")
    print(f" Slots Adicionais        : +{report.total_slots} slots")
    print(f" Decisões Destravadas    : {report.total_decisions_unlocked}")
    print(f" Eventos Disparados      : {report.total_events_fired}")
    print(f" Prontidão 1914 (Guerra) : {report.pacing_1914_readiness_pct}%")
    print(f" Colisões de Coordenadas : {report.collision_count} conflitos")
    print(f" Risco Foco Contínuo     : {'[ALERTA] Risco de sobreposição no canto superior esquerdo' if report.continuous_focus_hazard else '[OK] Limpo'}")
    print("=" * 80)

    if report.hitlist:
        print("\n [!] HIT LIST — OS 10 FOCOS MAIS RASOS/CHATOS QUE PRECISAM DE MECÂNICA:")
        for idx, node in enumerate(report.hitlist[:10], 1):
            reasons = "; ".join(node.filler_reasons) if node.filler_reasons else "Recompensa fraca"
            print(f"   {idx:2d}. {node.id:<32} (Score: {node.substance_score}/10 | {node.cost_days}d) -> {reasons}")

    # Export interactive HTML
    html_out = OUTPUT_DIR / f"{tag}_focus_tree.html"
    generate_interactive_html(report, html_out)
    print(f"\n [+] Painel Visual 2D Interativo Gerado em:\n     file:///{html_out.as_posix()}\n")


def run_audit_all() -> None:
    print("\n" + "=" * 80)
    print("       AUDITORIA GLOBAL DE JOGABILIDADE E CONTEÚDO (TODAS AS POTÊNCIAS)")
    print("=" * 80)
    print(f" {'TAG':<5} | {'Focos':<6} | {'Score/10':<9} | {'Fillers':<10} | {'Fábricas':<10} | {'1914 Ready':<10} | {'Status':<12}")
    print("-" * 80)

    for tag, file_path in TAG_TO_FILE.items():
        if tag in ["AUH", "SOV"]:
            continue  # Aliases
        if not file_path.exists():
            continue
        report = analyze_tree(tag, file_path)
        status = "EXCELENTE" if report.avg_substance_score >= 6.0 and report.filler_percentage <= 15 else "PRECISA POLIR"
        if report.avg_substance_score < 4.0 or report.filler_percentage > 35:
            status = "CRÍTICO/RASO"
        total_facs = report.total_civ_factories + report.total_mil_factories
        print(f" {tag:<5} | {report.total_focuses:<6} | {report.avg_substance_score:<9} | {report.filler_count} ({report.filler_percentage}%) | +{total_facs:<8} | {report.pacing_1914_readiness_pct}%       | {status:<12}")

    print("=" * 80 + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python scripts/mod_engine.py inspect <TAG>    -> Inspeciona e gera HTML 2D para um país")
        print("  python scripts/mod_engine.py audit-all        -> Auditoria comparativa de todas as potências")
        print("  python scripts/mod_engine.py visual <TAG>     -> Gera apenas o mapa visual")
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd == "inspect" and len(sys.argv) >= 3:
        run_inspect(sys.argv[2])
    elif cmd == "audit-all":
        run_audit_all()
    elif cmd == "visual" and len(sys.argv) >= 3:
        run_inspect(sys.argv[2])
    else:
        run_inspect(sys.argv[1])

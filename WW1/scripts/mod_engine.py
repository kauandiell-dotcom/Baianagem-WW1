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
 5. GFX Integrity, Missing Sprites & Image Dimensions (450x250, DDS/PNG).
 6. National Spirit Stacking, Top-Bar Clutter (>7 ideas) & Buff Inflation.
 7. Event Visualizer & Layout Inspector (HTML Parchment Simulation).
 8. Multiplayer Safety, Anti-Desync (OOS) & Daily Performance / Lag Telemetry.
 9. Interactive 2D Visual SVG/HTML Inspector with Phase Filters.
===============================================================================
"""

import os
import re
import sys
import json
import base64
import io
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Set, Optional, Tuple
from collections import Counter

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

ROOT_DIR = Path(__file__).resolve().parent.parent
COMMON_DIR = ROOT_DIR / "common"
FOCUS_DIR = COMMON_DIR / "national_focus"
DECISIONS_DIR = COMMON_DIR / "decisions"
EVENTS_DIR = ROOT_DIR / "events"
IDEAS_DIR = COMMON_DIR / "ideas"
CHARACTERS_DIR = COMMON_DIR / "characters"
INTERFACE_DIR = ROOT_DIR / "interface"
GFX_DIR = ROOT_DIR / "gfx"
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
    icon: str = ""
    prerequisites: List[List[str]] = field(default_factory=list)
    mutually_exclusive: List[str] = field(default_factory=list)
    raw_reward: str = ""
    raw_ai: str = ""
    
    # Phase Classification
    phase: int = 1  # 1: 1911-1914, 2: 1914-1916, 3: 1917-1920
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
    event_details: List[Dict[str, any]] = field(default_factory=list)
    gives_ideas: List[str] = field(default_factory=list)
    removes_ideas: List[str] = field(default_factory=list)
    is_filler: bool = False
    filler_reasons: List[str] = field(default_factory=list)
    strengths: List[str] = field(default_factory=list)

    # GFX & Visual Integrity
    is_icon_valid: bool = True
    icon_file: str = ""
    icon_warning: str = ""

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
class GFXAuditReport:
    total_sprites_defined: int = 0
    missing_texture_files: List[str] = field(default_factory=list)
    missing_focus_icons: List[str] = field(default_factory=list)
    missing_idea_icons: List[str] = field(default_factory=list)
    missing_event_pictures: List[str] = field(default_factory=list)
    invalid_dimension_event_pictures: List[str] = field(default_factory=list)


@dataclass
class SpiritStackingReport:
    tag: str
    starting_ideas: List[str] = field(default_factory=list)
    total_starting_count: int = 0
    max_simultaneous_estimate: int = 0
    has_topbar_overflow_risk: bool = False
    unpaired_ideas_added: List[str] = field(default_factory=list)
    powercreep_warnings: List[str] = field(default_factory=list)


@dataclass
class EventInspection:
    id: str
    file_name: str
    event_type: str = "country_event"  # "country_event" or "news_event"
    country_tag: str = ""
    picture_gfx: str = ""
    picture_file: str = ""
    is_picture_valid: bool = True
    picture_dims: Tuple[int, int] = (0, 0)
    title_key: str = ""
    desc_key: str = ""
    title_pt: str = ""
    desc_pt: str = ""
    desc_length: int = 0
    is_text_overflow_risk: bool = False
    options_count: int = 0
    options: List[Dict[str, any]] = field(default_factory=list)
    is_options_overflow_risk: bool = False
    warnings: List[str] = field(default_factory=list)
    
    # Event Substance & Gameplay Impact
    has_provisions: bool = False
    has_consent: bool = False
    has_cohesion: bool = False
    has_debt: bool = False
    has_tech_bonus: bool = False
    has_experience: bool = False
    has_political_power: bool = False
    has_timed_ideas: bool = False
    has_ideas: bool = False
    has_staff_effects: bool = False
    has_economic_tradeoffs: bool = False
    has_military_tradeoffs: bool = False
    has_diplomatic_tradeoffs: bool = False
    has_political_tradeoffs: bool = False
    raw_block: str = ""


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
    
    # 5 Authentic Gameplay Pillars (each 0.0 - 10.0)
    score_p1_specialization: float = 0.0   # Identidade & Especialização dos Ramos
    score_p2_mechanics: float = 0.0        # Integração Mecânica & Interatividade
    score_p3_balance: float = 0.0          # Equilíbrio & Anti-Powercreep
    score_p4_diversity: float = 0.0        # Diversidade de Design & Anti-Repetição
    score_p5_pacing: float = 0.0           # Ritmo & Prontidão de Guerra
    overall_gameplay_index: float = 0.0    # Índice Geral de Jogabilidade
    gameplay_tier: str = ""               # "Obra-Prima", "Sólido", "Moderado", "Crítico"
    
    # Wing Breakdown Diagnostics
    wing_metrics: Dict[str, Dict[str, any]] = field(default_factory=dict)
    distinct_signatures: int = 0
    max_signature_pct: float = 0.0
    cookie_cutter_warning: str = ""
    strengths_list: List[str] = field(default_factory=list)
    weaknesses_list: List[str] = field(default_factory=list)
    
    # 3-Phase Chronological Arc
    phase_1_count: int = 0
    phase_2_count: int = 0
    phase_3_count: int = 0
    phase_1_score: float = 0.0
    phase_2_score: float = 0.0
    phase_3_score: float = 0.0

    # Physical Map Rewards
    total_civ_factories: int = 0
    total_mil_factories: int = 0
    total_dockyards: int = 0
    total_slots: int = 0
    total_bunkers: int = 0
    total_events_fired: int = 0
    total_decisions_unlocked: int = 0
    total_variable_mods: int = 0
    total_tech_bonuses: int = 0
    
    # Ergonomics & Visual Collisions
    collision_count: int = 0
    continuous_focus_hazard: bool = False
    pacing_1914_readiness_pct: float = 0.0
    
    # AI & Loc Summary
    ai_coverage_pct: float = 0.0
    loc_coverage_pct: float = 0.0
    shallow_loc_count: int = 0

    # GFX & Spirit Health
    missing_icons_count: int = 0
    has_spirit_overflow: bool = False

    nodes: Dict[str, FocusNode] = field(default_factory=dict)
    hitlist: List[FocusNode] = field(default_factory=list)
    combat: Optional[CombatReport] = None
    spirits: Optional[SpiritStackingReport] = None


# =============================================================================
# GFX DATABASE ENGINE
# =============================================================================

class GFXDatabase:
    def __init__(self):
        self.sprites: Dict[str, str] = {}
        self.load_sprites()

    def load_sprites(self):
        if not INTERFACE_DIR.exists():
            return
        
        # Regex to capture name and texturefile in spriteType blocks
        sprite_block_re = re.compile(r'spriteType\s*=\s*\{([^\}]+(?:\{[^\}]*\}[^\}]*)*)\}', re.DOTALL)
        name_re = re.compile(r'name\s*=\s*\"?([a-zA-Z0-9_\-\.]+)\"?')
        tex_re = re.compile(r'texturefile\s*=\s*\"?([^\s\"\n\}]+)\"?', re.IGNORECASE)

        for gfx_file in INTERFACE_DIR.glob("*.gfx"):
            try:
                with open(gfx_file, "r", encoding="utf-8", errors="ignore") as f:
                    txt = f.read()
                for block_match in sprite_block_re.finditer(txt):
                    block = block_match.group(1)
                    n_match = name_re.search(block)
                    t_match = tex_re.search(block)
                    if n_match and t_match:
                        s_name = n_match.group(1)
                        s_path = t_match.group(1).replace("\\", "/").strip('"').strip("'")
                        self.sprites[s_name] = s_path
            except Exception:
                pass

    def resolve_sprite(self, sprite_name: str) -> Tuple[bool, str]:
        if sprite_name in self.sprites:
            rel_path = self.sprites[sprite_name]
            clean_rel = rel_path.lstrip("/")
            full_path = ROOT_DIR / clean_rel
            if full_path.exists():
                return True, str(clean_rel)
            return False, f"Definido no .gfx mas arquivo ausente: {rel_path}"
        return False, "Sprite nao declarado em nenhum arquivo .gfx"

    def get_image_dimensions(self, rel_path: str) -> Tuple[int, int]:
        if not HAS_PIL:
            return (0, 0)
        try:
            full_path = ROOT_DIR / rel_path.lstrip("/")
            if full_path.exists():
                with Image.open(full_path) as img:
                    return img.size
        except Exception:
            pass
        return (0, 0)


GLOBAL_GFX = GFXDatabase()


# =============================================================================
# LOCALIZATION ENGINE
# =============================================================================

class LocalizationDB:
    def __init__(self):
        self.pt_keys: Dict[str, str] = {}
        self.en_keys: Dict[str, str] = {}
        self.load_all()

    def load_all(self):
        pt_dir = LOCALISATION_DIR / "braz_por"
        if pt_dir.exists():
            for f in pt_dir.glob("*.yml"):
                self._load_file(f, self.pt_keys)
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


class EventDatabase:
    def __init__(self):
        self.events: Dict[str, EventInspection] = {}
        self.load_all()

    def load_all(self):
        if not EVENTS_DIR.exists():
            return
        e_pattern = re.compile(r'(country_event|news_event)\s*=\s*\{')
        for f in sorted(EVENTS_DIR.glob("*.txt")):
            if f.stat().st_size == 0:
                continue
            try:
                with open(f, "r", encoding="utf-8", errors="ignore") as fp:
                    text = fp.read()
            except Exception:
                continue

            pos = 0
            while True:
                m = e_pattern.search(text, pos)
                if not m:
                    break
                ev_type = m.group(1)
                block, end_idx = parse_bracket_content(text, m.end() - 1)
                pos = end_idx

                id_match = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\.]+)', block)
                if not id_match:
                    continue
                ev_id = id_match.group(1)

                pic_match = re.search(r'\bpicture\s*=\s*\"?([a-zA-Z0-9_]+)\"?', block)
                pic_gfx = pic_match.group(1) if pic_match else ""

                t_match = re.search(r'\btitle\s*=\s*\"?([a-zA-Z0-9_\.]+)\"?', block)
                d_match = re.search(r'\bdesc\s*=\s*\"?([a-zA-Z0-9_\.]+)\"?', block)
                title_key = t_match.group(1) if t_match else ""
                desc_key = d_match.group(1) if d_match else ""

                options = []
                has_prov = False
                has_cons = False
                has_cohe = False
                has_debt = False
                has_tech = False
                has_xp = False
                has_pp = False
                has_timed = False
                has_id = False
                has_staff = False

                for opt_match in re.finditer(r'\boption\s*=\s*\{', block):
                    o_block, _ = parse_bracket_content(block, opt_match.end() - 1)
                    name_m = re.search(r'\bname\s*=\s*\"?([a-zA-Z0-9_\.]+)\"?', o_block)
                    opt_key = name_m.group(1) if name_m else "Sem Nome"
                    opt_text = GLOBAL_LOC.pt_keys.get(opt_key, opt_key)
                    is_empty = not bool(re.search(r'[a-zA-Z0-9_]+\s*=', o_block))

                    effects = []
                    for var, val in re.findall(r'add_to_variable\s*=\s*\{\s*([a-zA-Z0-9_]+)\s*=\s*([0-9\.\-]+)', o_block):
                        sign = "+" if not val.startswith("-") else ""
                        if "provisions" in var:
                            effects.append(f"{sign}{val} Provisões")
                            has_prov = True
                        elif "consent" in var:
                            effects.append(f"{sign}{val} Consenso")
                            has_cons = True
                        elif "cohesion" in var:
                            effects.append(f"{sign}{val} Coesão")
                            has_cohe = True
                        elif "debt" in var:
                            effects.append(f"{sign}{val} Dívida")
                            has_debt = True
                        else:
                            effects.append(f"{sign}{val} {var}")

                    pp = re.findall(r'add_political_power\s*=\s*([0-9\-]+)', o_block)
                    if pp:
                        val = pp[0]
                        sign = "+" if not val.startswith("-") else ""
                        effects.append(f"{sign}{val} PP")
                        has_pp = True

                    xp = re.findall(r'(?:army|navy|air)_experience\s*=\s*([0-9]+)', o_block)
                    if xp:
                        effects.append(f"+{xp[0]} XP")
                        has_xp = True

                    tech = re.findall(r'category\s*=\s*([a-zA-Z0-9_]+)', o_block)
                    if tech:
                        effects.append(f"Pesquisa: {tech[0]}")
                        has_tech = True
                    elif "add_tech_bonus" in o_block:
                        effects.append("Bônus Tecnológico")
                        has_tech = True

                    timed = re.findall(r'add_timed_idea\s*=\s*\{\s*idea\s*=\s*([a-zA-Z0-9_]+)', o_block)
                    if timed:
                        effects.append(f"Ideia temporária: {timed[0]}")
                        has_timed = True

                    ideas = re.findall(r'add_ideas\s*=\s*([a-zA-Z0-9_]+)', o_block)
                    if ideas:
                        effects.append(f"+Ideia: {ideas[0]}")
                        has_id = True

                    if "auh_ww1_set_defensive_staff" in o_block:
                        effects.append("Estado-Maior Defensivo")
                        has_staff = True
                    elif "auh_ww1_set_offensive_staff" in o_block:
                        effects.append("Estado-Maior Ofensivo")
                        has_staff = True

                    flags = re.findall(r'set_country_flag\s*=\s*([a-zA-Z0-9_]+)', o_block)
                    if flags:
                        effects.append(f"Flag: {flags[0]}")

                    summary = ", ".join(effects) if effects else ("Efeito Diplomático/Narrativo" if o_block.strip() else "Vazia")
                    options.append({
                        "key": opt_key,
                        "text": opt_text,
                        "is_empty": is_empty,
                        "summary": summary,
                        "raw": o_block
                    })

                tag_hint = "AUS"
                if "ger" in ev_id.lower() or "germany" in f.name.lower(): tag_hint = "GER"
                elif "auh" in ev_id.lower() or "austria" in f.name.lower(): tag_hint = "AUS"
                elif "fra" in ev_id.lower() or "france" in f.name.lower(): tag_hint = "FRA"
                elif "ita" in ev_id.lower() or "italy" in f.name.lower(): tag_hint = "ITA"
                elif "eng" in ev_id.lower() or "uk" in f.name.lower() or "britain" in f.name.lower(): tag_hint = "ENG"
                elif "rus" in ev_id.lower() or "sov" in f.name.lower(): tag_hint = "RUS"
                elif "tur" in ev_id.lower() or "turkey" in f.name.lower(): tag_hint = "TUR"

                ev_obj = EventInspection(
                    id=ev_id,
                    file_name=f.name,
                    event_type=ev_type,
                    country_tag=tag_hint,
                    picture_gfx=pic_gfx,
                    title_key=title_key,
                    desc_key=desc_key,
                    title_pt=GLOBAL_LOC.pt_keys.get(title_key, title_key),
                    desc_pt=GLOBAL_LOC.pt_keys.get(desc_key, desc_key),
                    desc_length=len(GLOBAL_LOC.pt_keys.get(desc_key, desc_key)),
                    options_count=len(options),
                    options=options,
                    has_provisions=has_prov,
                    has_consent=has_cons,
                    has_cohesion=has_cohe,
                    has_debt=has_debt,
                    has_tech_bonus=has_tech,
                    has_experience=has_xp,
                    has_political_power=has_pp,
                    has_timed_ideas=has_timed,
                    has_ideas=has_id,
                    has_staff_effects=has_staff,
                    has_economic_tradeoffs=(has_prov or has_debt or has_timed or "economic" in ev_id.lower() or "bread" in ev_id.lower() or "food" in ev_id.lower() or "factory" in ev_id.lower() or "trade" in ev_id.lower()),
                    has_military_tradeoffs=(has_xp or has_tech or has_staff or "army" in ev_id.lower() or "military" in ev_id.lower() or "offensive" in ev_id.lower() or "corps" in ev_id.lower()),
                    has_diplomatic_tradeoffs=("channel" in ev_id.lower() or "mission" in ev_id.lower() or "peace" in ev_id.lower() or "treaty" in ev_id.lower() or "diplomacy" in f.name.lower()),
                    has_political_tradeoffs=(has_cons or has_cohe or has_pp or "council" in ev_id.lower() or "audit" in ev_id.lower() or "constitution" in ev_id.lower() or "reform" in ev_id.lower()),
                    raw_block=block
                )

                # Validate Picture GFX
                if pic_gfx:
                    valid, path_or_msg = GLOBAL_GFX.resolve_sprite(pic_gfx)
                    ev_obj.is_picture_valid = valid
                    if valid:
                        ev_obj.picture_file = path_or_msg
                        dims = GLOBAL_GFX.get_image_dimensions(path_or_msg)
                        ev_obj.picture_dims = dims
                        if ev_obj.event_type == "news_event":
                            aspect = (dims[0] / dims[1]) if dims[1] > 0 else 0
                            if abs(aspect - 2.57) > 0.35 and dims != (0, 0):
                                ev_obj.warnings.append(f"⚠️ Tarjas Pretas / Letterbox: Dimensões ({dims[0]}x{dims[1]}, proporção {aspect:.2f}:1). O visor de jornal espera ~2.57:1 (399x155px). Causará faixas pretas laterais no jogo!")
                        else:
                            if dims != (0, 0) and dims != (450, 250) and dims != (156, 210) and dims != (400, 160):
                                ev_obj.warnings.append(f"Dimensões fora do padrão ({dims[0]}x{dims[1]}). Risco de barras pretas ou esticamento.")
                    else:
                        ev_obj.warnings.append(f"GFX da imagem inexistente: {path_or_msg}")
                else:
                    ev_obj.warnings.append("Evento sem imagem declarada ('picture = GFX_...')")

                # Validate Text Length
                max_char_limit = 750 if ev_type == "news_event" else 550
                if ev_obj.desc_length > max_char_limit:
                    ev_obj.is_text_overflow_risk = True
                    ev_obj.warnings.append(f"Texto muito longo ({ev_obj.desc_length} chars).")

                if ev_obj.options_count > 4:
                    ev_obj.is_options_overflow_risk = True
                    ev_obj.warnings.append(f"Muitas opções ({ev_obj.options_count}).")

                for o in options:
                    if o["is_empty"]:
                        ev_obj.warnings.append(f"Opção '{o['key']}' sem efeito prático")

                self.events[ev_id] = ev_obj


GLOBAL_EVENTS = EventDatabase()


def extract_focus_nodes(file_path: Path) -> Dict[str, FocusNode]:
    if not file_path.exists():
        return {}

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    nodes: Dict[str, FocusNode] = {}
    clean_lines = [line[:line.index("#")] if "#" in line else line for line in text.splitlines()]
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

        icon_match = re.search(r'\bicon\s*=\s*\"?([a-zA-Z0-9_]+)\"?', block)
        icon = icon_match.group(1) if icon_match else ""

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
            icon=icon,
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
# SUBSTANCE, GFX & LOC SCORING
# =============================================================================

def analyze_focus(node: FocusNode) -> None:
    reward = node.raw_reward
    x = node.x
    y = node.y
    cost = node.cost_days
    
    # 1. Determine Wing Role
    if node.id.startswith('ENG_'):
        if x <= 15:
            wing = 'POLITICAL'
        elif 16 <= x <= 38:
            wing = 'ECONOMIC'
        elif 44 <= x <= 62:
            wing = 'DIPLOMACY'
        elif 63 <= x <= 86:
            wing = 'NAVY'
        elif 87 <= x <= 104:
            wing = 'ARMY'
        else:
            wing = 'POSTWAR'
    elif node.id.startswith('ITA_'):
        if x <= 16:
            wing = 'POLITICAL'
        elif 17 <= x <= 38:
            wing = 'ECONOMIC'
        elif 39 <= x <= 56:
            wing = 'DIPLOMACY'
        elif 57 <= x <= 77 or 88 <= x <= 94:
            wing = 'ARMY'
        elif 78 <= x <= 87:
            wing = 'NAVY'
        else:
            wing = 'POSTWAR'
    elif x <= 10:
        wing = 'POLITICAL'
    elif 16 <= x <= 38:
        wing = 'ECONOMIC'
    elif 44 <= x <= 62:
        wing = 'ARMY'
    elif 68 <= x <= 86:
        wing = 'DIPLOMACY'
    elif 92 <= x <= 102:
        wing = 'NAVY'
    else:
        wing = 'POSTWAR'
        
    score = 5.0 # Neutral baseline for a functional 35-day focus
    strengths = []
    fillers = []
    
    # Physical Assets
    civs = len(re.findall(r'industrial_complex\s*=\s*[1-9]', reward)) + len(re.findall(r'type\s*=\s*industrial_complex', reward))
    mils = len(re.findall(r'arms_factory\s*=\s*[1-9]', reward)) + len(re.findall(r'type\s*=\s*arms_factory', reward))
    docks = len(re.findall(r'dockyard\s*=\s*[1-9]', reward)) + len(re.findall(r'type\s*=\s*dockyard', reward))
    slots = len(re.findall(r'add_extra_state_shared_building_slots\s*=\s*[1-9]', reward))
    infras = len(re.findall(r'infrastructure\s*=\s*[1-9]', reward)) + len(re.findall(r'type\s*=\s*infrastructure', reward))
    bunkers = len(re.findall(r'bunker\s*=\s*[1-9]', reward)) + len(re.findall(r'type\s*=\s*(?:bunker|coastal_bunker)', reward))
    resources = len(re.findall(r'add_resource\s*=', reward))
    
    node.factories_civ = civs
    node.factories_mil = mils
    node.dockyards = docks
    node.slots = slots
    
    # Interactive Systems
    tech_bonuses = len(re.findall(r'add_tech_bonus\s*=', reward))
    raw_ev1 = re.findall(r'(?:country_event|news_event)\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_\.]+)', reward)
    raw_ev2 = re.findall(r'(?:country_event|news_event)\s*=\s*([a-zA-Z0-9_\.]+)', reward)
    events = []
    for e in raw_ev1 + raw_ev2:
        if e not in events and e not in ('{', 'id'):
            events.append(e)
    node.fired_events = events

    # Resolve linked event models and gameplay impact
    node.event_details = []
    node_event_objs = []
    for ev_id in events:
        ev_obj = GLOBAL_EVENTS.events.get(ev_id)
        if ev_obj:
            node_event_objs.append(ev_obj)
            node.event_details.append({
                "id": ev_obj.id,
                "title": ev_obj.title_pt or ev_obj.title_key,
                "options_count": ev_obj.options_count,
                "options": [{"text": o["text"], "summary": o.get("summary", "")} for o in ev_obj.options]
            })

    decisions = re.findall(r'activate_mission\s*=\s*([a-zA-Z0-9_]+)', reward)
    dec_cats = re.findall(r'unlocks_decision_category\s*=\s*([a-zA-Z0-9_]+)', reward)
    add_dec = re.findall(r'add_decision\s*=\s*([a-zA-Z0-9_]+)', reward)
    all_dec = list(set(decisions + dec_cats + add_dec))
    node.unlocked_decisions = all_dec
    
    ideas_add = re.findall(r'add_ideas\s*=\s*([a-zA-Z0-9_]+)', reward)
    ideas_rem = re.findall(r'remove_ideas\s*=\s*([a-zA-Z0-9_]+)', reward)
    node.gives_ideas = ideas_add
    node.removes_ideas = ideas_rem
    
    scripted_ideas = re.findall(r'(auh_ww1_set_[a-zA-Z0-9_]+)\s*=', reward)
    flags = re.findall(r'set_country_flag\s*=\s*([a-zA-Z0-9_]+)', reward)
    vars_mod = re.findall(r'add_to_variable\s*=\s*\{\s*([a-zA-Z0-9_]+)', reward)
    
    xp_match = re.findall(r'(?:add_)?(?:army|navy|air)_experience\s*=\s*([0-9]+)', reward)
    xp_val = sum(int(x) for x in xp_match) if xp_match else 0
    
    cp_match = re.findall(r'add_command_power\s*=\s*([0-9]+)', reward)
    cp_val = sum(int(x) for x in cp_match) if cp_match else 0
    
    pp_match = re.findall(r'add_political_power\s*=\s*([0-9\-]+)', reward)
    pp_val = sum(int(x) for x in pp_match) if pp_match else 0
    
    if not reward.strip():
        node.substance_score = 0.5
        node.category = "Dead/Filler"
        node.is_filler = True
        node.filler_reasons = ["Foco 100% Vazio"]
        return

    # Role Fidelity Evaluation
    if wing == 'POLITICAL':
        if len(vars_mod) > 0:
            score += 1.5; strengths.append(f"Mecânica Imperial ({len(vars_mod)} ajuste(s) de consenso/coesão)")
        if len(scripted_ideas) > 0:
            score += 1.5; strengths.append("Reforma de Estrutura Constitucional/Gabinete")
        if len(events) > 0:
            ev_first = node_event_objs[0] if node_event_objs else None
            opt_info = f" ({ev_first.options_count} opções de deliberação)" if ev_first else ""
            ev_title = f" '{ev_first.title_pt}'" if ev_first and ev_first.title_pt else f" '{events[0]}'"
            score += 1.8; strengths.append(f"Deliberação Política via Evento{ev_title}{opt_info}")
        if pp_val >= 20:
            score += 0.8; strengths.append(f"+{pp_val} Poder Político")
        if civs > 0 or slots > 0:
            score += 1.0; strengths.append("Expansão administrativa regional")
        if not (vars_mod or scripted_ideas or events or pp_val >= 20):
            score -= 1.5; fillers.append("Foco político sem impacto no regime ou consenso")

    elif wing == 'ECONOMIC':
        if civs > 0 or mils > 0 or docks > 0:
            score += 1.8; strengths.append(f"Expansão fabril/estaleiros (+{civs} civ, +{mils} mil, +{docks} dock)")
        if resources > 0:
            score += 1.5; strengths.append(f"Prospecção de recursos ({resources})")
        if infras > 0 or slots > 0 or 'build_railway' in reward:
            score += 1.0; strengths.append(f"Logística e infraestrutura (+{infras} infra, +{slots} slots)")
        if 'provisions' in reward:
            score += 1.5; strengths.append("Abastecimento alimentar / mitigação de fome")
        if tech_bonuses > 0:
            score += 1.0; strengths.append("Pesquisa de modernização industrial")
        if len(ideas_add) > 0:
            score += 1.2; strengths.append(f"Regime/Instituição Econômica ({', '.join(ideas_add)})")
        if len(vars_mod) > 0:
            score += 1.0; strengths.append(f"Gestão Fiscal e Dívida ({len(vars_mod)} ajustes)")
        
        # Check event-driven economic governance
        ev_econ = [e for e in node_event_objs if e.has_economic_tradeoffs or e.has_provisions or e.options_count >= 2 or "economic" in e.id.lower() or "eco" in e.id.lower() or "food" in e.id.lower() or "bread" in e.id.lower() or "factory" in e.id.lower()]
        if ev_econ:
            e_first = ev_econ[0]
            score += 1.8
            strengths.append(f"Governança Econômica via Evento '{e_first.id}' ({e_first.options_count} opções de gestão)")
        
        if not (civs or mils or docks or resources or infras or slots or 'build_railway' in reward or 'provisions' in reward or tech_bonuses or ideas_add or vars_mod or ev_econ):
            score -= 1.5; fillers.append("Foco econômico sem impacto material tangível")

    elif wing == 'ARMY':
        if tech_bonuses > 0:
            score += 1.5; strengths.append(f"+{tech_bonuses} Bônus de doutrina/armamento")
        if bunkers > 0:
            score += 1.8; strengths.append(f"Fortificação de setor de fronteira ({bunkers} níveis)")
        if mils > 0:
            score += 1.8; strengths.append(f"Arsenais militares (+{mils} fábricas de armas)")
        if xp_val >= 15:
            score += 1.0; strengths.append(f"+{xp_val} Experiência militar")
        if cp_val >= 15:
            score += 0.8; strengths.append(f"+{cp_val} Poder de comando")
        if len(scripted_ideas) > 0:
            score += 1.5; strengths.append("Reforma militar de línguas / estado-maior")
        
        # Check event-driven army review / war council
        ev_army = [e for e in node_event_objs if e.has_military_tradeoffs or e.has_staff_effects or e.has_experience or e.has_tech_bonus or e.options_count >= 2 or "army" in e.id.lower() or "war" in e.id.lower() or "military" in e.id.lower()]
        if ev_army:
            e_first = ev_army[0]
            score += 1.8
            strengths.append(f"Conselho de Guerra / Auditoria Estratégica via Evento '{e_first.id}' ({e_first.options_count} opções)")
        
        if not (tech_bonuses or bunkers or mils or xp_val >= 15 or scripted_ideas or ev_army):
            score -= 1.5; fillers.append("Foco militar sem benefício tático operacional")

    elif wing == 'NAVY':
        if docks > 0:
            score += 1.8; strengths.append(f"Expansão de estaleiros (+{docks})")
        if bunkers > 0:
            score += 1.8; strengths.append("Baterias costeiras no Adriático (anti-invasão)")
        if tech_bonuses > 0:
            score += 1.5; strengths.append("Pesquisa de frota / doutrina naval")
        if xp_val >= 15:
            score += 1.0; strengths.append(f"+{xp_val} XP Naval")
        
        ev_navy = [e for e in node_event_objs if e.has_tech_bonus or e.options_count >= 2 or "naval" in e.id.lower() or "fleet" in e.id.lower() or "admiralty" in e.id.lower() or "marine" in e.id.lower()]
        if ev_navy:
            e_first = ev_navy[0]
            score += 1.8
            strengths.append(f"Conselho da Armada / Programa Naval via Evento '{e_first.id}' ({e_first.options_count} opções)")

        if not (docks or bunkers or tech_bonuses or xp_val >= 15 or ev_navy):
            score -= 1.5; fillers.append("Foco naval sem impacto na Kriegsmarine")

    elif wing == 'DIPLOMACY':
        if len(events) > 0:
            ev_first = node_event_objs[0] if node_event_objs else None
            opt_info = f" ({ev_first.options_count} opções)" if ev_first else ""
            score += 1.8; strengths.append(f"Canal Diplomático via Evento '{events[0]}'{opt_info}")
        if len(flags) > 0 or len(scripted_ideas) > 0:
            score += 1.2; strengths.append("Pacto geopolítico / alinhamento")
        if pp_val >= 10:
            score += 0.8; strengths.append(f"+{pp_val} Poder Político para influência")
        if len(vars_mod) > 0:
            score += 1.2; strengths.append(f"Gestão de minorias e consenso ({len(vars_mod)})")
        if civs > 0 or 'provisions' in reward:
            score += 1.2; strengths.append("Tratado comercial / abastecimento bilateral")
        if bunkers > 0 or mils > 0 or xp_val >= 15 or tech_bonuses > 0:
            score += 1.2; strengths.append("Acordo militar / contingência de fronteira")
        if not (events or flags or scripted_ideas or vars_mod or civs or 'provisions' in reward or bunkers or pp_val >= 10):
            score -= 1.5; fillers.append("Foco diplomático sem interação bilateral")

    else: # POSTWAR
        if civs > 0 or mils > 0:
            score += 1.5; strengths.append("Reconstrução industrial pós-guerra")
        if len(vars_mod) > 0:
            score += 1.5; strengths.append("Consolidação da coesão do império pós-guerra")
        if len(events) > 0:
            ev_first = node_event_objs[0] if node_event_objs else None
            opt_info = f" ({ev_first.options_count} opções)" if ev_first else ""
            score += 1.5; strengths.append(f"Decisão Constitucional Pós-Guerra via Evento '{events[0]}'{opt_info}")

    # Anti-chimera check: penalize artificial kitchen-sink formula
    is_chimera = (civs > 0 and mils > 0 and tech_bonuses > 0 and len(vars_mod) > 0 and xp_val > 0)
    if is_chimera:
        score = min(score, 7.0)
        fillers.append("Fórmula artificial genérica (Kitchen-sink Chimera)")

    node.substance_score = round(max(1.0, min(10.0, score)), 1)
    node.strengths = strengths
    node.filler_reasons = fillers

    if node.substance_score >= 7.5:
        node.category = "Epic"
    elif node.substance_score >= 5.5:
        node.category = "Solid"
    elif node.substance_score >= 3.5:
        node.category = "Moderate"
    else:
        node.category = "Dead/Filler"
        node.is_filler = True

    # 8. GFX Icon Integrity
    if node.icon:
        valid, msg = GLOBAL_GFX.resolve_sprite(node.icon)
        node.is_icon_valid = valid
        node.icon_file = msg
        if not valid:
            node.icon_warning = msg
    else:
        node.is_icon_valid = False
        node.icon_warning = "Foco sem declaracao de 'icon = GFX_...'"

    # 9. AI Behavior
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

    # 10. Localization
    node.has_loc_pt = node.id in GLOBAL_LOC.pt_keys
    node.has_loc_en = node.id in GLOBAL_LOC.en_keys
    node.loc_pt_title = GLOBAL_LOC.pt_keys.get(node.id, node.id)
    desc_key = f"{node.id}_desc"
    desc_text = GLOBAL_LOC.pt_keys.get(desc_key, "")
    node.loc_pt_desc_len = len(desc_text)
    if not node.has_loc_pt or node.loc_pt_desc_len < 25:
        node.is_loc_shallow = True


# =============================================================================
# NATIONAL SPIRIT STACKING & POWERCREEP AUDIT
# =============================================================================

def analyze_spirits(tag: str, tree_nodes: Dict[str, FocusNode]) -> SpiritStackingReport:
    history_file = TAG_TO_HISTORY.get(tag)
    report = SpiritStackingReport(tag=tag)

    if history_file and history_file.exists():
        with open(history_file, "r", encoding="utf-8", errors="ignore") as f:
            h_text = f.read()
        ideas_match = re.search(r'add_ideas\s*=\s*\{([^}]+)\}', h_text)
        if ideas_match:
            ideas = re.findall(r'([a-zA-Z0-9_]+)', ideas_match.group(1))
            report.starting_ideas = ideas
            report.total_starting_count = len(ideas)

    # Count focuses that add ideas without removing
    unpaired = []
    total_added = 0
    for node in tree_nodes.values():
        if node.gives_ideas and not node.removes_ideas:
            for idea_id in node.gives_ideas:
                unpaired.append(f"{node.id} -> adiciona '{idea_id}' sem remover ideia antiga")
                total_added += 1

    report.unpaired_ideas_added = unpaired
    # Top-bar overflow estimate: Starting ideas + added ideas
    report.max_simultaneous_estimate = report.total_starting_count + total_added
    if report.total_starting_count >= 6:
        report.has_topbar_overflow_risk = True
        report.powercreep_warnings.append(f"Comeco de jogo com {report.total_starting_count} ideias ativas. Risco de poluir a barra superior.")

    return report


# =============================================================================
# EVENT VISUALIZER & LAYOUT INSPECTOR
# =============================================================================

def load_asset_b64(filename: str) -> str:
    path = SCRIPTS_DIR / "visual_radar" / "assets" / filename
    if path.exists():
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")
    return ""


def load_image_b64(rel_path: str) -> str:
    if not rel_path:
        return ""
    full_path = ROOT_DIR / rel_path.lstrip("/")
    if not full_path.exists():
        return ""
    try:
        if HAS_PIL:
            with Image.open(full_path) as im:
                buf = io.BytesIO()
                im.save(buf, format="PNG")
                return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")
    except Exception:
        pass
    return ""


def inspect_event(event_id: str) -> Optional[EventInspection]:
    return GLOBAL_EVENTS.events.get(event_id)


def generate_event_preview_html(event: EventInspection, output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Load Clausewitz Textures
    news_bg_b64 = load_asset_b64("event_news_bg.png")
    news_overlay_b64 = load_asset_b64("event_news_pic_overlay.png")
    top_win_b64 = load_asset_b64("event_report_top_win.png")
    mid_win_b64 = load_asset_b64("event_report_tileable_midsection.png")
    bot_win_b64 = load_asset_b64("event_report_bottom_win.png")
    option_entry_b64 = load_asset_b64("event_option_entry.png")
    pic_clip_b64 = load_asset_b64("event_pic_clip.png")
    
    # Load Event Picture
    img_b64 = load_image_b64(event.picture_file)

    # Format Warnings for HUD
    warnings_html = ""
    if event.warnings:
        warnings_html = '<div class="hud-warnings"><h4>⚠️ Alertas de Composição Visual</h4><ul>'
        for w in event.warnings:
            warnings_html += f'<li>{w}</li>'
        warnings_html += '</ul></div>'
    else:
        warnings_html = '<div class="hud-ok">✅ Nenhum bug de proporção, texto ou GFX detectado!</div>'

    # Differentiate news_event vs country_event
    if event.event_type == "news_event":
        # Render News Event Window (Authentic "World News" folded newspaper)
        img_tag = f'<img class="news-event-img" src="{img_b64}" alt="{event.picture_gfx}">' if img_b64 else '<div class="missing-img">[GFX AUSENTE]</div>'
        
        options_html = ""
        for opt in event.options:
            empty_badge = ' <span style="color: #ff6b6b; font-size: 0.75rem;">(Vazia!)</span>' if opt["is_empty"] else ""
            options_html += f"""
            <button class="news-btn">
                <span>{opt['text']}{empty_badge}</span>
            </button>
            """

        event_window_html = f"""
        <div class="news-window" style="background-image: url('{news_bg_b64}');">
            <div class="news-pic-wrapper">
                {img_tag}
                <img class="news-overlay-img" src="{news_overlay_b64}" alt="frame">
            </div>
            <div class="news-title">{event.title_pt}</div>
            <div class="news-body">{event.desc_pt}</div>
            <div class="news-options">
                {options_html}
            </div>
        </div>
        """
    else:
        # Render Country Event Window (Authentic Dispatch Clipboard / Pasta de Despacho)
        img_tag = f'<img class="country-event-img" src="{img_b64}" alt="{event.picture_gfx}">' if img_b64 else '<div class="missing-img">[GFX AUSENTE]</div>'
        
        options_html = ""
        for opt in event.options:
            empty_badge = ' <span style="color: #ff6b6b; font-size: 0.72rem;">(Vazia!)</span>' if opt["is_empty"] else ""
            options_html += f"""
            <button class="country-btn" style="background-image: url('{option_entry_b64}');">
                <span>{opt['text']}{empty_badge}</span>
            </button>
            """

        event_window_html = f"""
        <div class="country-window">
            <div class="country-top" style="background-image: url('{top_win_b64}');">
                <div class="country-title">{event.title_pt}</div>
            </div>
            <div class="country-mid" style="background-image: url('{mid_win_b64}');">
                <div class="country-body">{event.desc_pt}</div>
            </div>
            <div class="country-bot" style="background-image: url('{bot_win_b64}');">
                <div class="country-pic-container">
                    <img class="country-clip" src="{pic_clip_b64}" alt="clip">
                    {img_tag}
                </div>
                <div class="country-options">
                    {options_html}
                </div>
            </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>HoI4 In-Game Simulator — {event.id}</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        body {{
            background: #0d1117;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: #c9d1d9;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }}

        /* TOPBAR DO HOI4 */
        .hoi4-topbar {{
            height: 36px;
            background: linear-gradient(180deg, #2b313a 0%, #171b21 100%);
            border-bottom: 2px solid #4a3e2c;
            display: flex;
            align-items: center;
            padding: 0 16px;
            font-size: 0.8rem;
            color: #dcd0b8;
            gap: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.6);
            z-index: 10;
        }}
        .topbar-flag {{
            font-size: 1.1rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .topbar-stat {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        .stat-val {{
            color: #79c0ff;
            font-weight: 600;
        }}

        /* MAP VIEWPORT & EVENT STAGE */
        .hoi4-viewport {{
            flex: 1;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px 20px;
            background: 
                radial-gradient(circle at center, rgba(30, 41, 59, 0.4) 0%, rgba(10, 15, 22, 0.88) 100%),
                repeating-linear-gradient(45deg, rgba(255,255,255,0.015) 0, rgba(255,255,255,0.015) 1px, transparent 0, transparent 40px),
                #141923;
        }}

        /* ======================================================== */
        /* NEWS EVENT (WORLD NEWS FOLDED NEWSPAPER) */
        /* ======================================================== */
        .news-window {{
            width: 528px;
            height: 595px;
            background-repeat: no-repeat;
            background-position: center top;
            background-size: 528px 595px;
            position: relative;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.92), 0 0 0 1px rgba(0,0,0,0.5);
            user-select: none;
            flex-shrink: 0;
        }}
        .news-pic-wrapper {{
            position: absolute;
            left: 59px;
            top: 91px;
            width: 400px;
            height: 155px;
            background: #111;
            overflow: hidden;
        }}
        .news-event-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: grayscale(80%) contrast(115%) sepia(15%);
        }}
        .news-overlay-img {{
            position: absolute;
            left: 0;
            top: 0;
            width: 400px;
            height: 155px;
            pointer-events: none;
        }}
        .news-title {{
            position: absolute;
            left: 14px;
            top: 256px;
            width: 495px;
            text-align: center;
            font-family: "Georgia", "Baskerville", "Times New Roman", serif;
            font-size: 19px;
            font-weight: 700;
            color: #17130f;
            letter-spacing: 0.3px;
        }}
        .news-body {{
            position: absolute;
            left: 39px;
            top: 295px;
            width: 450px;
            max-height: 200px;
            overflow-y: auto;
            font-family: "Courier New", Courier, monospace;
            font-size: 13.5px;
            line-height: 1.45;
            color: #241c14;
            text-align: justify;
            white-space: pre-line;
            padding-right: 6px;
        }}
        .news-options {{
            position: absolute;
            left: 80px;
            bottom: 25px;
            width: 368px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            align-items: center;
        }}
        .news-btn {{
            width: 352px;
            height: 48px;
            background: url('{option_entry_b64}') no-repeat center;
            background-size: 352px 48px;
            border: none;
            outline: none;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 13.5px;
            font-weight: 700;
            color: #e6dac0;
            text-shadow: 0 2px 2px #000;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 0 16px;
            transition: filter 0.1s ease, transform 0.05s ease;
        }}
        .news-btn:hover {{
            filter: brightness(1.2);
            transform: scale(1.01);
        }}

        /* ======================================================== */
        /* COUNTRY EVENT (DOSSIER / DISPATCH CLIPBOARD) */
        /* ======================================================== */
        .country-window {{
            width: 581px;
            display: flex;
            flex-direction: column;
            box-shadow: 0 25px 65px rgba(0, 0, 0, 0.95), 0 0 0 1px rgba(0,0,0,0.6);
            user-select: none;
            position: relative;
            flex-shrink: 0;
        }}
        .country-top {{
            width: 581px;
            height: 121px;
            background-repeat: no-repeat;
            background-position: center top;
            background-size: 581px 121px;
            position: relative;
            flex-shrink: 0;
        }}
        .country-title {{
            position: absolute;
            left: 14px;
            top: 70px;
            width: 551px;
            text-align: center;
            font-family: "Courier New", Courier, monospace;
            font-size: 20px;
            font-weight: 700;
            color: #211912;
            text-shadow: 0 1px 0 rgba(255,255,255,0.4);
        }}
        .country-mid {{
            width: 580px;
            background-repeat: repeat-y;
            background-position: center top;
            background-size: 580px 66px;
            box-sizing: border-box;
            padding: 8px 36px 16px 36px;
        }}
        .country-body {{
            font-family: "Courier New", Courier, monospace;
            font-size: 14.5px;
            line-height: 1.45;
            color: #261d15;
            text-align: left;
            white-space: pre-line;
        }}
        .country-bot {{
            width: 581px;
            height: 206px;
            background-repeat: no-repeat;
            background-position: center top;
            background-size: 581px 206px;
            position: relative;
            flex-shrink: 0;
        }}
        .country-pic-container {{
            position: absolute;
            left: 20px;
            top: 15px;
            width: 228px;
            height: 165px;
            background: #0f0d0b;
            border: 2px solid #5a4b37;
            box-shadow: 0 4px 10px rgba(0,0,0,0.6);
            overflow: hidden;
        }}
        .country-event-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: sepia(35%) contrast(108%) brightness(95%);
        }}
        .country-clip {{
            position: absolute;
            top: -2px;
            left: 8px;
            width: 45px;
            z-index: 5;
            pointer-events: none;
        }}
        .country-options {{
            position: absolute;
            left: 255px;
            top: 15px;
            width: 310px;
            height: 175px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 8px;
        }}
        .country-btn {{
            width: 295px;
            height: 44px;
            background-repeat: no-repeat;
            background-position: center;
            background-size: 295px 44px;
            border: none;
            outline: none;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 13px;
            font-weight: 700;
            color: #dfd2af;
            text-shadow: 0 2px 2px #000;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 0 14px;
            transition: filter 0.1s ease, transform 0.05s ease;
        }}
        .country-btn:hover {{
            filter: brightness(1.2);
            transform: scale(1.01);
        }}

        .missing-img {{
            width: 100%;
            height: 100%;
            background: #1c1510;
            color: #a89476;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            text-align: center;
            padding: 10px;
        }}

        /* HUD TELEMETRY SIDEBAR */
        .hud-panel {{
            position: absolute;
            top: 50px;
            right: 25px;
            width: 340px;
            background: rgba(18, 22, 28, 0.94);
            border: 1px solid #30363d;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
            padding: 16px;
            font-size: 0.8rem;
            backdrop-filter: blur(8px);
            z-index: 20;
        }}
        .hud-header {{
            font-weight: 700;
            color: #f0f6fc;
            font-size: 0.95rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            border-bottom: 1px solid #30363d;
            padding-bottom: 8px;
        }}
        .hud-badge {{
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 0.72rem;
            font-weight: 700;
            background: #238636;
            color: #fff;
        }}
        .hud-row {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 6px;
            color: #8b949e;
        }}
        .hud-val {{
            color: #c9d1d9;
            font-weight: 600;
        }}
        .hud-warnings {{
            margin-top: 12px;
            padding: 10px;
            background: rgba(248, 81, 73, 0.12);
            border: 1px solid #f85149;
            border-radius: 6px;
        }}
        .hud-warnings h4 {{
            color: #f85149;
            font-size: 0.82rem;
            margin-bottom: 4px;
        }}
        .hud-warnings ul {{
            padding-left: 16px;
            margin: 0;
            color: #e6edf3;
            font-size: 0.75rem;
        }}
        .hud-ok {{
            margin-top: 12px;
            padding: 8px;
            background: rgba(46, 160, 67, 0.12);
            border: 1px solid #2ea043;
            border-radius: 6px;
            color: #3fb950;
            font-weight: 600;
            font-size: 0.78rem;
            text-align: center;
        }}
    </style>
</head>
<body>
    <!-- TOPBAR HOI4 -->
    <div class="hoi4-topbar">
        <div class="topbar-flag">
            <span>{'🇦🇹' if event.country_tag == 'AUS' else '🇩🇪'}</span>
            <span>{event.country_tag}</span>
        </div>
        <div class="topbar-stat">📅 <span class="stat-val">12 Jul, 1914</span></div>
        <div class="topbar-stat">⚖️ PP: <span class="stat-val">+414</span></div>
        <div class="topbar-stat">🕊️ Estabilidade: <span class="stat-val">76%</span></div>
        <div class="topbar-stat">⚔️ Guerra: <span class="stat-val">67%</span></div>
        <div class="topbar-stat">🏭 Fábricas: <span class="stat-val">90</span></div>
        <div class="topbar-stat">🎖️ Divisões: <span class="stat-val">58</span></div>
        <div class="topbar-stat">🌐 Tensão: <span class="stat-val">0%</span></div>
    </div>

    <!-- VIEWPORT COM O EVENTO DO JOGO -->
    <div class="hoi4-viewport">
        {event_window_html}

        <!-- HUD DE TELEMETRIA VISUAL -->
        <div class="hud-panel">
            <div class="hud-header">
                <span>Raio-X de Evento HoI4</span>
                <span class="hud-badge">{event.event_type}</span>
            </div>
            <div class="hud-row">
                <span>ID do Evento:</span>
                <span class="hud-val">{event.id}</span>
            </div>
            <div class="hud-row">
                <span>Arquivo de Origem:</span>
                <span class="hud-val">{event.file_name}</span>
            </div>
            <div class="hud-row">
                <span>GFX da Imagem:</span>
                <span class="hud-val">{event.picture_gfx or 'N/A'}</span>
            </div>
            <div class="hud-row">
                <span>Resolução da Imagem:</span>
                <span class="hud-val">{event.picture_dims[0]}x{event.picture_dims[1]} px</span>
            </div>
            <div class="hud-row">
                <span>Comprimento do Texto:</span>
                <span class="hud-val">{event.desc_length} caracteres</span>
            </div>
            <div class="hud-row">
                <span>Quantidade de Opções:</span>
                <span class="hud-val">{event.options_count} escolhas</span>
            </div>
            {warnings_html}
        </div>
    </div>
</body>
</html>
"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)


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

        battalions = []
        reg_match = re.search(r'regiments\s*=\s*\{', block)
        if reg_match:
            r_block, _ = parse_bracket_content(block, reg_match.end() - 1)
            battalions = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{', r_block)

        supports = []
        sup_match = re.search(r'support\s*=\s*\{', block)
        if sup_match:
            s_block, _ = parse_bracket_content(block, sup_match.end() - 1)
            supports = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{', s_block)

        combat_width = len(battalions) * 2
        template = DivisionTemplate(
            name=template_name,
            battalions=battalions,
            supports=supports,
            combat_width=combat_width,
            total_manpower=len(battalions) * 1000 + len(supports) * 400
        )

        if combat_width < 12:
            template.is_balanced = False
            template.critique = f"Largura de combate muito baixa ({combat_width}W). Fragil para trincheiras."
        elif "artillery" not in supports and not any("artillery" in b for b in battalions):
            template.is_balanced = False
            template.critique = "Sem artilharia! Sofrera atrito macico contra infantaria entrincheirada."
        else:
            template.critique = "Template solido para combate de trincheiras (WW1)."

        report.templates.append(template)

    div_count = len(re.findall(r'\bdivision\s*=\s*\{', text))
    report.total_starting_divisions = div_count

    if history_file and history_file.exists():
        with open(history_file, "r", encoding="utf-8", errors="ignore") as f:
            h_text = f.read()
        
        inf_guns = re.findall(r'type\s*=\s*infantry_equipment_[0-9][^}]*amount\s*=\s*([0-9]+)', h_text)
        art_guns = re.findall(r'type\s*=\s*artillery_equipment_[0-9][^}]*amount\s*=\s*([0-9]+)', h_text)
        sup_guns = re.findall(r'type\s*=\s*support_equipment_[0-9][^}]*amount\s*=\s*([0-9]+)', h_text)

        report.infantry_equipment_stockpile = sum(int(x) for x in inf_guns)
        report.artillery_stockpile = sum(int(x) for x in art_guns)
        report.support_equipment_stockpile = sum(int(x) for x in sup_guns)

        if report.infantry_equipment_stockpile < 1000:
            report.is_stockpile_sufficient = False
            report.warnings.append(f"Estoque inicial de fuzis critico (+{report.infantry_equipment_stockpile}).")

    return report


# =============================================================================
# MULTIPLAYER SAFETY & PERFORMANCE RADAR
# =============================================================================

def audit_multiplayer_safety() -> List[str]:
    hazards = []
    if ON_ACTIONS_DIR.exists():
        for f in ON_ACTIONS_DIR.glob("*.txt"):
            with open(f, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
                if "on_daily" in content:
                    lines = content.splitlines()
                    for idx, line in enumerate(lines, 1):
                        if "every_country" in line or "every_state" in line:
                            hazards.append(f"[PERFORMANCE] Loop global em on_daily detectado em {f.name}:{idx}: '{line.strip()}'")
    return hazards


# =============================================================================
# COMPLETE TREE ANALYSIS AGGREGATOR
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
    missing_icons = 0

    p1_nodes, p2_nodes, p3_nodes = [], [], []
    wing_map = {
        'Político': [],
        'Econômico': [],
        'Exército': [],
        'Diplomacia': [],
        'Marinha': [],
        'Pós-Guerra': []
    }
    coords_seen: Dict[Tuple[int, int], str] = {}
    collision_count = 0
    signatures = []

    for f_id, node in nodes.items():
        analyze_focus(node)
        total_score += node.substance_score
        
        if node.phase == 1:
            p1_nodes.append(node)
        elif node.phase == 2:
            p2_nodes.append(node)
        else:
            p3_nodes.append(node)

        # Classify by wing
        if node.id.startswith('ENG_') or tag == 'ENG':
            if node.x <= 15:
                wing_map['Político'].append(node)
            elif 16 <= node.x <= 38:
                wing_map['Econômico'].append(node)
            elif 44 <= node.x <= 62:
                wing_map['Diplomacia'].append(node)
            elif 63 <= node.x <= 86:
                wing_map['Marinha'].append(node)
            elif 87 <= node.x <= 104:
                wing_map['Exército'].append(node)
            else:
                wing_map['Pós-Guerra'].append(node)
        elif node.id.startswith('ITA_') or tag == 'ITA':
            if node.x <= 16:
                wing_map['Político'].append(node)
            elif 17 <= node.x <= 38:
                wing_map['Econômico'].append(node)
            elif 39 <= node.x <= 56:
                wing_map['Diplomacia'].append(node)
            elif 57 <= node.x <= 77 or 88 <= node.x <= 94:
                wing_map['Exército'].append(node)
            elif 78 <= node.x <= 87:
                wing_map['Marinha'].append(node)
            else:
                wing_map['Pós-Guerra'].append(node)
        elif node.x <= 10:
            wing_map['Político'].append(node)
        elif 16 <= node.x <= 38:
            wing_map['Econômico'].append(node)
        elif 44 <= node.x <= 62:
            wing_map['Exército'].append(node)
        elif 68 <= node.x <= 86:
            wing_map['Diplomacia'].append(node)
        elif 92 <= node.x <= 102:
            wing_map['Marinha'].append(node)
        else:
            wing_map['Pós-Guerra'].append(node)

        # Asset metrics
        report.total_civ_factories += node.factories_civ
        report.total_mil_factories += node.factories_mil
        report.total_dockyards += node.dockyards
        report.total_slots += node.slots
        
        bunkers_in_node = len(re.findall(r'bunker\s*=\s*[1-9]', node.raw_reward)) + len(re.findall(r'type\s*=\s*(?:bunker|coastal_bunker)', node.raw_reward))
        report.total_bunkers += bunkers_in_node
        report.total_events_fired += len(node.fired_events)
        report.total_decisions_unlocked += len(node.unlocked_decisions)
        report.total_variable_mods += len(re.findall(r'add_to_variable\s*=', node.raw_reward))
        report.total_tech_bonuses += len(re.findall(r'add_tech_bonus\s*=', node.raw_reward))

        # Signature for variety detection
        cr = node.raw_reward
        sig = (
            bool(re.search(r'type\s*=\s*industrial_complex', cr)),
            bool(re.search(r'type\s*=\s*arms_factory', cr)),
            bool(re.search(r'type\s*=\s*dockyard', cr)),
            bool(re.search(r'type\s*=\s*(?:bunker|coastal_bunker)', cr)),
            bool(re.search(r'country_event', cr)),
            bool(re.search(r'add_tech_bonus', cr)),
            bool(re.search(r'add_to_variable', cr)),
            bool(re.search(r'set_country_flag', cr)),
            bool(re.search(r'(?:army|navy|air)_experience', cr)),
            bool(re.search(r'add_ideas', cr)),
            bool(re.search(r'remove_ideas', cr)),
            bool(re.search(r'add_political_power', cr)),
            bool(re.search(r'add_stability', cr)),
            bool(re.search(r'add_autonomy_ratio|build_railway', cr)),
            bool(re.search(r'(?:auh|ENG)_ww1_set_', cr))
        )
        signatures.append(sig)

        if node.is_filler or node.substance_score < 3.5:
            filler_nodes.append(node)

        if not node.is_icon_valid:
            missing_icons += 1

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
            has_relocated_cont = False
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as _f_cont:
                    _m_cont = re.search(r'continuous_focus_position\s*=\s*\{\s*x\s*=\s*(\d+)\s*y\s*=\s*(\d+)', _f_cont.read())
                    if _m_cont and int(_m_cont.group(2)) >= 2000:
                        has_relocated_cont = True
            except Exception:
                pass
            if not has_relocated_cont:
                report.continuous_focus_hazard = True

    report.nodes = nodes
    report.total_focuses = len(nodes)
    report.avg_substance_score = round(total_score / len(nodes), 2)
    report.filler_count = len(filler_nodes)
    report.filler_percentage = round((len(filler_nodes) / len(nodes)) * 100, 1)
    report.collision_count = collision_count
    report.missing_icons_count = missing_icons

    # 5 Gameplay Pillars Calculation
    wing_evals = {}
    for wname, flist in wing_map.items():
        if flist:
            w_score = round(sum(f.substance_score for f in flist) / len(flist), 1)
            w_civs = sum(f.factories_civ for f in flist)
            w_mils = sum(f.factories_mil for f in flist)
            w_docks = sum(f.dockyards for f in flist)
            w_bunkers = sum(len(re.findall(r'type\s*=\s*(?:bunker|coastal_bunker)', f.raw_reward)) for f in flist)
            w_events = sum(len(f.fired_events) for f in flist)
            w_vars = sum(len(re.findall(r'add_to_variable', f.raw_reward)) for f in flist)
            w_techs = sum(len(re.findall(r'add_tech_bonus', f.raw_reward)) for f in flist)
            wing_evals[wname] = {
                'count': len(flist),
                'score': w_score,
                'civs': w_civs,
                'mils': w_mils,
                'docks': w_docks,
                'bunkers': w_bunkers,
                'events': w_events,
                'vars': w_vars,
                'techs': w_techs
            }
    report.wing_metrics = wing_evals
    p1 = sum(w['score'] for w in wing_evals.values()) / max(len(wing_evals), 1)
    report.score_p1_specialization = round(p1, 1)

    # P2: Systemic Integration
    sys_density = (report.total_variable_mods + report.total_events_fired + report.total_decisions_unlocked) / max(len(nodes), 1)
    p2 = min(10.0, 5.0 + sys_density * 4.5)
    report.score_p2_mechanics = round(p2, 1)

    # P3: Balance & Anti-Powercreep
    p3 = 8.5
    if report.total_mil_factories < 10:
        p3 -= 2.0
    elif report.total_mil_factories > 60:
        p3 -= 3.0
    if report.total_civ_factories > 75:
        p3 -= 2.0
    report.score_p3_balance = round(max(1.0, p3), 1)

    # P4: Diversity & Anti-Repetition
    sig_counts = Counter(signatures)
    report.distinct_signatures = len(sig_counts)
    max_sig_count = sig_counts.most_common(1)[0][1] if sig_counts else 0
    report.max_signature_pct = round((max_sig_count / max(len(nodes), 1)) * 100, 1)
    
    p4 = 8.2
    if report.max_signature_pct > 30.0:
        p4 -= 3.5
        report.cookie_cutter_warning = f"[ALERTA CRÍTICO] Repetição excessiva: {report.max_signature_pct}% dos focos compartilham o mesmo molde exato."
    elif report.max_signature_pct > 18.0:
        p4 -= 1.5
        report.cookie_cutter_warning = f"[ALERTA] Repetição moderada: {report.max_signature_pct}% dos focos compartilham o mesmo molde."
    else:
        report.cookie_cutter_warning = f"[OK] Variedade Saudável: {report.distinct_signatures} perfis distintos (máxima concentração {report.max_signature_pct}%)."
    report.score_p4_diversity = round(max(1.0, p4), 1)

    # P5: Pacing & Readiness for 1914
    report.phase_1_count = len(p1_nodes)
    report.phase_2_count = len(p2_nodes)
    report.phase_3_count = len(p3_nodes)
    report.phase_1_score = round(sum(n.substance_score for n in p1_nodes) / max(len(p1_nodes), 1), 2)
    report.phase_2_score = round(sum(n.substance_score for n in p2_nodes) / max(len(p2_nodes), 1), 2)
    report.phase_3_score = round(sum(n.substance_score for n in p3_nodes) / max(len(p3_nodes), 1), 2)
    report.pacing_1914_readiness_pct = round(min(100.0, (report.phase_1_count / 60.0) * 100.0), 1)
    p5 = 7.0
    if report.phase_1_count >= 50:
        p5 += 1.0
    report.score_p5_pacing = round(p5, 1)

    # Overall Gameplay Health Index
    report.overall_gameplay_index = round(
        0.25 * report.score_p1_specialization +
        0.25 * report.score_p2_mechanics +
        0.20 * report.score_p3_balance +
        0.15 * report.score_p4_diversity +
        0.15 * report.score_p5_pacing,
        2
    )

    if report.overall_gameplay_index >= 8.5:
        report.gameplay_tier = "OBRA-PRIMA (Nível Tier 1)"
    elif report.overall_gameplay_index >= 7.0:
        report.gameplay_tier = "SÓLIDO (Nível de Grande Mod Histórico)"
    elif report.overall_gameplay_index >= 5.0:
        report.gameplay_tier = "MODERADO (Funcional, mas precisa de polimento)"
    else:
        report.gameplay_tier = "CRÍTICO/RASO (Árvore vazia ou artificial)"

    # Diagnostic Strengths & Weaknesses
    strengths = []
    weaknesses = []
    
    if report.total_variable_mods >= 50:
        strengths.append(f"Forte integração sistêmica: {report.total_variable_mods} interações com variáveis imperiais de consentimento e coesão.")
    if report.total_events_fired >= 20:
        strengths.append(f"Densidade narrativa alta: {report.total_events_fired} eventos históricos e bilaterais disparados pela árvore.")
    if report.distinct_signatures >= 40 and report.max_signature_pct <= 20.0:
        strengths.append(f"Excelente diversidade de design: {report.distinct_signatures} perfis distintos sem repetição mecânica excessiva.")

    # Check for specific gameplay flaws
    army_mils = wing_evals.get('Exército', {}).get('mils', 0)
    if army_mils < 8:
        weaknesses.append(f"Gargalo Tático: Apenas {army_mils} fábricas militares no ramo do Exército. Em uma guerra de 4 frentes, isso sufoca a reposição de fuzis e canhões!")
    
    hollow_events = sum(
        1 for f in nodes.values()
        if f.fired_events and not any(
            ev.get("options_count", 0) >= 2 or any(o.get("summary") and o.get("summary") != "Vazia" for o in ev.get("options", []))
            for ev in f.event_details
        ) and len(f.raw_reward.strip().split()) <= 8
    )
    if hollow_events >= 10:
        weaknesses.append(f"Monotonia Residual: {hollow_events} focos apenas disparam eventos ocos sem escolhas de gabinete ou impacto material.")

    report.strengths_list = strengths
    report.weaknesses_list = weaknesses

    # AI & Loc
    report.ai_coverage_pct = round((ai_count / len(nodes)) * 100, 1)
    report.loc_coverage_pct = round((loc_count / len(nodes)) * 100, 1)
    report.shallow_loc_count = shallow_loc_count

    # Hitlist
    filler_nodes.sort(key=lambda n: (n.substance_score, -n.cost_days))
    report.hitlist = filler_nodes[:20]

    # Attach combat & spirits reports
    report.combat = analyze_combat(tag)
    report.spirits = analyze_spirits(tag, nodes)

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
            "is_icon_valid": n.is_icon_valid,
            "ai_status": n.ai_status,
            "has_ai": n.has_ai_will_do,
            "civs": n.factories_civ,
            "mils": n.factories_mil,
            "docks": n.dockyards,
            "slots": n.slots,
            "events": n.fired_events,
            "event_details": n.event_details,
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

            if (n.event_details && n.event_details.length > 0) {{
                html += '<div style="color: #58a6ff; font-weight: 600; margin-top: 8px;">📜 Eventos & Escolhas de Governança:</div>';
                n.event_details.forEach(ev => {{
                    html += `
                        <div style="background: rgba(88, 166, 255, 0.08); border: 1px solid rgba(88, 166, 255, 0.25); border-left: 3px solid #58a6ff; border-radius: 4px; padding: 6px 8px; margin: 5px 0;">
                            <div style="font-weight: 600; font-size: 0.78rem; color: #fff;">${{ev.title}} <span style="color: #8b949e; font-size: 0.7rem;">(${{ev.id}})</span></div>
                            <div style="font-size: 0.72rem; color: #8b949e; margin-top: 3px; font-weight: 500;">Opções & Ramificações:</div>
                            <ul style="padding-left: 14px; margin: 3px 0; font-size: 0.72rem;">`;
                    ev.options.forEach(opt => {{
                        html += `<li><b>${{opt.text}}</b>: <span style="color: #7ee787;">${{opt.summary}}</span></li>`;
                    }});
                    html += `</ul></div>`;
                }});
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
        print(f"[ERRO] Arquivo de foco para '{tag}' nao encontrado em {FOCUS_DIR}")
        return

    report = analyze_tree(tag, file_path)
    
    print("\n" + "=" * 80)
    print(f"       HOI4 GAMEPLAY RADAR — RAIO-X COMPLETO DE JOGABILIDADE & DESIGN ({report.tag})")
    print("=" * 80)
    print(f" Arquivo                 : {report.file_path}")
    print(f" Total de Focos          : {report.total_focuses}")
    print(f" Indice Geral de Gameplay: {report.overall_gameplay_index} / 10.0 [{report.gameplay_tier}]")
    print(f" Score Medio de Focos    : {report.avg_substance_score} / 10.0 | Fillers: {report.filler_count} ({report.filler_percentage}%)")
    print("-" * 80)
    print(" [1] OS 5 PILARES DE GAMEPLAY & DESIGN:")
    print(f"     Pilar 1 - Identidade dos Ramos     : {report.score_p1_specialization:4.1f} / 10.0 [Divisao Funcional dos 6 Ramos]")
    print(f"     Pilar 2 - Integracao Mecanica      : {report.score_p2_mechanics:4.1f} / 10.0 [{report.total_variable_mods} Vars, {report.total_events_fired} Eventos, {report.total_decisions_unlocked} Decisoes]")
    print(f"     Pilar 3 - Equilibrio & Powercreep  : {report.score_p3_balance:4.1f} / 10.0 [{report.total_civ_factories} Civs, {report.total_mil_factories} Mils, {report.total_bunkers} Fortes]")
    print(f"     Pilar 4 - Diversidade & Repeticao  : {report.score_p4_diversity:4.1f} / 10.0 [{report.distinct_signatures} Perfis | Max {report.max_signature_pct}%]")
    print(f"     Pilar 5 - Ritmo & Prontidao 1914   : {report.score_p5_pacing:4.1f} / 10.0 [P1: {report.phase_1_count} focos | Prontidao 1914: {report.pacing_1914_readiness_pct}%]")
    print("-" * 80)
    print(" [2] RAIO-X DOS 6 RAMOS DA ARVORE (WING BREAKDOWN):")
    for wname, w in report.wing_metrics.items():
        print(f"     • {wname:<10} ({w['count']:2d} focos | Nota: {w['score']:3.1f}/10): {w['civs']:2d} Civs | {w['mils']:2d} Mils | {w['bunkers']:2d} Fortes | {w['events']:2d} Eventos | {w['vars']:2d} Vars | {w['techs']:2d} Techs")
    print("-" * 80)
    print(" [3] DIAGNOSTICO HONESTO DE JOGABILIDADE:")
    for s in report.strengths_list:
        print(f"     [+] PONTO FORTE : {s}")
    for w in report.weaknesses_list:
        print(f"     [!] GARGALO     : {w}")
    if report.cookie_cutter_warning:
        print(f"     [*] REPETICAO   : {report.cookie_cutter_warning}")
    print("-" * 80)
    print(" [4] GFX & SAUDE VISUAL:")
    print(f"     Icones Quebrados/Missing : {report.missing_icons_count} focos sem icone valido no disco")
    print(f"     Colisoes de Coordenadas  : {report.collision_count} conflitos")
    print(f"     Risco Foco Continuo      : {'[ALERTA] Risco de sobreposicao no topo esquerdo' if report.continuous_focus_hazard else '[OK] Limpo'}")
    print("-" * 80)
    print(" [5] ESPIRITOS NACIONAIS & EMPILHAMENTO (BUFF STACKING):")
    if report.spirits:
        print(f"     Espiritos Iniciais 1911  : {report.spirits.total_starting_count} ideias ({', '.join(report.spirits.starting_ideas[:4])}...)")
        print(f"     Risco de Overflow Topbar : {'[ALERTA] Mais de 6 ideias ativas simultaneas' if report.spirits.has_topbar_overflow_risk else '[OK] Equilibrado'}")
        print(f"     Ideias sem 'remove_ideas': {len(report.spirits.unpaired_ideas_added)} adicionadas sem substituir tier anterior")
    print("-" * 80)
    print(" [6] BALISTICA & EXERCITO INICIAL (COMBAT RADAR):")
    if report.combat:
        print(f"     Divisoes Iniciais OOB    : {report.combat.total_starting_divisions} divisoes")
        print(f"     Estoque Fuzis / Canhoes  : +{report.combat.infantry_equipment_stockpile} fuzis | +{report.combat.artillery_stockpile} pecas de artilharia")
        for t in report.combat.templates[:2]:
            print(f"     Template '{t.name}': {t.combat_width}W -> {t.critique}")
    print("=" * 80)

    html_out = OUTPUT_DIR / f"{tag}_focus_tree.html"
    generate_interactive_html(report, html_out)
    print(f"\n [+] Painel Visual 2D Interativo com Filtro de Fases Gerado em:\n     file:///{html_out.as_posix()}\n")


def run_audit_all() -> None:
    print("\n" + "=" * 98)
    print("       AUDITORIA GLOBAL MULTIDIMENSIONAL DE JOGABILIDADE (TODAS AS POTENCIAS)")
    print("=" * 98)
    print(f" {'TAG':<5} | {'Focos':<5} | {'Score':<6} | {'Fase 1':<8} | {'Fase 2':<8} | {'Fase 3':<8} | {'Fillers':<10} | {'GFX Err':<8} | {'Status':<12}")
    print("-" * 98)

    for tag, file_path in TAG_TO_FILE.items():
        if tag in ["AUH", "SOV"]:
            continue
        if not file_path.exists():
            continue
        report = analyze_tree(tag, file_path)
        status = "EXCELENTE" if report.avg_substance_score >= 6.0 and report.filler_percentage <= 15 else "PRECISA POLIR"
        if report.avg_substance_score < 4.0 or report.filler_percentage > 35:
            status = "CRITICO/RASO"
        print(f" {tag:<5} | {report.total_focuses:<5} | {report.avg_substance_score:<6} | {report.phase_1_score:<8} | {report.phase_2_score:<8} | {report.phase_3_score:<8} | {report.filler_percentage}%      | {report.missing_icons_count:<8} | {status:<12}")

    print("=" * 98 + "\n")


def run_event_preview(event_id: str) -> None:
    event = inspect_event(event_id)
    if not event:
        print(f"[ERRO] Evento '{event_id}' nao encontrado em nenhum arquivo de events/")
        return

    print("\n" + "=" * 80)
    print(f"       INSPECAO VISUAL & ESTRUTURAL DE EVENTO — {event.id}")
    print("=" * 80)
    print(f" Arquivo              : {event.file_name}")
    print(f" Titulo               : {event.title_pt}")
    print(f" Imagem GFX           : {event.picture_gfx} -> {'[OK]' if event.is_picture_valid else '[ERRO GFX]'}")
    print(f" Arquivo da Imagem    : {event.picture_file or 'Nao encontrado'}")
    print(f" Dimensoes da Imagem  : {event.picture_dims[0]}x{event.picture_dims[1]} px {'(Ideal 450x250)' if event.picture_dims == (450, 250) else ''}")
    print(f" Tamanho do Texto     : {event.desc_length} caracteres {'[ALERTA OVERFLOW]' if event.is_text_overflow_risk else '[OK]'}")
    print(f" Opcoes de Escolha    : {event.options_count} opcoes")
    for idx, opt in enumerate(event.options, 1):
        print(f"   Opcao {idx}: '{opt['text']}' ({opt['key']}) {'[VAZIA]' if opt['is_empty'] else ''}")
    
    if event.warnings:
        print("-" * 80)
        print(" [!] ALERTAS DE COMPOSICAO:")
        for w in event.warnings:
            print(f"     - {w}")

    out_file = OUTPUT_DIR / f"event_{event.id}.html"
    generate_event_preview_html(event, out_file)
    print(f"\n [+] Simulador Visual do Evento Renderizado em:\n     file:///{out_file.as_posix()}\n")


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
        print("  python scripts/mod_engine.py inspect <TAG>        -> Raio-X completo (focos, combate, GFX, ideias)")
        print("  python scripts/mod_engine.py event-preview <ID>   -> Inspeciona e renderiza visual do evento em HTML")
        print("  python scripts/mod_engine.py audit-all            -> Auditoria comparativa global de todas as potencias")
        print("  python scripts/mod_engine.py mp-safety            -> Auditoria anti-desync e anti-lag para multiplayer")
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd in ("event", "event-preview", "event_preview") and len(sys.argv) >= 3:
        run_event_preview(sys.argv[2])
    elif cmd == "inspect" and len(sys.argv) >= 3:
        run_inspect(sys.argv[2])
    elif cmd == "audit-all":
        run_audit_all()
    elif cmd == "mp-safety":
        run_mp_safety()
    else:
        run_inspect(sys.argv[1])

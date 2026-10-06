"""Shared utilities, data models, and constants for Italy (ITA) WW1 content.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "ITA_ww1_"

# 5 Internal gauges
GAUGES = [
    "ita_ww1_interventionism",
    "ita_ww1_social_tension",
    "ita_ww1_army_morale",
    "ita_ww1_southern_gap",
    "ita_ww1_irredentism"
]

def clean_desc(effect_desc, lang="en"):
    """Format description ensuring immediate effect explanation is present."""
    prefix = "Immediate effect: " if lang == "en" else "Efeito imediato: "
    return f"{prefix}{effect_desc}"

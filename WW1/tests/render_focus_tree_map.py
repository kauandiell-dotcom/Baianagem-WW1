#!/usr/bin/env python3
"""
HOI4 Focus Tree Visual Renderer (via Matplotlib)
Renders the exact in-game 5-Wing coordinate grid, connection arrows,
and focus boxes to a high-resolution PNG diagram.
"""

import re
import argparse
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

WING_COLORS = [
    ("#1f77b4", "Wing 1: Política e Ideologias (x: 1-24)"),
    ("#2ca02c", "Wing 2: Economia e Infraestrutura (x: 25-48)"),
    ("#9467bd", "Wing 3: Marinha e Aviação (x: 49-72)"),
    ("#d62728", "Wing 4: Exército e Doutrinas (x: 73-105)"),
    ("#ff7f0e", "Wing 5: Diplomacia e Tratados (x: 106-135)")
]

def get_wing_color(x):
    if x <= 24:
        return WING_COLORS[0][0]
    elif x <= 48:
        return WING_COLORS[1][0]
    elif x <= 72:
        return WING_COLORS[2][0]
    elif x <= 105:
        return WING_COLORS[3][0]
    else:
        return WING_COLORS[4][0]

def parse_tree(file_path):
    with open(file_path, "r", encoding="utf-8-sig", errors="replace") as f:
        content = f.read()

    foci = {}
    focus_pattern = re.compile(r'\bfocus\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}|.)*?\}[^{}]*)*)\}', re.DOTALL)

    for m in focus_pattern.finditer(content):
        block = m.group(1)
        id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block)
        if not id_m:
            continue
        fid = id_m.group(1)

        x_m = re.search(r'\bx\s*=\s*(-?\d+)', block)
        y_m = re.search(r'\by\s*=\s*(-?\d+)', block)
        if not (x_m and y_m):
            continue

        x = int(x_m.group(1))
        y = int(y_m.group(1))

        prereqs = []
        for p_match in re.finditer(r'prerequisite\s*=\s*\{([^}]+)\}', block):
            for p_id in re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', p_match.group(1)):
                prereqs.append(p_id)

        foci[fid] = {"id": fid, "x": x, "y": y, "prereqs": prereqs}

    return foci

def render_tree(foci, output_png, title="HOI4 National Focus Tree"):
    if not foci:
        print("No foci found to render.")
        return

    min_x = min(f["x"] for f in foci.values())
    max_x = max(f["x"] for f in foci.values())
    min_y = min(f["y"] for f in foci.values())
    max_y = max(f["y"] for f in foci.values())

    fig_w = max(16, (max_x - min_x + 6) * 0.4)
    fig_h = max(10, (max_y - min_y + 4) * 0.7)

    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=150)
    fig.patch.set_facecolor("#1a1a1a")
    ax.set_facecolor("#121212")

    # Draw arrows first
    for fid, f in foci.items():
        cx, cy = f["x"], -f["y"]
        for p in f["prereqs"]:
            if p in foci:
                px, py = foci[p]["x"], -foci[p]["y"]
                ax.annotate(
                    "",
                    xy=(cx, cy + 0.35),
                    xytext=(px, py - 0.35),
                    arrowprops=dict(
                        arrowstyle="-|>",
                        color="#666666",
                        lw=1.2,
                        mutation_scale=8,
                        shrinkA=2,
                        shrinkB=2,
                    ),
                )

    # Draw focus boxes
    box_w = 1.4
    box_h = 0.6
    for fid, f in foci.items():
        x, y = f["x"], -f["y"]
        color = get_wing_color(x)

        rect = patches.FancyBboxPatch(
            (x - box_w / 2, y - box_h / 2),
            box_w,
            box_h,
            boxstyle="round,pad=0.08,rounding_size=0.15",
            facecolor="#222222",
            edgecolor=color,
            linewidth=1.8,
            zorder=3,
        )
        ax.add_patch(rect)

        # Label (truncate if long)
        short_label = fid.replace("GER_", "").replace("_", "\n")
        if len(short_label.split("\n")) > 3:
            lines = short_label.split("\n")
            short_label = "\n".join(lines[:2]) + "..."

        ax.text(
            x,
            y,
            short_label,
            ha="center",
            va="center",
            fontsize=5.5,
            color="#ffffff",
            fontweight="bold",
            zorder=4,
        )

    # Decorate axes
    ax.set_xlim(min_x - 2, max_x + 2)
    ax.set_ylim(-max_y - 2, -min_y + 2)
    ax.set_xlabel("X (Columns / Wings)", color="#cccccc", fontsize=10)
    ax.set_ylabel("Y (Rows / Timeline Progression)", color="#cccccc", fontsize=10)
    ax.tick_params(colors="#888888")
    ax.grid(True, linestyle="--", alpha=0.15, color="#555555")

    # Title
    plt.title(f"{title} ({len(foci)} Focos)", color="#ffffff", fontsize=14, pad=15, fontweight="bold")

    # Legend
    legend_elements = [
        patches.Patch(facecolor=c, edgecolor="#ffffff", label=lbl)
        for c, lbl in WING_COLORS
    ]
    ax.legend(handles=legend_elements, loc="upper right", facecolor="#222222", edgecolor="#444444", labelcolor="#ffffff", fontsize=8)

    plt.tight_layout()
    output_path = Path(output_png)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"Rendered {len(foci)} foci diagram to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render HOI4 focus tree to PNG")
    parser.add_argument("--tree", required=True, help="Focus tree .txt")
    parser.add_argument("--out", default="focus_tree_map.png", help="Output PNG path")
    args = parser.parse_args()

    foci = parse_tree(args.tree)
    render_tree(foci, args.out, title=Path(args.tree).stem.upper())

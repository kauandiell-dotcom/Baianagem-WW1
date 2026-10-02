import re
import json
from pathlib import Path

tree_file = Path(r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\common\national_focus\germany.txt")
loc_file = Path(r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\localisation\braz_por\ww1_germany_focus_l_braz_por.yml")
output_html = Path(r"C:\Users\Usuário\.gemini\antigravity\brain\262c6aaa-3175-48e9-9057-aecbb94d8027\hoi4_interactive_tree.html")

loc_dict = {}
if loc_file.exists():
    with open(loc_file, "r", encoding="utf-8-sig", errors="replace") as f:
        for line in f:
            m = re.match(r'^\s*([a-zA-Z0-9_.]+):(?:\d+)?\s*"(.*)"\s*$', line)
            if m:
                loc_dict[m.group(1)] = m.group(2)

with open(tree_file, "r", encoding="utf-8-sig", errors="replace") as f:
    text = f.read()

pattern = re.compile(r'\bfocus\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}|.)*?\}[^{}]*)*)\}', re.DOTALL)
foci = []
for m in pattern.finditer(text):
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

    mut_ex = []
    for mex in re.finditer(r'mutually_exclusive\s*=\s*\{([^}]+)\}', block):
        for m_id in re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', mex.group(1)):
            mut_ex.append(m_id)

    cost_m = re.search(r'\bcost\s*=\s*(\d+)', block)
    cost = int(cost_m.group(1)) * 7 if cost_m else 70

    title = loc_dict.get(fid, fid)
    desc = loc_dict.get(fid + "_desc", "Sem descrição disponível.")

    # Clean styling codes §Y §! for HTML
    clean_title = re.sub(r'§[A-Z!]?', '', title)
    clean_desc = re.sub(r'§[A-Z!]?', '', desc)

    # Determine wing
    if x <= 24:
        wing = "Wing 1: Política & Ideologias"
        wing_color = "#3b82f6"
    elif x <= 48:
        wing = "Wing 2: Economia & Indústria"
        wing_color = "#10b981"
    elif x <= 72:
        wing = "Wing 3: Marinha & Aviação"
        wing_color = "#8b5cf6"
    elif x <= 105:
        wing = "Wing 4: Exército & Frentes"
        wing_color = "#ef4444"
    else:
        wing = "Wing 5: Diplomacia & Tratados"
        wing_color = "#f97316"

    foci.append({
        "id": fid,
        "title": clean_title,
        "desc": clean_desc,
        "x": x,
        "y": y,
        "days": cost,
        "wing": wing,
        "wingColor": wing_color,
        "prereqs": prereqs,
        "mut_ex": mut_ex
    })

foci_json = json.dumps(foci, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>HOI4 Mod Utilities - Interactive Focus Tree (Antigravity 2.0)</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    body {{
      margin: 0;
      padding: 0;
      overflow: hidden;
      user-select: none;
      background: #0f172a;
      color: #f8fafc;
      font-family: system-ui, -apple-system, sans-serif;
    }}
    .focus-card {{
      cursor: pointer;
      transition: transform 0.15s ease, stroke-width 0.15s ease;
    }}
    .focus-card:hover {{
      transform: scale(1.04);
      filter: brightness(1.2);
    }}
    .active-card {{
      stroke: #38bdf8 !important;
      stroke-width: 3px !important;
    }}
  </style>
</head>
<body class="flex flex-col h-screen">

  <!-- Top Toolbar -->
  <header class="flex items-center justify-between px-6 py-3 bg-slate-900 border-b border-slate-800 z-10">
    <div class="flex items-center gap-3">
      <div class="px-2.5 py-1 bg-sky-500/20 text-sky-400 font-bold rounded text-xs tracking-wider uppercase border border-sky-500/30">
        Antigravity 2.0 Native
      </div>
      <h1 class="text-base font-bold text-white tracking-wide">HOI4 Focus Tree Visual Explorer &bull; Alemanha WW1</h1>
      <span class="text-xs text-slate-400 bg-slate-800 px-2 py-0.5 rounded-full">{len(foci)} Focos</span>
    </div>

    <!-- Search & Controls -->
    <div class="flex items-center gap-4">
      <input type="text" id="searchInput" placeholder="Pesquisar foco..." class="bg-slate-800 border border-slate-700 text-xs px-3 py-1.5 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:border-sky-500 w-56" />
      <div class="flex items-center gap-1 bg-slate-800 p-1 rounded-lg border border-slate-700">
        <button id="btnZoomIn" class="px-2.5 py-1 text-xs hover:bg-slate-700 rounded font-bold" title="Zoom In">+</button>
        <button id="btnZoomOut" class="px-2.5 py-1 text-xs hover:bg-slate-700 rounded font-bold" title="Zoom Out">-</button>
        <button id="btnReset" class="px-2.5 py-1 text-xs hover:bg-slate-700 rounded" title="Ajustar Visualização">Ajustar</button>
      </div>
    </div>
  </header>

  <!-- Main Explorer Canvas + Sidebar -->
  <div class="flex flex-1 relative overflow-hidden">
    
    <!-- SVG Viewport -->
    <div id="viewport" class="flex-1 cursor-grab active:cursor-grabbing relative overflow-hidden bg-slate-950">
      <svg id="svgCanvas" class="w-full h-full">
        <defs>
          <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b" />
          </marker>
        </defs>
        <g id="scene"></g>
      </svg>
    </div>

    <!-- Sidebar Detail Panel -->
    <aside id="sidebar" class="w-96 bg-slate-900 border-l border-slate-800 flex flex-col p-5 overflow-y-auto shadow-2xl z-10 hidden">
      <div class="flex items-start justify-between mb-3">
        <span id="detailWing" class="text-xs font-bold uppercase tracking-wider px-2 py-0.5 rounded border"></span>
        <button id="btnCloseDetail" class="text-slate-400 hover:text-white text-sm font-bold">&times;</button>
      </div>
      <h2 id="detailTitle" class="text-lg font-bold text-white leading-tight mb-2"></h2>
      <div class="text-xs text-sky-400 font-mono mb-4" id="detailId"></div>
      
      <div class="flex items-center gap-2 mb-4 text-xs">
        <span class="bg-slate-800 px-2.5 py-1 rounded border border-slate-700 text-slate-300 font-semibold" id="detailDays"></span>
        <span class="bg-slate-800 px-2.5 py-1 rounded border border-slate-700 text-slate-300 font-semibold" id="detailCoords"></span>
      </div>

      <div class="mb-4">
        <h3 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1">Descrição Histórica</h3>
        <p id="detailDesc" class="text-xs text-slate-300 leading-relaxed bg-slate-800/60 p-3 rounded-lg border border-slate-700/50"></p>
      </div>

      <div id="prereqsBox" class="mb-4 hidden">
        <h3 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1">Pré-Requisitos</h3>
        <div id="detailPrereqs" class="flex flex-col gap-1 text-xs"></div>
      </div>

      <div id="mutExBox" class="hidden">
        <h3 class="text-xs font-bold text-rose-400 uppercase tracking-wider mb-1">Mutuamente Exclusivo Com</h3>
        <div id="detailMutEx" class="flex flex-col gap-1 text-xs text-rose-300"></div>
      </div>
    </aside>

  </div>

  <script>
    const fociData = {foci_json};
    const scene = document.getElementById('scene');
    const viewport = document.getElementById('viewport');
    const searchInput = document.getElementById('searchInput');

    // Grid Scaling constants
    const SCALE_X = 140;
    const SCALE_Y = 110;
    const BOX_W = 120;
    const BOX_H = 65;

    let panX = 50;
    let panY = 80;
    let zoom = 0.55;
    let isDragging = false;
    let startX = 0;
    let startY = 0;

    function applyTransform() {{
      scene.setAttribute('transform', `translate(${{panX}}, ${{panY}}) scale(${{zoom}})`);
    }}

    // Render tree connections & nodes
    function render() {{
      scene.innerHTML = '';
      const fociMap = new Map();
      fociData.forEach(f => fociMap.set(f.id, f));

      // Draw Arrows
      fociData.forEach(f => {{
        const cx = f.x * SCALE_X;
        const cy = f.y * SCALE_Y;

        f.prereqs.forEach(pid => {{
          const p = fociMap.get(pid);
          if (p) {{
            const px = p.x * SCALE_X;
            const py = p.y * SCALE_Y;

            const line = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            const d = `M ${{px}} ${{py + BOX_H/2}} C ${{px}} ${{py + BOX_H/2 + 30}}, ${{cx}} ${{cy - BOX_H/2 - 30}}, ${{cx}} ${{cy - BOX_H/2}}`;
            line.setAttribute('d', d);
            line.setAttribute('fill', 'none');
            line.setAttribute('stroke', '#475569');
            line.setAttribute('stroke-width', '2');
            line.setAttribute('marker-end', 'url(#arrow)');
            scene.appendChild(line);
          }}
        }});
      }});

      // Draw Foci Boxes
      fociData.forEach(f => {{
        const cx = f.x * SCALE_X;
        const cy = f.y * SCALE_Y;

        const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        g.setAttribute('class', 'focus-card');
        g.setAttribute('data-id', f.id);
        g.onclick = () => selectFocus(f);

        // Rect
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', cx - BOX_W/2);
        rect.setAttribute('y', cy - BOX_H/2);
        rect.setAttribute('width', BOX_W);
        rect.setAttribute('height', BOX_H);
        rect.setAttribute('rx', '8');
        rect.setAttribute('fill', '#1e293b');
        rect.setAttribute('stroke', f.wingColor);
        rect.setAttribute('stroke-width', '2');
        g.appendChild(rect);

        // Title text
        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', cx);
        text.setAttribute('y', cy - 8);
        text.setAttribute('text-anchor', 'middle');
        text.setAttribute('fill', '#f8fafc');
        text.setAttribute('font-size', '10');
        text.setAttribute('font-weight', 'bold');
        text.setAttribute('pointer-events', 'none');

        // Split title into short lines
        const words = f.title.split(' ');
        let l1 = words.slice(0, 3).join(' ');
        let l2 = words.slice(3, 6).join(' ');
        if (words.length > 6) l2 += '...';

        const tspan1 = document.createElementNS('http://www.w3.org/2000/svg', 'tspan');
        tspan1.setAttribute('x', cx);
        tspan1.setAttribute('dy', '0');
        tspan1.textContent = l1;
        text.appendChild(tspan1);

        if (l2) {{
          const tspan2 = document.createElementNS('http://www.w3.org/2000/svg', 'tspan');
          tspan2.setAttribute('x', cx);
          tspan2.setAttribute('dy', '14');
          tspan2.textContent = l2;
          text.appendChild(tspan2);
        }}
        g.appendChild(text);

        // Cost badge
        const badge = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        badge.setAttribute('x', cx);
        badge.setAttribute('y', cy + BOX_H/2 - 8);
        badge.setAttribute('text-anchor', 'middle');
        badge.setAttribute('fill', '#94a3b8');
        badge.setAttribute('font-size', '8');
        badge.textContent = `${{f.days}} dias`;
        g.appendChild(badge);

        scene.appendChild(g);
      }});

      applyTransform();
    }}

    function selectFocus(f) {{
      const sidebar = document.getElementById('sidebar');
      sidebar.classList.remove('hidden');

      const wingBadge = document.getElementById('detailWing');
      wingBadge.textContent = f.wing;
      wingBadge.style.color = f.wingColor;
      wingBadge.style.borderColor = f.wingColor + '40';
      wingBadge.style.backgroundColor = f.wingColor + '15';

      document.getElementById('detailTitle').textContent = f.title;
      document.getElementById('detailId').textContent = f.id;
      document.getElementById('detailDays').textContent = `Duração: ${{f.days}} dias`;
      document.getElementById('detailCoords').textContent = `Posição: (x: ${{f.x}}, y: ${{f.y}})`;
      document.getElementById('detailDesc').textContent = f.desc;

      // Prerequisites
      const prereqsBox = document.getElementById('prereqsBox');
      const prereqsList = document.getElementById('detailPrereqs');
      prereqsList.innerHTML = '';
      if (f.prereqs && f.prereqs.length > 0) {{
        prereqsBox.classList.remove('hidden');
        f.prereqs.forEach(p => {{
          const div = document.createElement('div');
          div.className = 'bg-slate-800 p-1.5 rounded border border-slate-700 text-slate-300';
          div.textContent = p;
          prereqsList.appendChild(div);
        }});
      }} else {{
        prereqsBox.classList.add('hidden');
      }}

      // Mutually Exclusive
      const mutExBox = document.getElementById('mutExBox');
      const mutExList = document.getElementById('detailMutEx');
      mutExList.innerHTML = '';
      if (f.mut_ex && f.mut_ex.length > 0) {{
        mutExBox.classList.remove('hidden');
        f.mut_ex.forEach(m => {{
          const div = document.createElement('div');
          div.className = 'bg-rose-950/40 p-1.5 rounded border border-rose-800/40';
          div.textContent = m;
          mutExList.appendChild(div);
        }});
      }} else {{
        mutExBox.classList.add('hidden');
      }}
    }}

    document.getElementById('btnCloseDetail').onclick = () => {{
      document.getElementById('sidebar').classList.add('hidden');
    }};

    // Pan & Zoom controls
    viewport.onmousedown = (e) => {{
      if (e.target.closest('.focus-card')) return;
      isDragging = true;
      startX = e.clientX - panX;
      startY = e.clientY - panY;
    }};

    window.onmousemove = (e) => {{
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      applyTransform();
    }};

    window.onmouseup = () => isDragging = false;

    viewport.onwheel = (e) => {{
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.15 : 0.85;
      zoom = Math.max(0.15, Math.min(2.5, zoom * zoomFactor));
      applyTransform();
    }};

    document.getElementById('btnZoomIn').onclick = () => {{
      zoom = Math.min(2.5, zoom * 1.25);
      applyTransform();
    }};

    document.getElementById('btnZoomOut').onclick = () => {{
      zoom = Math.max(0.15, zoom * 0.8);
      applyTransform();
    }};

    document.getElementById('btnReset').onclick = () => {{
      panX = 50;
      panY = 80;
      zoom = 0.55;
      applyTransform();
    }};

    // Search filter
    searchInput.oninput = (e) => {{
      const q = e.target.value.toLowerCase().trim();
      document.querySelectorAll('.focus-card').forEach(card => {{
        const fid = card.getAttribute('data-id');
        const f = fociData.find(item => item.id === fid);
        if (!q || f.title.toLowerCase().includes(q) || f.id.toLowerCase().includes(q)) {{
          card.style.opacity = '1';
        }} else {{
          card.style.opacity = '0.15';
        }}
      }});
    }};

    render();
  </script>
</body>
</html>
"""

output_html.parent.mkdir(parents=True, exist_ok=True)
with open(output_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated interactive focus tree explorer at: {output_html}")

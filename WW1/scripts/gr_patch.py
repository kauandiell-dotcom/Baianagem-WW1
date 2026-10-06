"""Remendos cirurgicos nas arvores de foco da Alemanha e da Russia (portas de data, IA, exclusoes, bypass)."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import relayout_tabbed_tree as rt


def _lines(block):
    return block.splitlines(keepends=True)


def _depth1_stmt(lines, key):
    """(i, j) do primeiro statement de profundidade 1 que comeca por `key =`; j inclusivo."""
    depth = 0
    for i, line in enumerate(lines):
        clean = rt._strip(line)
        if depth == 1 and re.match(r"\s*" + re.escape(key) + r"\s*=", clean):
            bal = clean.count("{") - clean.count("}")
            j = i
            while bal > 0:
                j += 1
                c = rt._strip(lines[j])
                bal += c.count("{") - c.count("}")
            return i, j
        depth += clean.count("{") - clean.count("}")
    return None


def _y_index(lines):
    depth = 0
    for i, line in enumerate(lines):
        clean = rt._strip(line)
        if depth == 1 and re.match(r"\s*y\s*=", clean):
            return i
        depth += clean.count("{") - clean.count("}")
    raise ValueError("sem y")


def _insert_after_y(lines, text, nl):
    k = _y_index(lines)
    ind = re.match(r"\s*", lines[k]).group(0)
    lines[k + 1:k + 1] = [ind + t + nl for t in text]


def add_available(lines, cond, nl):
    st = _depth1_stmt(lines, "available")
    if st:
        i, _ = st
        lines[i] = re.sub(r"(available\s*=\s*\{)", lambda m: m.group(1) + " " + cond + " ", lines[i], count=1)
    else:
        _insert_after_y(lines, ["available = { " + cond + " }"], nl)


def add_bypass(lines, cond, nl):
    if _depth1_stmt(lines, "bypass"):
        st = _depth1_stmt(lines, "bypass")
        lines[st[0]] = re.sub(r"(bypass\s*=\s*\{)", lambda m: m.group(1) + " OR = { " + cond + " } ", lines[st[0]], count=1) \
            if False else lines[st[0]]
        return
    _insert_after_y(lines, ["bypass = { " + cond + " }"], nl)


def add_mex(lines, ids, nl):
    st = _depth1_stmt(lines, "mutually_exclusive")
    toks = " ".join("focus = " + i for i in ids)
    if st:
        i, _ = st
        lines[i] = re.sub(r"(mutually_exclusive\s*=\s*\{)", lambda m: m.group(1) + " " + toks + " ", lines[i], count=1)
    else:
        _insert_after_y(lines, ["mutually_exclusive = { " + toks + " }"], nl)


def set_ai(lines, ai_text, nl):
    st = _depth1_stmt(lines, "ai_will_do")
    if st:
        del lines[st[0]:st[1] + 1]
    _insert_after_y(lines, [ai_text], nl)


def add_reward(lines, effect, nl):
    st = _depth1_stmt(lines, "completion_reward")
    if not st:
        raise ValueError("sem completion_reward")
    i, _ = st
    lines[i] = re.sub(r"(completion_reward\s*=\s*\{)", lambda m: m.group(1) + " " + effect + " ", lines[i], count=1)


def patch_tree(path, ops):
    """ops: {focus_id: [(fn_name, arg), ...]} ; fn_name in available|bypass|mex|ai|reward."""
    raw = Path(path).read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    nl = "\r\n" if "\r\n" in text else "\n"
    nodes, spans = rt.parse(text)
    ids = {n["id"] for n in nodes}
    missing = [i for i in ops if i not in ids]
    if missing:
        raise SystemExit("focos inexistentes: %s" % missing)
    out, last = [], 0
    for n, (s, e) in zip(nodes, spans):
        out.append(text[last:s])
        block = text[s:e]
        if n["id"] in ops:
            lines = _lines(block)
            for fn, arg in ops[n["id"]]:
                {"available": add_available, "bypass": add_bypass, "mex": add_mex, "ai": set_ai, "reward": add_reward}[fn](lines, arg, nl)
            block = "".join(lines)
        out.append(block)
        last = e
    out.append(text[last:])
    Path(path).write_bytes((b"\xef\xbb\xbf" if bom else b"") + "".join(out).encode("utf-8"))
    return len(ops)


def all_ids(path):
    text = Path(path).read_bytes().decode("utf-8-sig")
    nodes, _ = rt.parse(text)
    return [n["id"] for n in nodes], {n["id"]: n for n in nodes}, text

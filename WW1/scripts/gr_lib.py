"""Helpers do gerador de conteudo da Alemanha e da Russia (eventos, decisoes, ideias, textos EN/PT-BR)."""
import re

LOC = {'english': {}, 'braz_por': {}}


def loc(key, en, pt):
    assert key not in LOC['english'], 'chave de texto duplicada: ' + key
    for lang, txt in (('english', en), ('braz_por', pt)):
        assert '"' not in txt and '\n' not in txt, (key, txt)
        LOC[lang][key] = txt


def V(var, n):
    return 'add_to_variable = { %s = %s }' % (var, n)


def ind(text, n):
    pad = '\t' * n
    return '\n'.join(pad + l if l.strip() else l for l in text.strip('\n').split('\n'))


def fx(*lines):
    return '\n'.join(l for l in lines if l)


# ------------------------------------------------------------------ eventos
EVENTS = []


def event(eid, pic, t, d, options, immediate=None, trigger=None, hidden=False, once=True):
    """t, d: (en, pt). options: lista de (en, pt, efeitos, ai_chance|None, trigger|None)."""
    assert len(options) >= 1
    loc(eid + '.t', *t)
    loc(eid + '.d', *d)
    out = ['country_event = {', '\tid = %s' % eid, '\ttitle = %s.t' % eid, '\tdesc = %s.d' % eid,
           '\tpicture = GFX_event_WW1_%s' % pic, '', '\tis_triggered_only = yes']
    if once:
        out.append('\tfire_only_once = yes')
    if trigger:
        out += ['', '\ttrigger = {', ind(trigger, 2), '\t}']
    if immediate:
        out += ['', '\timmediate = {', ind(immediate, 2), '\t}']
    for k, (en, pt, eff, ai, otrig) in enumerate(options):
        key = '%s.%s' % (eid, 'abcdef'[k])
        loc(key, en, pt)
        out += ['', '\toption = {', '\t\tname = %s' % key]
        if otrig:
            out += ['\t\ttrigger = {', ind(otrig, 3), '\t\t}']
        if ai is not None:
            out += ['\t\tai_chance = { factor = %d }' % ai]
        if eff:
            out += [ind(eff, 2)]
        out += ['\t}']
    out += ['}', '']
    EVENTS.append('\n'.join(out))


# ------------------------------------------------------------------ ideias
IDEAS = {}


def idea(name, picture, mods, en, pt, den, dpt):
    assert name not in IDEAS
    IDEAS[name] = (picture, mods)
    loc(name, en, pt)
    loc(name + '_desc', den, dpt)


def render_ideas():
    out = ['ideas = {', '\tcountry = {', '']
    for name, (pic, mods) in IDEAS.items():
        out += ['\t\t%s = {' % name, '\t\t\tpicture = %s' % pic, '\t\t\tallowed = { always = no }',
                '\t\t\tremoval_cost = -1', '\t\t\tmodifier = {']
        out += ['\t\t\t\t%s = %s' % (k, v) for k, v in mods.items()]
        out += ['\t\t\t}', '\t\t}', '']
    out += ['\t}', '}', '']
    return '\n'.join(out)


# ------------------------------------------------------------------ decisoes
DECISIONS = {}   # categoria -> [blocos]
CATEGORIES = []


def category(cid, icon, allowed, visible, en, pt, den, dpt):
    loc(cid, en, pt)
    loc(cid + '_desc', den, dpt)
    CATEGORIES.append('%s = {\n\ticon = %s\n\tallowed = { %s }\n\tvisible = { %s }\n\tvisible_when_empty = no\n}\n'
                      % (cid, icon, allowed.replace('\n', ' '), visible.replace('\n', ' ')))
    DECISIONS[cid] = []


def decision(cat, did, icon, cost, re_enable, available, visible, effect, ai, en, pt, den, dpt):
    loc(did, en, pt)
    loc(did + '_desc', den, dpt)
    b = ['\t%s = {' % did, '\t\ticon = %s' % icon, '\t\tcost = %d' % cost, '\t\tdays_re_enable = %d' % re_enable,
         '\t\tavailable = {', ind(available, 3), '\t\t}', '\t\tvisible = {', ind(visible, 3), '\t\t}',
         '\t\tcomplete_effect = {', ind(effect, 3), '\t\t}', '\t\tai_will_do = { base = 0', ind(ai, 3), '\t\t}', '\t}', '']
    DECISIONS[cat].append('\n'.join(b))


def render_decisions():
    out = []
    for cat, blocks in DECISIONS.items():
        out += ['%s = {' % cat, ''] + blocks + ['}', '']
    return '\n'.join(out)


def write_loc(root):
    d_en = root / 'localisation' / 'english'
    d_pt = root / 'localisation' / 'braz_por'
    for d, lang, head in ((d_en, 'english', 'l_english:'), (d_pt, 'braz_por', 'l_braz_por:')):
        d.mkdir(parents=True, exist_ok=True)
        lines = [head] + [' %s:0 "%s"' % (k, v) for k, v in LOC[lang].items()]
        (d / ('ww1_ger_rus_rework_%s.yml' % head[:-1])).write_bytes(('\ufeff' + '\n'.join(lines) + '\n').encode('utf-8'))

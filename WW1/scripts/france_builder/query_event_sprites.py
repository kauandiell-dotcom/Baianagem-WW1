import re

with open('interface/ww1_france_eventpictures.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

sprites = re.findall(r'name = "([^"]+)"', text)
queries = ['agadir', 'verdun', 'marne', 'poincare', 'clemenceau', 'russia', 'british', 'italy', 'serbia', 'pershing', 'tank', 'plane', 'parliament', 'conference', 'treaty', 'surrender', 'french', 'german', 'soldier']

for q in queries:
    m = [s for s in sprites if q in s.lower()]
    print(f"{q}: {m[:4]}")

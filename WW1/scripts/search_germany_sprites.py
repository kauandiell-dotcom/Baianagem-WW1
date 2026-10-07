import re

with open('scripts/all_normal_germany_sprites.txt', 'r', encoding='utf-8') as f:
    sprites = [l.strip() for l in f if l.strip()]

cats = {
    'spartakus': ['spart', 'rot', 'red', 'streik', 'strike', 'rat', 'counc', 'arbeit', 'volk', 'prolet', 'liebknecht', 'luxemburg', 'kpd'],
    'spd_republic': ['spd', 'scheidemann', 'ebert', 'weimar', 'republ', 'demokrat', 'reichstag', 'sozial', 'pazif', 'peace', 'reform', 'verfass'],
    'ohl_military': ['ohl', 'hindenburg', 'ludendorff', 'generalstab', 'milit', 'diktat', 'krupp', 'ruhr', 'heer', 'artill', 'kanon', 'krieg'],
    'vaterland': ['vaterland', 'tirpitz', 'kapp', 'siegfrieden', 'annex', 'balt', 'landeswehr', 'pan_', 'alld', 'chauvin', 'flotte'],
    'kaiser_trunk': ['kaiser', 'wilhelm', 'reichstag', 'preuss', 'hohenzollern', 'junker', 'kanzler', 'bethmann']
}

for cat_name, keywords in cats.items():
    matches = [s for s in sprites if any(k in s.lower() for k in keywords)]
    print(f'=== Category {cat_name}: {len(matches)} sprites ===')
    for m in matches[:15]:
        print('  ', m)

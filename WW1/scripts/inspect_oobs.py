import glob, re, os

majors = ['GER', 'SOV', 'FRA', 'ENG', 'AUS', 'ITA', 'USA', 'TUR', 'SER', 'BUL', 'BEL', 'ROM']
for tag in majors:
    f = f'history/units/{tag}_1936_generic.txt'
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        divs = len(re.findall(r'\bdivision\s*=', content))
        templates = re.findall(r'division_template\s*=\s*\{\s*name\s*=\s*"([^"]+)"', content)
        stockpiles = re.findall(r'add_equipment_to_stockpile\s*=\s*\{\s*type\s*=\s*([^\s]+)\s+amount\s*=\s*([0-9]+)', content)
        print(f"{tag:4} | Divs: {divs:3} | Templates: {len(templates):2} ({templates})")
        print(f"     Stockpiles in OOB: {stockpiles}")
        
    c_f = glob.glob(f'history/countries/{tag}*')
    if c_f:
        with open(c_f[0], 'r', encoding='utf-8', errors='ignore') as fp:
            c_content = fp.read()
        c_stockpiles = re.findall(r'add_equipment_to_stockpile\s*=\s*\{\s*type\s*=\s*([^\s]+)\s+amount\s*=\s*([0-9]+)', c_content)
        if c_stockpiles:
            print(f"     Stockpiles in Country: {c_stockpiles}")

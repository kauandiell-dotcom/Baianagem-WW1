from pathlib import Path

path = Path(r"C:\Users\Usuário\Pictures\Baianagem-WW1\WW1\localisation\english\generic_focuses_names_l_english.yml")
content = path.read_text(encoding="utf-8-sig")

replacements = {
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(path, "wb") as f:
    f.write(b'\xef\xbb\xbf')
    f.write(content.encode("utf-8"))

print("Successfully cleaned curly quotes and saved with UTF-8 BOM.")

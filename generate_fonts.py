import os

# Define your font folder and output CSS file
FONT_DIR = "fonts"
OUTPUT_CSS = "fonts.css"

# Map of font file extensions to CSS format values
FONT_FORMATS = {
    ".woff2": "woff2",
    ".woff": "woff",
    ".ttf": "truetype",
    ".otf": "opentype"
}

# Guess style from filename
def guess_style(name):
    return "italic" if "italic" in name.lower() else "normal"

# Guess weight from filename
def guess_weight(name):
    name = name.lower()
    if "thin" in name: return 100
    if "extralight" in name: return 200
    if "light" in name: return 300
    if "regular" in name or "normal" in name: return 400
    if "medium" in name: return 500
    if "semibold" in name or "demibold" in name: return 600
    if "bold" in name: return 700
    if "extrabold" in name or "heavy" in name: return 800
    if "black" in name: return 900
    return 400

def generate_font_face(file):
    name, ext = os.path.splitext(file)
    format = FONT_FORMATS.get(ext.lower())
    if not format:
        return ""

    font_family = name.split("-")[0]
    weight = guess_weight(name)
    style = guess_style(name)

    return f"""
@font-face {{
  font-family: '{font_family}';
  src: url('{FONT_DIR}/{file}') format('{format}');
  font-weight: {weight};
  font-style: {style};
}}
""".strip()

# Main script
def main():
    files = os.listdir(FONT_DIR)
    css_blocks = []

    for file in files:
        if os.path.splitext(file)[1].lower() in FONT_FORMATS:
            block = generate_font_face(file)
            if block:
                css_blocks.append(block)

    output = "\n\n".join(css_blocks)
    with open(OUTPUT_CSS, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ {OUTPUT_CSS} generated with {len(css_blocks)} fonts.")

if __name__ == "__main__":
    main()

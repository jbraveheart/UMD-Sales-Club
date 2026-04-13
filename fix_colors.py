import re
import os

files = ["index.html", "about.html", "leaders.html", "sponsors.html"]

config_block = """<script id="tailwind-config">
    tailwind.config = {
        darkMode: "class",
        theme: {
            extend: {
                "colors": {
                    "surface": "#FAF5E9",
                    "background": "#FAF5E9",
                    "on-surface": "#3D0B15",
                    "on-surface-variant": "#821E32",
                    "surface-dim": "#F0E5D1",
                    "surface-container": "#F0E5D1",
                    "surface-container-lowest": "#FFFDF8",
                    "surface-container-highest": "#EAD8BD",
                    "surface-container-low": "#F5ECD8",
                    "primary": "#821E32",
                    "on-primary": "#F0BE3C",
                    "primary-container": "#4D111D",
                    "on-primary-container": "#F0BE3C",
                    "secondary": "#F0BE3C",
                    "on-secondary": "#3D0B15",
                    "secondary-container": "#FBEACA",
                    "on-secondary-container": "#821E32",
                    "outline": "#C9B69B",
                    "outline-variant": "#E0CEB6"
                },
                "fontFamily": {
                    "headline": ["Work Sans", "Montserrat", "sans-serif"],
                    "body": ["Inter", "sans-serif"],
                    "label": ["Inter", "sans-serif"]
                }
            }
        }
    }
</script>"""

# Regex to find existing tailwind-config scripts.
config_regex = re.compile(r'<script id="tailwind-config">.*?</script>', re.DOTALL)
tailwind_src_regex = re.compile(r'<script src="https://cdn\.tailwindcss\.com.*?"></script>')

replacements_html = {
    'bg-[#050505]/95': 'bg-surface-container-highest/95',
    'bg-[#050505]': 'bg-surface-container',
    'bg-[#121212]': 'bg-surface',
    'bg-[#0A0A0A]': 'bg-surface-container-low',
    'bg-black': 'bg-primary-container',
    'bg-white/5': 'bg-secondary/10',
    'bg-white/10': 'bg-secondary/20',
    'border-white/5': 'border-outline-variant',
    'border-white/10': 'border-outline',
    'text-white/70': 'text-on-primary/70',
    'text-white/60': 'text-on-primary/60',
    'text-white': 'text-on-primary', # If on primary container, else needs care, but general is better than white
    'text-gray-400': 'text-on-surface-variant',
    'text-gray-300': 'text-on-surface-variant'
}

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Apply configuration injection
    if '<script id="tailwind-config">' in content:
        content = config_regex.sub(config_block, content)
    else:
        # Insert after the tailwind script
        match = tailwind_src_regex.search(content)
        if match:
            content = content[:match.end()] + "\n" + config_block + content[match.end():]

    # Force body to have bg-surface text-on-surface
    content = content.replace('<body class="bg-white text-slate-900 font-[\'Inter\']">', '<body class="bg-surface text-on-surface font-body">')
    content = content.replace('<body class="bg-[#050505] text-white font-[\'Inter\']">', '<body class="bg-surface text-on-surface font-body">')

    # General replacements for hardcoded black/white remaining in about.html or others
    for old, new in replacements_html.items():
        content = content.replace(old, new)
        
    # Extra fix for about.html specific stuff
    content = content.replace('bg-white', 'bg-surface')
    content = content.replace('text-slate-900', 'text-primary')
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Universally applied UMD Logo Maroon/Gold palette everywhere.")

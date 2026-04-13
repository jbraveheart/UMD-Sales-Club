import re

html_files = ["index.html", "leaders.html", "sponsors.html"]

dark_colors = """            "colors": {
                    "surface": "#121212",
                    "on-surface-variant": "#B3B3B3",
                    "background": "#050505",
                    "on-surface": "#FFFFFF",
                    "surface-dim": "#1C1C1C",
                    "surface-container": "#1F1F1F",
                    "primary-container": "#51000D",
                    "on-primary": "#FFFFFF",
                    "surface-container-lowest": "#000000",
                    "surface-container-highest": "#333333",
                    "surface-container-low": "#0F0F0F",
                    "outline": "#4D4D4D",
                    "primary": "#C8102E", 
                    "outline-variant": "#262626",
                    "secondary": "#FFD200",
                    "on-secondary": "#111111",
                    "secondary-fixed": "#FFE16B",
                    "secondary-fixed-dim": "#E5B800",
                    "secondary-container": "#332200",
                    "on-secondary-container": "#FFF0B3",
                    "surface-variant": "#262626",
                    "inverse-surface": "#F0F0F0",
                    "inverse-on-surface": "#121212"
            },"""

for filepath in html_files:
    with open(filepath, "r") as f:
        content = f.read()

    # using regex to replace the colors dict
    match = re.search(r'"colors"\s*:\s*\{[^{}]+\}', content)
    if match:
        content = content[:match.start()] + dark_colors + content[match.end():]
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated {filepath} colors to dark mode.")

# Now for about.html, we replace utility classes.
about_path = "about.html"
with open(about_path, "r") as f:
    about = f.read()

# Replace classes
replacements = {
    'bg-white text-slate-900': 'bg-[#050505] text-white',
    'bg-white/80': 'bg-black/80',
    'border-slate-100': 'border-white/10',
    'text-slate-900': 'text-white',
    'text-slate-800': 'text-white',
    'text-slate-500': 'text-gray-400',
    'text-slate-400': 'text-gray-400',
    'text-slate-600': 'text-gray-300',
    'bg-white/95': 'bg-[#050505]/95',
    'bg-slate-50': 'bg-[#0A0A0A]',
    'bg-white': 'bg-[#121212]',
    'bg-slate-950': 'bg-black',
    'bg-slate-900': 'bg-[#050505]',
    'border-slate-800': 'border-white/10',
    'text-slate-300': 'text-gray-300'
}

for old, new in replacements.items():
    about = about.replace(old, new)

with open(about_path, "w") as f:
    f.write(about)
print("Updated about.html classes to dark mode.")


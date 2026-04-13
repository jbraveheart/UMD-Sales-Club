import os
import re

html_files = ["index.html", "about.html", "leaders.html", "sponsors.html"]

new_colors = """            "colors": {
                    "surface": "#FCFAF8",
                    "on-surface-variant": "#5C4D4D",
                    "background": "#FCFAF8",
                    "on-surface": "#2A2121",
                    "surface-dim": "#EBE3E0",
                    "surface-container": "#F4EBE8",
                    "primary-container": "#8C001C",
                    "on-primary": "#FFFFFF",
                    "surface-container-lowest": "#FFFFFF",
                    "surface-container-highest": "#E3D5D2",
                    "surface-container-low": "#F9F3F1",
                    "outline": "#C2B2B2",
                    "primary": "#51000D",
                    "outline-variant": "#E8DBDB",
                    "secondary": "#C69214",
                    "on-secondary": "#FFFFFF",
                    "secondary-fixed": "#FFE18F",
                    "secondary-fixed-dim": "#E5B02E",
                    "secondary-container": "#FBE6AB",
                    "on-secondary-container": "#4A3500",
                    "surface-variant": "#E3D5D2",
                    "on-secondary-fixed": "#2B1E00",
                    "on-secondary-fixed-variant": "#4E3700",
                    "inverse-surface": "#3D3131",
                    "inverse-on-surface": "#FCFAF8"
            },"""

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist")
        return
    
    with open(filepath, "r") as f:
        content = f.read()

    match = re.search(r'"colors"\s*:\s*\{[^{}]+\}', content)
    if match:
        content = content[:match.start()] + new_colors + content[match.end():]
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Could not find colors block in {filepath}")

for f in html_files:
    update_file(f)

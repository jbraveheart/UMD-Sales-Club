import os

def update_file(filename, replacements):
    if not os.path.exists(filename):
        return
    with open(filename, 'r') as f:
        content = f.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open(filename, 'w') as f:
        f.write(content)

# leaders.html
update_file("leaders.html", {
    'class="w-full h-full object-cover"': 'class="w-full h-full object-cover transition-transform duration-500 hover:scale-110 hover:brightness-110 cursor-pointer"'
})

# sponsors.html
update_file("sponsors.html", {
    'class="max-h-16 w-auto"': 'class="max-h-16 w-auto transition-transform duration-500 group-hover:scale-110"'
})

# index.html
update_file("index.html", {
    'class="w-full h-auto max-w-xl object-contain drop-shadow-2xl"': 'class="w-full h-auto max-w-xl object-contain drop-shadow-2xl hover:scale-105 hover:drop-shadow-[0_20px_50px_rgba(240,190,60,0.5)] transition-all duration-500"'
})

# about.html
update_file("about.html", {
    'class="w-16 h-16 rounded-full object-cover"': 'class="w-16 h-16 rounded-full object-cover transition-transform duration-300 group-hover:scale-110"',
    'class="w-16 h-16 rounded-full object-cover filter grayscale group-hover:grayscale-0 transition"': 'class="w-16 h-16 rounded-full object-cover filter grayscale group-hover:grayscale-0 group-hover:scale-110 transition-all duration-300"'
})

print("Images made interactive!")

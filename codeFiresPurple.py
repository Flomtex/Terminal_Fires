import os, random, time

w, h = 40, 20
fire = [0] * (w * h)

# ASCII chars from low to high heat
chars = " .:-=+*#%@"

# Matching ANSI 256-color codes (purple/magenta tones)
colors = [
    16,   # black
    53,   # deep plum
    54,   # dark purple
    55,   # purple
    90,   # violet
    129,  # magenta-ish
    135,  # brighter magenta
    141,  # soft pink-purple
    183,  # pastel violet
    219   # lavender white
]

# Padding spaces for center alignment
pad = " " * 6  # adjust for your terminal width

def clear(): print("\033[H", end="")

def draw():
    for y in range(h):
        print(pad, end="")  # Add horizontal padding
        for x in range(w):
            heat = fire[y * w + x]
            c = chars[min(len(chars)-1, heat)]
            color = colors[min(len(colors)-1, heat)]
            print(f"\033[38;5;{color}m{c}\033[0m", end="")
        print()

def update():
    for x in range(w):
        fire[(h-1)*w + x] = random.randint(0, len(chars)-1)
    for y in range(h-1):
        for x in range(w):
            below = fire[(y+1)*w + x]
            decay = random.randint(0, 2)
            fire[y*w + x] = max(0, below - decay)

os.system("cls" if os.name == "nt" else "clear")
print("\033[?25l")  # hide cursor

try:
    while True:
        update()
        clear()
        draw()
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\033[?25h")  # show cursor

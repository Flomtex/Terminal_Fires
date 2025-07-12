import os, random, time

w, h = 40, 20
fire = [0] * (w * h)

# ASCII chars from low to high heat
chars = " .:-=+*#%@"

# Matching ANSI 256-color codes (blue tones)
colors = [
    16,   # black
    17,   # dark blue
    18,   # navy
    19,   # blue
    20,   # brighter blue
    25,   # indigo
    27,   # teal
    33,   # cyan
    45,   # sky blue
    81    # icy blue
]

# Padding spaces for center alignment
pad = " " * 6  # adjust this number to center

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

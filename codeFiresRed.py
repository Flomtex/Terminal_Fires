import os, random, time

w, h = 40, 20
fire = [0] * (w * h)

# ASCII chars from low to high heat
chars = " .:-=+*#%@"

# Matching ANSI 256-color codes (red/yellow/orange)
colors = [
    16,   # black
    52,   # dark red
    88,   # red
    124,  # brighter red
    160,  # orange-red
    166,  # orange
    202,  # yellow-orange
    208,  # gold
    220,  # yellow
    226,  # light yellow
]

# Padding spaces to center the fire horizontally
pad = " " * 6  # adjust this to match your terminal width

def clear(): print("\033[H", end="")

def draw():
    for y in range(h):
        print(pad, end="")  # add horizontal padding to each line
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

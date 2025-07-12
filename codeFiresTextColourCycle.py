import os, random, time

w, h = 40, 20
fire = [0] * (w * h)

chars = " .:-=+*#%@"

# Define multiple palettes: red, green, blue, purple, cyan, yellow
palettes = [
    [16, 52, 88, 124, 160, 166, 202, 208, 220, 226],  # 🔴 red/yellow
    [16, 22, 28, 34, 40, 46, 82, 118, 154, 190],      # 🟢 green
    [16, 17, 18, 19, 20, 25, 27, 33, 45, 81],         # 🔵 blue
    [16, 53, 54, 55, 90, 129, 135, 141, 183, 219],    # 🟣 purple
    [16, 30, 31, 32, 37, 38, 44, 51, 87, 123],        # 🔵 cyan-teal
    [16, 100, 142, 178, 184, 185, 186, 220, 226, 227] # 🟡 yellow-gold
]

message = "FLOMTEX BUILDS"  # Edit this to your own text!
msg_row = h - 2
msg_start = (w - len(message)) // 2
pad = " " * 11

def clear(): print("\033[H", end="")

def draw(colors):
    for y in range(h):
        print(pad, end="")
        for x in range(w):
            idx = y * w + x
            heat = fire[idx]
            c = chars[min(len(chars)-1, heat)]
            color = colors[min(len(colors)-1, heat)]

            # Burn message
            if y == msg_row and msg_start <= x < msg_start + len(message):
                c = message[x - msg_start]

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
    for i, char in enumerate(message):
        idx = msg_row * w + msg_start + i
        fire[idx] = len(chars)-1 if char != ' ' else 0

os.system("cls" if os.name == "nt" else "clear")
print("\033[?25l")  # hide cursor

# Animation loop
try:
    palette_index = 0
    last_switch = time.time()

    while True:
        update()
        clear()
        draw(palettes[palette_index])
        time.sleep(0.05)

        # Switch palette every 2 seconds
        if time.time() - last_switch >= 2:
            palette_index = (palette_index + 1) % len(palettes)
            last_switch = time.time()

except KeyboardInterrupt:
    print("\033[?25h")  # show cursor

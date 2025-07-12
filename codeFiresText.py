import os, random, time

w, h = 40, 20
fire = [0] * (w * h)

chars = " .:-=+*#%@"
colors = [16, 52, 88, 124, 160, 166, 202, 208, 220, 226]

message = "FLOMTEX BUILDS"  # Edit this to your own text!
msg_row = h - 2
msg_start = (w - len(message)) // 2

# Padding to center the whole fire horizontally
pad = " " * 11  # Adjust t his to match your terminal width

def clear(): print("\033[H", end="")

def draw():
    for y in range(h):
        print(pad, end="")  # Add horizontal padding before each row
        for x in range(w):
            idx = y * w + x
            heat = fire[idx]
            c = chars[min(len(chars)-1, heat)]
            color = colors[min(len(colors)-1, heat)]

            # Overwrite message line with actual text
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

    # Keep heat high where text appears
    for i, char in enumerate(message):
        idx = msg_row * w + msg_start + i
        fire[idx] = len(chars)-1 if char != ' ' else 0

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

import os, random, time

w, h = 40, 20
fire = [0] * (w * h)
chars = " .:-=+*#%@"

# Number of spaces to center the fire horizontally
pad = " " * 6  # adjust this as needed

def clear(): print("\033[H", end="")

def draw():
    for y in range(h):
        print(pad, end="")  # add padding at the start of each row
        for x in range(w):
            heat = fire[y * w + x]
            c = chars[min(len(chars)-1, heat)]
            print(c, end="")
        print()

def update():
    for x in range(w):
        fire[(h-1)*w + x] = random.randint(0, 9)
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

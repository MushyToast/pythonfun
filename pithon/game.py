import random
import sys
from getkey import getkey, keys
def display(maze, secondary, walls, x, y, face):
    for _ in range(1,50): 
        print()
    sys.stdout.write("Coords: " + str(x) + " " + str(y) + "\n")
    for i in range(3,-4, -1):
        y_ = y + i
        for j in range(-3,4):
            x_ = x + j
            coord = str(x_) + " " + str(y_)
            if coord in maze:
                if x == x_ and y == y_:
                    sys.stdout.write(face + " ")
                else:
                    sys.stdout.write(maze[coord])
            else:
                wall = random.choice(walls)
                if random.randint(1,12) == 1:
                    wall = "🟨"
                if coord in secondary:
                    if secondary[coord] == "🪜 ":
                        wall = "🪜 "
                else:
                    if random.randint(1,50) == 1:
                        wall = "🪜 "
                maze[coord] = wall
                sys.stdout.write(maze[coord])
        print()
    sys.stdout.write("🪙: " + str(coin))
    print()
    for _ in range(1,3):
        if _ == 1:
            if maze[str(x) + " " + str(y)] == "🪜 ":
                print("Press Space To Climb Ladder")
            else:
                print("Floor: " + str(floor))
        else:
            print()
    return maze
maze = {}
maze_ = {}
face = "⬆️"
walls = ["⬜","⬛"]
coin = 0
for i in range(-1,2):
    for j in range(-1,2):
        maze[str(i) + " " + str(j)] = random.choice(walls)
maze["0 0"] = "⬜"

floor = 1
x = 0
y = 0

display(maze, maze_, walls, x, y, face)
while True:
    while True:
        key = getkey()

        if key.lower() == "x":
            exit()
        if key.lower() == "f":
            if face == "⬆️":
                if maze[str(x) + " " + str(y+1)] == "⬛":
                    maze[str(x) + " " + str(y+1)] = "⬜"
            elif face == "⬇️":
                if maze[str(x) + " " + str(y-1)] == "⬛":
                    maze[str(x) + " " + str(y-1)] = "⬜"
            elif face == "➡️":
                if maze[str(x+1) + " " + str(y)] == "⬛":
                    maze[str(x+1) + " " + str(y)] = "⬜"
            elif face == "⬅️":
                if maze[str(x-1) + " " + str(y)] == "⬛":
                    maze[str(x-1) + " " + str(y)] = "⬜"
            break
        if key == keys.SPACE:
            if maze[str(x) + " " + str(y)] == "🪜 ":
                if floor == 1:
                    floor = 2
                else:
                    floor = 1
                newmaze = maze_
                maze_ = maze
                maze = newmaze
                maze[str(x) + " " + str(y)] = "🪜 "
                display(maze, maze_, walls, x, y, face)
                break
        if key.lower() == "w" or key == "a" or key == "s" or key == "d":
            x_ = 0
            y_ = 0
            if key == "w":
                face = "⬆️"
                if maze[str(x) + " " + str(y+1)] != "⬛":
                    y += 1
            elif key == "s":
                face = "⬇️"
                if maze[str(x) + " " + str(y-1)] != "⬛":
                    y -= 1
            elif key == "d":
                face = "➡️"
                if maze[str(x+1) + " " + str(y)] != "⬛":
                    x += 1
            elif key == "a":
                face = "⬅️"
                if maze[str(x-1) + " " + str(y)] != "⬛":
                    x -= 1
            if maze[str(x) + " " + str(y)] == "🟨":
                coin += 1
                maze[str(x) + " " + str(y)] = "⬜"
            break
    print("\n")
    maze = display(maze, maze_, walls, x, y, face)

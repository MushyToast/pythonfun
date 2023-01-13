#IMPORTS
from pyfiglet import figlet_format
from getkey import getkey, keys
import random
import sys
from time import sleep
import colorama
from colorama import Fore

#PYFIGLET AND INFO

print(figlet_format("Soccer", font="big"))
print("A and D to aim your shot. Space to shoot. Watch for that goalie")
#FUNCTIONS
def deline(amount):
    for x in range(0, amount):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
def printarrow(offset):
    for x in range(0, offset):
        sys.stdout.write(" ")
    print("^")
    for x in range(0, offset):
        sys.stdout.write(" ")
    print("|")
    for x in range(0, offset):
        sys.stdout.write(" ")
    print("|")
    for x in range(0, offset):
        sys.stdout.write(" ")
    print("|")
    for x in range(0, offset):
        sys.stdout.write(" ")
    print("⚽")
def wait(time):
    sleep(time)
def printgoal():
    print("_______________")
    print("|-------------|")
    print("|-------------|")
    print("|-------------|")
    print("|-------------|")

def printgoalie(offset2):
    for x in range(0, offset2):
        sys.stdout.write(" ")
    print("🧍")

def offset(ofset):
    for x in range(0, ofset):
        sys.stdout.write(" ")
#VARIABLES
score = 0
oppscore = 0
v1 = False
pos = 0
v2 = 0
v3 = 0
speeds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.01, 0.05, 0.001]
print("Game starting momentarily..")
wait(2)
deline(99)
#ACTUAL CODE
while True:
    suddenfail = False
    fail = False
    suddenfailint = 0
    plrpos = 0
    print("Current score:", score, "Opponent score:", oppscore)
    printgoal()
    printgoalie(0)
    printarrow(0)
    while True: #while true loop to inf play until user stops
        goaliepos = 0
        v2 = random.randint(0, 1)
        key = getkey()
        if (key == "d" and pos + 1 != 14):
            if v1 == True:
                deline(99)
                v1 = False
            else:
                deline(99)
            print("Current score:", score, "Opponent score:", oppscore)
            printgoal()
            pos = pos + 1
            if v2 == 1:
                goaliepos = pos
                printgoalie(goaliepos)
            else:
                goaliepos = random.randint(0, 13)
                printgoalie(random.randint(0, 13))
            printarrow(pos)
        elif (key == "a" and pos - 1 != -1):
            if v1 == True:
                deline(99)
                v1 = False
            else:
                deline(99)
            print("Current score:", score, "Opponent score:", oppscore)
            printgoal()
            pos = pos - 1
            if v2 == 1:
                goaliepos = pos
                printgoalie(goaliepos)
            else:
                goaliepos = random.randint(0, 13)
                printgoalie(random.randint(0, 13))
            printarrow(pos)
        elif key == "a" or key == "d":
            print("You can't go any further!")
            deline(99)
            if pos == 0:
                pos = pos + 1
            else:
                pos = pos - 1
            v1 = True
        if key == " ":
            break
    if pos == goaliepos:
        fail = True
    else:
        fail = False
    suddenfailint = random.randint(1, 4)
    if suddenfailint == 2 or pos + 2 == goaliepos or pos - 2 == goaliepos:
        fail = True
        suddenfail = True
    if fail == False:
        for x in range(0, 5):
            deline(2)
            offset(pos)
            print("⚽")
            wait(random.choice(speeds))
    elif fail == True:
        if suddenfail == True:
            deline(99)
            print('Current score:', score, 'Opponent score:', oppscore)
            printgoal()
            printgoalie(pos)
            printarrow(pos)
            for x in range(0, 4):
                deline(2)
                offset(pos)
                print("⚽")
                wait(random.choice(speeds))
        else:
            for x in range(0, 4):
                deline(2)
                offset(pos)
                print("⚽")
                wait(random.choice(speeds))

    if fail == True:
        print(Fore.RED + f"Awh man, the goalie caught your ball. Sucks for you!" + Fore.RESET)
        wait(1.5)
        deline(99)
    elif fail == False:
        score = score + 1
        print(Fore.GREEN + f"Congrats, you scored against the goalie! Your score is now", str(score) + Fore.RESET)
        wait(1.5)
        deline(99)
    else:
        print(Fore.RED + f"An unkown error occured. lmao" + Fore.RESET)
        wait(1.5)
        deline(99)
    print("Current score:", score, "Opponent score:", oppscore)
    printgoal()
    printgoalie(0)
    printarrow(0)
    while True: #plr goalie mode
        shotpos = random.randint(1, 14)
        v3 = random.randint(0, 5)
        key = getkey()
        if (key == "a" and plrpos - 1 != -1):
            deline(99)
            plrpos = plrpos - 1
            print("Current score:", score, "Opponent score:", oppscore)
            printgoal()
            printgoalie(plrpos)
            if v3 == 1:
                shotpos = plrpos
                printarrow(shotpos)
                print(shotpos)
            else:
                printarrow(shotpos)
                print(shotpos)
            print(plrpos, shotpos, "Pos 1: Plr, Pos 2: Shot")
        elif key == "a":
            print("You can't go any further!")
        if (key == "d" and plrpos + 1 != 14):
            deline(99)
            plrpos = plrpos + 1
            print("Current score:", score, "Opponent score:", oppscore)
            printgoal()
            printgoalie(plrpos)
            if v3 == 1:
                shotpos = plrpos
                printarrow(shotpos)
                print(shotpos)
            else:
                printarrow(shotpos)
                print(shotpos)
            print(plrpos, shotpos, "Pos 1: Plr, Pos 2: Shot")
        elif key == "d":
            print("You can't go any further!")
        if key == " ":
            fail = False
            win = False
            if v3 == 1:
                shotpos = plrpos
            if (plrpos == shotpos):
                win = True
                print("EEEEE")
            if win == True:
                print('pass')
            else:
                print('fail')

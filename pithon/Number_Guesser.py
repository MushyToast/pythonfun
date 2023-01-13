import random
from getkey import getkey, keys
import sys
maxnumber = 999

def deleteline(lines):
    for x in range(1, lines):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

while True:
    rnumber = random.randint(1,maxnumber)
    guess = 0
    tries = 0
    
    while True:
        guess = int(input("Guess a number between 1 and %s: " % maxnumber))
        tries += 1
        if guess == rnumber:
            print("You guessed it in %s tries!" % tries)
            print("Play again? (y/n)")
            key = getkey()
            if key == "y" or key == "Y":
                break
            else:
                exit()
        elif guess > rnumber:
            print("Too high!")
        else:
            print("Too low!")
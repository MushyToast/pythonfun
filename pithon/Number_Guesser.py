import random
import time
from getkey import getkey, keys

maxnumber = 999


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
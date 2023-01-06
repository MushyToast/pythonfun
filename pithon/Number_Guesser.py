import random
import time

rnumber = random.randint(1,999)
gn = 0
v2 = True

while v2 == True:
    def ask():
        global gn
        v1 = input("Enter Number Guess > ")
        gn = int(v1)


    ask()
    print(gn)

    def compare():
        if gn > rnumber:
            print("Number too high")
        elif gn < rnumber:
                print("Number too low")
        elif gn == rnumber:
            print("You got it!")
            print("Program stopping in 3 seconds")
            time.sleep(3)
            quit()
    compare()


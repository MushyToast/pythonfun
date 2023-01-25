#IMPORTS
import time
import random
from getkey import getkey, keys
import pyquery
import os
import sys
import pyfiglet
#FUNCTIONS
def clearscreen():
    os.system('clear')

def scrollText(text, delay=0.1):
    for i in text:
        print(i, end='')
        sys.stdout.flush()
        time.sleep(delay)

def wait(secs):
    time.sleep(secs)

def specialcombine(val, combiner, min, max):
    if val + combiner > max:
        return max
    elif val + combiner < min:
        return min
    else:
        return val + combiner

#PYFIGLET
scrollText(pyfiglet.figlet_format("The", font="big"), 0.001)
scrollText(pyfiglet.figlet_format("Matrix", font="big"), 0.001)

#VARIABLES
balance = 500
day = -1
job = "Unemployed"
residence = "Apartment"
itemsinfridge = 0
happiness = 50
daycompleted = False
experience = 0
jobinfo = {
    "Unemployed": {"WeeklyPay": 0, "WeeklyHours": 0, "XPRequired": 0},
    "McDonalds": {"WeeklyPay": 620, "WeeklyHours": 40, "XPRequired": 0},
    "Walmart": {"WeeklyPay": 800, "WeeklyHours": 40, "XPRequired": 25},
    "Amazon": {"WeeklyPay": 900, "WeeklyHours": 40, "XPRequired": 35},
    "Google": {"WeeklyPay": 1000, "WeeklyHours": 50, "XPRequired": 60},
    "Microsoft": {"WeeklyPay": 1200, "WeeklyHours": 50, "XPRequired": 100},
    "Apple": {"WeeklyPay": 1250, "WeeklyHours": 50, "XPRequired": 120},
    "IT Tech": {"WeeklyPay": 1300, "WeeklyHours": 55, "XPRequired": 150},
    "Dunder Mifflin": {"WeeklyPay": 1500, "WeeklyHours": 60, "XPRequired": 69},
    "Teacher": {"WeeklyPay": 900, "WeeklyHours": 60, "XPRequired": 60},

}



weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#ACTUAL CODE

scrollText("This is the Matrix. A never ending cycle. Go to work. Get paid. Go to work. Get paid. \n", 0.01)
scrollText("You are fresh out of college. You have no job. You have no money. You are single. \n", 0.01)
print("Game starting momentarily...")
while True:
    clearscreen()
    if daycompleted == True:
        balance += 100
        day += 1
        daycompleted = False
    if daycompleted == False:
        if day == -1:
            day = 0
    if day == 7:
        day = 0
    if day == 5 or day == 6:
        scrollText("It's the weekend! You have no work. \n", 0.01)
    if day == 4:
        scrollText("It's Friday! Today is payday!. \n", 0.01)
        balance += jobinfo[job]["WeeklyPay"]
    weekday = weekdays[day]
    print(weekday)
    print("------------------")
    print(f"Job Experience: {experience}")
    print("Balance: $" + str(balance))
    print("Job: " + job)
    print("Happiness: " + str(happiness))
    print("[1] Work Options")
    print("[2] Go to the store")
    print("[3] Go to the gym")
    print("[4] Go to the park")
    key = getkey()
    if key == "1":
        clearscreen()
        print("Work Options:")
        print("[1] Go to work")
        print("[2] Change job")
        print("[3] Take the day off")
        print("[4] Go back")
        key = getkey()
        if key == "1":
            if job == "Unemployed":
                scrollText("You have no job. You can't go to work. \n", 0.01)
                wait(2)
                clearscreen()
            elif day == 5 or day == 6:
                    scrollText("It's the weekend. You have no work. \n", 0.01)
            else:
                experience +=  random.randint(1, 10)
                scrollText("You went to work. \n", 0.01)
                wait(1)
                scrollText("Still at work... \n", 0.01)
                wait(1)
                scrollText("It is now your lunch break \n")
                print("What will you eat? ")
                print("[1] Sandwich")
                print("[2] Salad")
                print("[3] Burger")
                print("[4] Pizza")
                key = getkey()
                if key == "1":
                    scrollText("You ate a sandwich. \n")
                    wait(2)
                    clearscreen()
                if key == "2":
                    scrollText("You ate a salad. \n")
                    wait(2)
                    clearscreen()
                if key == "3":
                    scrollText("You ate a burger. \n")
                    wait(2)
                    clearscreen()
                if key == "4":
                    scrollText("You ate a pizza. \n")
                    scrollText("The pizza was delicious. +5 happiness\n")
                    happiness = specialcombine(happiness, 5, 0, 100)
                    wait(2)
                    clearscreen()
                scrollText("You went back to work. \n")
                wait(1)
                fireddeterminer = None
                if random.randint(1, 5) == 3:
                    scrollText("You see your boss at work. What do you do? \n")
                    print("[1] Talk to your boss")
                    print("[2] Do nothing")
                    print("[3] Request a raise")
                    key = getkey()
                    if key == "1":
                        scrollText("You talked to your boss. +5 XP \n")
                        experience += 5
                        wait(0.5)
                        clearscreen()
                    if key == "3":
                        scrollText("You requested a raise. \n")
                        determiner = random.randint(1, 20)
                        fireddeterminer = random.randint(1, 100)
                        if determiner == 13:
                            scrollText("Your boss said yes! +10 XP \n")
                            experience += 10
                            jobinfo[job]["WeeklyPay"] += random.randint(50, 100)
                            wait(2)
                            clearscreen()
                        else:
                            if fireddeterminer == 69:
                                scrollText("Your boss said no. I guess he was in a bad mood because he fired you. -15 happiness \n")
                                job = "Unemployed"
                                happiness = specialcombine(happiness, -15, 0, 100)
                                wait(2)
                                clearscreen()
                                daycompleted = True
                            else:
                                scrollText("Your boss said no. -1 XP, -5 happiness \n")
                                experience -= 1
                                happiness = specialcombine(happiness, -5, 0, 100)
                                wait(2)
                                clearscreen()
                if fireddeterminer != 69:
                    scrollText("You went back to work. \n")
                    wait(1)
                    scrollText("You went home. \n")
                    wait(1)
                    scrollText("You are now home. \n")
                    wait(1)
                    clearscreen()
                    scrollText("It's time for dinner. Will you cook or order? \n")
                    print("[1] Cook")
                    print("[2] Order")
                    key = getkey()
                    if key == "1":
                        if itemsinfridge == 0:
                            scrollText("You have no food. You can't cook. And all the stores are closed.\n")
                            wait(2)
                            clearscreen()
                        else:
                            scrollText("You cooked dinner. \n")
                            wait(2)
                            clearscreen()
                    if key == "2":
                        print("What will you order? ")
                        print("[1] Pizza")
                        print("[2] Burger")
                        print("[3] Wings")
                        print("[4] Sushi")
                        key = getkey()
                        if key == "1":
                            if balance >= 20:
                                balance -= 20
                                scrollText("You ordered pizza. \n")
                                wait(2)
                                clearscreen()
                            else:
                                scrollText(f"You don't have enough money. You need $20. You only have ${balance}\n")
                                wait(2)
                                clearscreen()
                        if key == "2":
                            if balance >= 10:
                                balance -= 10
                                scrollText("You ordered a burger. \n")
                                wait(2)
                                clearscreen()
                            else:
                                scrollText(f"You don't have enough money. You need $10. You only have ${balance}\n")
                                wait(2)
                                clearscreen()
                        if key == "3":
                            if balance >= 15:
                                balance -= 15
                                scrollText("You ordered wings. \n")
                                wait(2)
                                clearscreen()
                            else:
                                scrollText(f"You don't have enough money. You need $15. You only have ${balance}\n")
                                wait(2)
                                clearscreen()
                        if key == "4":
                            if balance >= 25:
                                balance -= 25
                                scrollText("You ordered sushi. \n")
                                wait(2)
                                clearscreen()
                            else:
                                scrollText(f"You don't have enough money. You need $25. You only have ${balance}\n")
                                wait(2)
                                clearscreen()
                    scrollText("It's quite late. What will you do now? \n")
                    print("[1] Watch TV")
                    print("[2] Scroll through social media")
                    print("[3] Go to sleep")
                    wenttosleep = False
                    key = getkey()
                    if key == "1":
                        scrollText("You watched TV. \n")
                        wait(2)
                        clearscreen()
                    if key == "2":
                        scrollText("You scrolled through social media. \n")
                        wait(2)
                        clearscreen()
                    if key == "3":
                        scrollText("You went to sleep. \n")
                        wait(2)
                        clearscreen()
                        wenttosleep = True
                        daycompleted = True
                    if wenttosleep == False:
                        scrollText("You are now extremely tired, and you went to sleep.")
                        daycompleted = True
                        wait(2)
                        clearscreen()


                key = None
        if key == "2":
            clearscreen()
            print("Change job:")
            print("[1] McDonalds")
            print("[2] Walmart")
            print("[3] Amazon")
            print("[4] Google")
            print("[5] Microsoft")
            print("[6] Apple")
            print("[7] IT Tech")
            print("[8] Dunder Mifflin")
            print("[9] Teacher")
            print("[q] Resign from job")
            print("[0] Go back")
            key = getkey()
            if key == "1":
                job = "McDonalds"
                scrollText("You are now a McDonalds employee. \n", 0.01)
                wait(2)
                clearscreen()
            if key == "2":
                if experience >= jobinfo["Walmart"]["XPRequired"]:
                    job = "Walmart"
                    scrollText("You are now a Walmart employee. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Walmart. \n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "3":
                if experience >= jobinfo["Amazon"]["XPRequired"]:
                    job = "Amazon"
                    scrollText("You are now an Amazon employee. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Amazon. \n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "4":
                if experience >= jobinfo["Google"]["XPRequired"]:
                    job = "Google"
                    scrollText("You are now a Google employee. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Google. \n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "5":
                if experience >= jobinfo["Microsoft"]["XPRequired"]:
                    job = "Microsoft"
                    scrollText("You are now a Microsoft employee. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Microsoft. \n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "6":
                if experience >= jobinfo["Apple"]["XPRequired"]:
                    job = "Apple"
                    scrollText("You are now an Apple employee. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Apple. \n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "7":
                if experience >= jobinfo["IT Tech"]["XPRequired"]:
                    job = "IT Tech"
                    scrollText("You are now an IT Tech. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to be an IT Tech. \n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "8":
                if experience >= jobinfo["Dunder Mifflin"]["XPRequired"]:
                    job = "Dunder Mifflin"
                    scrollText("You are now a Dunder Mifflin employee. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Dunder Mifflin. \n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "9":
                if experience >= jobinfo["Teacher"]["XPRequired"]:
                    job = "Teacher"
                    scrollText("You are now a teacher. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to be a teacher. \n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "q":
                job = "Unemployed"
                scrollText("You are now unemployed. \n", 0.01)
                wait(2)
                clearscreen()
            if key == "0":
                clearscreen()
    elif key == "2":
        clearscreen()
        scrollText("You are now at the store. What will you buy? \n")
        print("[1] Food")
        print("[2] Clothes")
        print("[3] Electronics")
        print("[4] Go back")
        key = getkey()
        if key == "1":
            clearscreen()
            print("Food:")
            print("[1] Bread - $1")
            print("[2] Milk - $2")
            print("[3] Eggs - $3")
            print("[4] Go back")
            key = getkey()
            if key == "1":
                if balance >= 1:
                    balance -= 1
                    scrollText("You bought bread. \n")
                    wait(2)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $1. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "2":
                if balance >= 2:
                    balance -= 2
                    scrollText("You bought milk. \n")
                    wait(2)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $2. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "3":
                if balance >= 3:
                    balance -= 3
                    scrollText("You bought eggs. \n")
                    wait(2)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $3. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "4":
                clearscreen()
        if key == "2":
            clearscreen()
            print("Clothes:")
            print("[1] T-Shirt - $5")
            print("[2] Pants - $10")
            print("[3] Shoes - $15")
            print("[4] Go back")
            key = getkey()
            if key == "1":
                if balance >= 5:
                    balance -= 5
                    scrollText("You bought a t-shirt. +5 Happiness\n")
                    happiness = specialcombine(happiness, 5, 0, 100)
                    wait(2)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $5. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "2":
                if balance >= 10:
                    balance -= 10
                    scrollText("You bought pants. +5 Happiness\n")
                    happiness = specialcombine(happiness, 5, 0, 100)
                    wait(2)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $10. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "3":
                if balance >= 15:
                    balance -= 15
                    scrollText("You bought shoes. +10 Happiness\n")
                    happiness = specialcombine(happiness, 10, 0, 100)
                    wait(2)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $15. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "4":
                clearscreen()
        if key == "3":
            clearscreen()
            print("Electronics:")
            print("[1] Phone - $50")
            print("[2] Laptop - $100")
            print("[3] Flipper Zero - $1000")
            print("[4] Go back")
            key = getkey()
            if key == "1":
                if balance >= 50:
                    balance -= 50
                    scrollText("You bought a phone. +5 Happiness\n")
                    happiness = specialcombine(happiness, 5, 0, 100)
                    wait(2)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $50. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "2":
                if balance >= 100:
                    balance -= 100
                    scrollText("You bought a laptop. +10 Happiness\n")
                    happiness = specialcombine(happiness, 10, 0, 100)
                    wait(2)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $100. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "3":
                if balance >= 1000:
                    balance -= 1000
                    scrollText("You bought a Flipper Zero. +100 Happiness\n")
                    happiness = specialcombine(happiness, 100, 0, 100)
                    wait(2)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $1000. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "4":
                clearscreen()
    if key == "3":
        clearscreen()
        scrollText("You are now at the gym. What will you do? \n")
        print("[1] Workout")
        print("[2] Go back")
        key = getkey()
        if key == "1":
            clearscreen()
            scrollText("How will you work out?\n")
            print("[1] Run")
            print("[2] Lift")
            print("[3] Go back")
            key = getkey()
            if key == "1":
                clearscreen()
                scrollText("How long will you run for?\n")
                print("[1] 10 minutes")
                print("[2] 20 minutes")
                print("[3] 30 minutes")
                print("[4] Go back")
                key = getkey()
                if key == "1":
                    clearscreen()
                    scrollText("You ran for 10 minutes. +5 Happiness\n")
                    happiness = specialcombine(happiness, 5, 0, 100)
                    wait(2)
                    clearscreen()
                if key == "2":
                    clearscreen()
                    scrollText("You ran for 20 minutes. +10 Happiness\n")
                    happiness = specialcombine(happiness, 10, 0, 100)
                    wait(2)
                    clearscreen()
                if key == "3":
                    clearscreen()
                    scrollText("You ran for 30 minutes. +15 Happiness\n")
                    happiness = specialcombine(happiness, 15, 0, 100)
                    wait(2)
                    clearscreen()
                if key == "4":
                    clearscreen()
            if key == "2":
                clearscreen()
                scrollText("How long will you lift for?\n")
                print("[1] 10 minutes")
                print("[2] 20 minutes")
                print("[3] 30 minutes")
                print("[4] Go back")
                key = getkey()
                if key == "1":
                    clearscreen()
                    scrollText("You lifted for 10 minutes. +5 Happiness\n")
                    happiness = specialcombine(happiness, 5, 0, 100)
                    wait(2)
                    clearscreen()
                if key == "2":
                    clearscreen()
                    scrollText("You lifted for 20 minutes. +10 Happiness\n")
                    happiness = specialcombine(happiness, 10, 0, 100)
                    wait(2)
                    clearscreen()
                if key == "3":
                    clearscreen()
                    scrollText("You lifted for 30 minutes. +15 Happiness\n")
                    happiness = specialcombine(happiness, 15, 0, 100)
                    wait(2)
                    clearscreen()
                if key == "4":
                    clearscreen()
        scrollText("You are now super tired. What will you do?\n")
        print("[1] Go home")
        print("[2] Grab an energy drink")
        print("[3] Drink water")
        print("[4] Go back")
        key = getkey()
        if key == "1":
            clearscreen()
            scrollText("You went home. +5 Happiness\n")
            happiness = specialcombine(happiness, 5, 0, 100)
            wait(2)
            clearscreen()
        if key == "2":
            clearscreen()
            scrollText("What brand of energy drink will you get?\n")
            print("[1] Monster - $2")
            print("[2] Red Bull - $3")
            print("[3] Ghost - $4")
            print("[4] Go back")
            key = getkey()
            if key == "1":
                if balance >= 2:
                    balance -= 2
                    scrollText("You bought a Monster. +5 Happiness\n")
                    happiness = specialcombine(happiness, 5, 0, 100)
                    wait(2)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $2. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "2":
                if balance >= 3:
                    balance -= 3
                    scrollText("You bought a Red Bull. +10 Happiness\n")
                    scrollText("Wait..what? You have..wings! You are flying!\n")
                    wait(2)
                    scrollText("Oh, it turned out to be a dream. -20 Happiness\n")
                    daycompleted = True
                    happiness = specialcombine(happiness, -20, 0, 100)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $3. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "3":
                if balance >= 4:
                    balance -= 4
                    scrollText("You bought a Ghost. +15 Happiness\n")
                    happiness = specialcombine(happiness, 15, 0, 100)
                    wait(2)
                    clearscreen()
                else:
                    scrollText(f"You don't have enough money. You need $4. You only have ${balance}\n")
                    wait(2)
                    clearscreen()
            if key == "4":
                clearscreen()
        if key == "3":
            clearscreen()
            scrollText("You drank water. +5 Happiness\n")
            happiness = specialcombine(happiness, 5, 0, 100)
            wait(2)
            clearscreen()
        if key == "4":
            clearscreen()
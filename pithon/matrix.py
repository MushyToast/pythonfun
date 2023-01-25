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
    os.system("clear")

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
scrollText(pyfiglet.figlet_format("The", font="big"), 0.000001)
scrollText(pyfiglet.figlet_format("Matrix", font="big"), 0.000001)

#VARIABLES
balance = 500
day = -1
totaldays = 0
friends = []
jobsfiredfrom = []
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


gfirst = ["Olivia", "Emma", "Ava", "Charlotte", "Harper", "Avery", "Camelia", "Sophia", "Sofia", "Luna", "Elizabeth", "Scarlett", "Madison", "Isabella", "Isabel", "Emily", "Audrey", "Mya", "Savannah", "August", "Sadie", "Hailey", "Autumn", "Quinn", "Harley", "Sonia", "Naveah", "Natalia", "Jade", "Adeline", "Alexandra", "Sandy", "Lydia", "Peyton", "Allison", "Megan", "Meghan", "Athena", "Lily", "Liliana", "Fate", "Kaylee", "Ella", "Ivy", "Charlie", "Jessie", "Alex", "Miley", "Madi", "Bella", "Anabella", "Ximena", "Xochitl", "Carmen", "Kylie", "Zoe", "Zoey", "Alyssa", "May", "Mei", "Rachel", "Alexis", "Julia", "Karla", "Amanda", "Amelia", "Mia", "Illa", "Arya", "Annabel", "Annabella"]

bfirst = ["Nolan", "Alex", "Marcus", "Daniel", "Benjamin", "George", "Liam", "Lucas", "Noah", "Oliver", "Gavin", "James", "Alexander", "Jacob", "Levi", "Sebastian", "Joseph", "John", "David", "Brian", "Reid", "Joaquin", "Morgan", "Wyatt", "Matthew", "Luke", "Asher", "Carter", "Leo", "Jayden", "Isaiah", 'Isiah', "Christian", "Thomas", "Tommy", "Kingston", "Michael", "Jackson", "Finn", "Mason", "Jason", "Jay", "Hayden", "Andrew", "Keil", "Tyler", "Cameron", "Samuel", "Sam", "Martin", "Ruben", "Marco", "Lukas", "CJ", "Aidan"]

lastnames = ["Smith", "Johnson", "Davis", "Martinez", "Lopez", "Patel", "Lee", "Harris", "Sanchez", "Munoz", "Clark", "Lewis", "Miller", "Young", "Scott", "Torres", "Frausto", "King", "Richards", "Ying", "Su", "Green", "Adams", "Nelson", "Baker", "Rivera", "Cervantes", "Contreras", "Roberts", "Carter", "Brady", "Gallegos", "Jenner", "Swift", "Shannon", "Papik", "Reasin", "Cardenas", "Maldonado", "Cintron", "Royes", "Bivens", "Eden", "Guy", "Hernandez", "Kuehfuss", "Rivas", "Laguitao", "Jackson", "Friedman", "Fletcher", "Flynn", "McCaleb", "McDonald", "Middleton", "Thiel", "Flock", "Hart", "David", "Wilson", "Anderson", "Mercury", "Martin", "Depp", "Scott", "Nathan", "Morgan", "Rusch"]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#ACTUAL CODE

scrollText("This is the Matrix. A never ending cycle. Go to work. Get paid. Go to work. Get paid. \n", 0.01)
scrollText("You are fresh out of college. You have no job. You have no money. You are single. \n", 0.01)
print("Game starting momentarily...")
while True:
    clearscreen()
    if daycompleted == True:
        balance += 10
        totaldays += 1
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
    print(jobsfiredfrom)
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
                scrollText("It is now your lunch break \n", 0.01)
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
                if random.randint(3, 3) == 3:
                    if job == "Dunder Mifflin":
                        scrollText("You see your boss, Michael Scott at work. He is busy flirting with Pam at the reception desk. What do you do? \n")
                        print("[1] Talk to your boss")
                        print("[2] Do nothing")
                        print("[3] Request a raise")
                        print("[4] Tell Jim Halpert")
                        key = getkey()
                        if key == "1":
                            scrollText("You talked to Michael Scott. +10 XP \n")
                            experience += 5
                            wait(0.5)
                            clearscreen()
                        if key == "3":
                            scrollText("You requested a raise. \n")
                            determiner = random.randint(1, 10)
                            fireddeterminer = random.randint(1, 200)
                            if determiner == 13:
                                scrollText("Michael Scott said yes! +10 XP \n")
                                experience += 10
                                jobinfo[job]["WeeklyPay"] += random.randint(50, 100)
                                wait(2)
                                clearscreen()
                            else:
                                if fireddeterminer == 69:
                                    scrollText("Michael Scott said no. I guess he was in a bad mood because he fired you. -15 happiness \n")
                                    jobsfiredfrom.append(job)
                                    job = "Unemployed"
                                    fireddeterminer = 69
                                    happiness = specialcombine(happiness, -15, 0, 100)
                                    wait(2)
                                    clearscreen()
                                    daycompleted = True
                                else:
                                    scrollText("Michael Scott said no. -1 XP, -5 happiness \n")
                                    experience -= 1
                                    happiness = specialcombine(happiness, -5, 0, 100)
                                    wait(2)
                                    clearscreen()
                        if key == "4":
                            scrollText("You told Jim Halpert. \n")
                            scrollText("Jim is angry. He tells Michael Scott. \n")
                            scrollText("Michael Scott is angry. He fires you. -15 happiness \n")
                            jobsfiredfrom.append(job)
                            job = "Unemployed"
                            fireddeterminer = 69
                            happiness = specialcombine(happiness, -15, 0, 100)
                    else:
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
                                    jobsfiredfrom.append(job)
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
                print(fireddeterminer)
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
                if experience >= jobinfo["Walmart"]["XPRequired"] and jobsfiredfrom.count("Walmart") == 0:
                    job = "Walmart"
                    scrollText("You are now a Walmart employee. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Walmart. Or you have been fired from Walmart recently.\n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "3":
                if experience >= jobinfo["Amazon"]["XPRequired"] and jobsfiredfrom.count("Amazon") == 1:
                    job = "Amazon"
                    scrollText("You are now an Amazon employee. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Amazon. Or you have been fired from Amazon recently\n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "4":
                if experience >= jobinfo["Google"]["XPRequired"] and jobsfiredfrom.count("Google") == 0:
                    job = "Google"
                    scrollText("You are now a Google employee. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Google. Or you have been fired from Google recently\n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "5":
                if experience >= jobinfo["Microsoft"]["XPRequired"] and jobsfiredfrom.count("Microsoft") == 0:
                    job = "Microsoft"
                    scrollText("You are now a Microsoft employee.\n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Microsoft. Or you have been fired from Microsoft recently\n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "6":
                if experience >= jobinfo["Apple"]["XPRequired"] and jobsfiredfrom.count("Apple") == 0:
                    job = "Apple"
                    scrollText("You are now an Apple employee. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Apple. Or you have been fired from Apple recently.\n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "7":
                if experience >= jobinfo["IT Tech"]["XPRequired"] and jobsfiredfrom.count("IT Tech") == 0:
                    job = "IT Tech"
                    scrollText("You are now an IT Tech. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to be an IT Tech. Or you have been fired from being an IT Tech recently.\n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "8":
                if experience >= jobinfo["Dunder Mifflin"]["XPRequired"] and jobsfiredfrom.count("Dunder Mifflin") == 0:
                    job = "Dunder Mifflin"
                    scrollText("You are now a Dunder Mifflin employee. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to work at Dunder Mifflin. Or you have been fired from Dunder Mifflin recently.\n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "9":
                if experience >= jobinfo["Teacher"]["XPRequired"] and jobsfiredfrom.count("Teacher") == 0:
                    job = "Teacher"
                    scrollText("You are now a teacher. \n", 0.01)
                    wait(2)
                    clearscreen()
                else:
                    scrollText("You don't have enough experience to be a teacher. Or you have been fired from being a teacher recently.\n", 0.01)
                    wait(2)
                    clearscreen()
            if key == "q":
                job = "Unemployed"
                scrollText("You are now unemployed. \n", 0.01)
                wait(2)
                clearscreen()
            if key == "0":
                clearscreen()
        key = None
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
                    itemsinfridge += 1
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
                    itemsinfridge += 1
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
                    itemsinfridge += 1
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
        key = None
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
        key = None
    if key == "4":
        scrollText("You are now at the park. What will you do?\n")
        print("[1] Play on the swings")
        print("[2] Play on the slide")
        print("[3] Play on the monkey bars")
        print("[4] Go on a peaceful walk")
        print("[5] Go back")
        key = getkey()
        if key == "1":
            clearscreen()
            scrollText("You played on the swings. +1 Happiness\n")
            happiness = specialcombine(happiness, 1, 0, 100)
            wait(2)
            clearscreen()
            if random.randint(1, 5) == 2:
                scrollText("You fell off the swings! -10 Happiness\n")
                happiness = specialcombine(happiness, -10, 0, 100)
                wait(2)
                clearscreen()
            elif random.randint(1, 5) == 3:
                scrollText("A kid made fun of you for playing on the swings. -5 Happiness\n")
                happiness = specialcombine(happiness, -5, 0, 100)

        if key == "2":
            clearscreen()
            scrollText("You played on the slide. +1 Happiness\n")
            happiness = specialcombine(happiness, 1, 0, 100)
            wait(2)
            clearscreen()
            if random.randint(1, 5) == 2:
                scrollText("You fell off the slide! -10 Happiness\n")
                happiness = specialcombine(happiness, -10, 0, 100)
                wait(2)
                clearscreen()
            elif random.randint(1, 5) == 3:
                scrollText("A kid made fun of you for playing on the slide. -5 Happiness\n")
                happiness = specialcombine(happiness, -5, 0, 100)
        if key == "3":
            clearscreen()
            scrollText("You played on the monkey bars. +1 Happiness\n")
            happiness = specialcombine(happiness, 1, 0, 100)
            wait(2)
            clearscreen()
            if random.randint(1, 5) == 2:
                scrollText("You fell off the monkey bars! -10 Happiness\n")
                happiness = specialcombine(happiness, -10, 0, 100)
                wait(2)
                clearscreen()
            elif random.randint(1, 5) == 3:
                scrollText("A kid made fun of you for playing on the monkey bars. -5 Happiness\n")
                happiness = specialcombine(happiness, -5, 100)
        if key == "4":
            clearscreen()
            scrollText("You went on a peaceful walk. +1 Happiness\n")
            happiness = specialcombine(happiness, 1, 0, 100)
            if random.randint(1, 5) == 3:
                scrollText("You found a $1 bill on the ground! +1 Money\n")
                balance += 1
            elif random.randint(1, 5) == 4:
                    scrollText("You come across a good looking woman while walking. What do you do?\n")
                    print("[1] Talk to her")
                    print("[2] Ignore her")
                    print("[3] Befriend her")
                    key = getkey()
                    if key == "1":
                        clearscreen()
                        scrollText("You talked to her. +2 Happiness\n")
                        happiness = specialcombine(happiness, 2, 0, 100)
                        wait(2)
                        clearscreen()
                    if key == "2":
                        clearscreen()
                    if key == "3":
                        clearscreen()
                        scrollText("You befriended her. +3 Happiness\n")
                        hername = random.choice(gfirst) + " " + random.choice(lastnames)
                        scrollText(f"Her name is {hername}.\n")
                        happiness = specialcombine(happiness, 3, 0, 100)
                        friends.append(hername)
                        wait(2)
                        clearscreen()
            wait(2)
            clearscreen()
            key = None
    if key == "a":
        experience += 10000
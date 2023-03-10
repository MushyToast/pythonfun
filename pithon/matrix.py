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
assets = []
allowedserialkiller = False
tookDayOff = False
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
    "McDonalds": {"WeeklyPay": 620, "WeeklyHours": 40, "XPRequired": 0}, #
    "Walmart": {"WeeklyPay": 800, "WeeklyHours": 40, "XPRequired": 25}, #
    "Amazon": {"WeeklyPay": 900, "WeeklyHours": 40, "XPRequired": 35}, 
    "Google": {"WeeklyPay": 1000, "WeeklyHours": 50, "XPRequired": 60},
    "Microsoft": {"WeeklyPay": 1200, "WeeklyHours": 50, "XPRequired": 100},
    "Apple": {"WeeklyPay": 1250, "WeeklyHours": 50, "XPRequired": 120}, #
    "IT Tech": {"WeeklyPay": 1300, "WeeklyHours": 55, "XPRequired": 150}, #
    "Dunder Mifflin": {"WeeklyPay": 1500, "WeeklyHours": 60, "XPRequired": 69}, #
    "Teacher": {"WeeklyPay": 900, "WeeklyHours": 60, "XPRequired": 60}, #

}

tips = ["Don't put your coworkers stapler in the microwave while it's in Jell-O and turn it on", "Don't ask your boss for a raise when he's in a bad mood", "Buy electronics to surf the web", "Don't say iPhones are the same."]

gfirst = ["Olivia", "Emma", "Ava", "Charlotte", "Harper", "Avery", "Camelia", "Sophia", "Sofia", "Luna", "Elizabeth", "Scarlett", "Madison", "Isabella", "Isabel", "Emily", "Audrey", "Mya", "Savannah", "August", "Sadie", "Hailey", "Autumn", "Quinn", "Harley", "Sonia", "Naveah", "Natalia", "Jade", "Adeline", "Alexandra", "Sandy", "Lydia", "Peyton", "Allison", "Megan", "Meghan", "Athena", "Lily", "Liliana", "Fate", "Kaylee", "Ella", "Ivy", "Charlie", "Jessie", "Alex", "Miley", "Madi", "Bella", "Anabella", "Ximena", "Xochitl", "Carmen", "Kylie", "Zoe", "Zoey", "Alyssa", "May", "Mei", "Rachel", "Alexis", "Julia", "Karla", "Amanda", "Amelia", "Mia", "Illa", "Arya", "Annabel", "Annabella"]

bfirst = ["Nolan", "Alex", "Marcus", "Daniel", "Benjamin", "George", "Liam", "Lucas", "Noah", "Oliver", "Gavin", "James", "Alexander", "Jacob", "Levi", "Sebastian", "Joseph", "John", "David", "Brian", "Reid", "Joaquin", "Morgan", "Wyatt", "Matthew", "Luke", "Asher", "Carter", "Leo", "Jayden", "Isaiah", 'Isiah', "Christian", "Thomas", "Tommy", "Kingston", "Michael", "Jackson", "Finn", "Mason", "Jason", "Jay", "Hayden", "Andrew", "Keil", "Tyler", "Cameron", "Samuel", "Sam", "Martin", "Ruben", "Marco", "Lukas", "CJ", "Aidan"]

lastnames = ["Smith", "Johnson", "Davis", "Martinez", "Lopez", "Patel", "Lee", "Harris", "Sanchez", "Munoz", "Clark", "Lewis", "Miller", "Young", "Scott", "Torres", "Frausto", "King", "Richards", "Ying", "Su", "Green", "Adams", "Nelson", "Baker", "Rivera", "Cervantes", "Contreras", "Roberts", "Carter", "Brady", "Gallegos", "Jenner", "Swift", "Shannon", "Papik", "Reasin", "Cardenas", "Maldonado", "Cintron", "Royes", "Bivens", "Eden", "Guy", "Hernandez", "Kuehfuss", "Rivas", "Laguitao", "Jackson", "Friedman", "Fletcher", "Flynn", "McCaleb", "McDonald", "Middleton", "Thiel", "Flock", "Hart", "David", "Wilson", "Anderson", "Mercury", "Martin", "Depp", "Scott", "Nathan", "Morgan", "Rusch"]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#LOADING
clearscreen()
"""
for x in range(0, random.randint(1, 10)):
    thistip = ("Loading.. Tip: " + random.choice(tips))
    tim = 0.2
    clearscreen()
    print("\ " + thistip)
    time.sleep(tim)
    clearscreen()
    print("| " + thistip)
    time.sleep(tim)
    clearscreen()
    print("/ " + thistip)
    time.sleep(tim)
    clearscreen()
    print("| " + thistip)
    time.sleep(tim)
    clearscreen()
    print("\ " + thistip)
    time.sleep(tim)
    clearscreen()
    print("\ " + thistip)
    time.sleep(tim)
    clearscreen()
    print("| " + thistip)
    time.sleep(tim)
    clearscreen()
    print("/ " + thistip)
    time.sleep(tim)
    clearscreen()
    print("| " + thistip)
    time.sleep(tim)
    clearscreen()
    print("\ " + thistip)
    time.sleep(tim)
    clearscreen()
    print("\ " + thistip)
    time.sleep(tim)
    clearscreen()
    print("| " + thistip)
    time.sleep(tim)
    clearscreen()
    print("/ " + thistip)
    time.sleep(tim)
    clearscreen()
    print("| " + thistip)
    time.sleep(tim)
    clearscreen()
    print("\ " + thistip)
    time.sleep(tim)
    clearscreen()
    print("\ " + thistip)
    time.sleep(tim)
    clearscreen()
    print("| " + thistip)
    time.sleep(tim)
    clearscreen()
    print("/ " + thistip)
    time.sleep(tim)
    clearscreen()
    print("| " + thistip)
    time.sleep(tim)
    clearscreen()
    print("\ " + thistip)
clearscreen()
"""

#ACTUAL CODE 

scrollText("This is the Matrix. A never ending cycle. Go to work. Get paid. Go to work. Get paid. \n", 0.01)
scrollText("You are fresh out of college. You have no job. You have no money. You are single. \n", 0.01)
print("Game starting momentarily...")
while True:
    clearscreen()
    if daycompleted == True:
        balance += 10
        tookDayOff = False
        totaldays += 1
        day += 1
        daycompleted = False
        if allowedserialkiller == True:
            allowedserialkiller = False
            scrollText("When you woke up, you checked your phone and found breaking news.\n")
            scrollText("It reads:\n")
            print("The M4TrIx News:")
            print("----------------")
            print("BREAKING NEWS!")
            print("Serial killer spotted in the area. He was last seen at Walmart. He poisoned many of his victims with potassium cyanide. Be safe.")
            wait(2)
            clearscreen()
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
    print("==================")
    print(f"Job Experience: {experience}")
    print("Balance: $" + str(balance))
    print("Job: " + job)
    print("Happiness: " + str(happiness))
    print("[1] Work Options")
    print("[2] Go to the store")
    print("[3] Go to the gym")
    print("[4] Go to the park")
    print("[5] Go to the special store")
    print("[6] View your assets")
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
            elif tookDayOff == True:
                scrollText("You took the day off. You can't go to work. \n", 0.01)
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
                #specific job interactions
                if job == "Apple":
                    if random.randint(1, 5) == 3:
                        scrollText("A customer comes up to you, complaining that the iPhone 13 & 14 are the same. What do you do? \n", 0.01)
                        print("[1] Say the camera is different")
                        print("[2] Say the processor is different")
                        print("[3] Say the battery is different")
                        print("[4] Admit it's the same (it really is)")
                        key = getkey()
                        if key == "1":
                            scrollText("You said the camera is different. Pretty BS\n")
                            if random.randint(1, 3) == 2:
                                scrollText("The customer was not happy. -5 happiness, -5 XP \n")
                                wait(2)
                                happiness = specialcombine(happiness, -5, 0, 100)
                                experience -= 5
                                clearscreen()
                            else:
                                    scrollText("The customer was happy. +5 happiness, +5 XP \n")
                                    wait(2)
                                    happiness = specialcombine(happiness, 5, 0, 100)
                                    experience += 5
                                    clearscreen()
                        if key == "2":
                            scrollText("You said the processor is different. Most technical answer. +1 XP\n")
                            wait(2)
                            experience += 1
                            clearscreen()
                        if key == "3":
                            scrollText("You said the battery is different.\n")
                            wait(2)
                            if random.randint(1, 5) == 3:
                                scrollText("The customer was not happy. -5 happiness, -5 XP \n")
                                wait(2)
                                happiness = specialcombine(happiness, -5, 0, 100)
                                experience -= 5
                                clearscreen()
                            else:
                                scrollText("The customer was happy. +5 happiness, +5 XP \n")
                                wait(2)
                                happiness = specialcombine(happiness, 5, 0, 100)
                                experience += 5
                                clearscreen()
                            clearscreen()
                        if key == "4":
                            scrollText("You admitted it's the same.\n")
                            wait(2)
                            if random.randint(1,5) == 3:
                                scrollText("The customer was not happy, and went to the manager. -5 happiness, -5 XP \n")
                                experience -= 5
                                happiness = specialcombine(happiness, -5, 0, 100)
                                wait(2)
                                scrollText("The manager fired you. \n")
                                wait(2)
                                jobsfiredfrom.append(job)
                                job = "Unemployed"
                                clearscreen()
                            else:
                                scrollText("The customer was happy. +5 happiness, +5 XP \n")
                                wait(2)
                                happiness = specialcombine(happiness, 5, 0, 100)
                                experience += 5
                                clearscreen()
                if job == "McDonald's":
                    if random.randint(1, 5) == 3:
                        scrollText("A customer comes up to you, complaining that the fries are cold. What do you do? \n", 0.01)
                        print("[1] Say the fries are fresh")
                        print("[2] Say the fries are hot")
                        print("[3] Say the fries are warm")
                        print("[4] Admit the fries are cold (they really are)")
                        key = getkey()
                        if key == "1":
                            scrollText("You said the fries are fresh. BS, nothing from McDonald's is fresh.\n")
                            if random.randint(1, 3) == 2:
                                scrollText("The customer was not happy. -5 happiness, -5 XP \n")
                                wait(2)
                                happiness = specialcombine(happiness, -5, 0, 100)
                                experience -= 5
                                clearscreen()
                            else:
                                    scrollText("The customer was happy. +5 happiness, +5 XP \n")
                                    wait(2)
                                    happiness = specialcombine(happiness, 5, 0, 100)
                                    experience += 5
                                    clearscreen()
                        if key == "2":
                            scrollText("You said the fries are hot. Most technical answer. +1 XP\n")
                            wait(2)
                            experience += 1
                            clearscreen()
                        if key == "3":
                            scrollText("You said the fries are warm.\n")
                            wait(2)
                            if random.randint(1, 5) == 3:
                                scrollText("The customer was not happy. -5 happiness, -5 XP \n")
                                wait(2)
                                happiness = specialcombine(happiness, -5, 0, 100)
                                experience -= 5
                                clearscreen()
                            else:
                                scrollText("The customer was happy. +5 happiness, +5 XP \n")
                                wait(2)
                                happiness = specialcombine(happiness, 5, 0, 100)
                                experience += 5
                                clearscreen()
                            clearscreen()
                        if key == "4":
                            scrollText("You admitted the fries are cold.\n")
                            wait(2)
                            if random.randint(1,5) == 3:
                                scrollText("The customer was not happy, and went to the manager. -5 happiness, -5 XP \n")
                                experience -= 5
                                happiness = specialcombine(happiness, -5, 0, 100)
                                wait(2)
                                clearscreen()
                            else:
                                scrollText("The customer was happy. +5 happiness, +5 XP \n")
                                wait(2)
                                happiness = specialcombine(happiness, 5, 0, 100)
                                experience += 5
                                clearscreen()
                if job == "Dunder Mifflin":
                    if random.randint(1, 3) == 3:
                        scrollText("Your coworker, Jim Halpert plays a prank on you. He puts your stapler in Jell-O. What do you do? \n")
                        print("[1] Get mad")

                        print("[2] Laugh it off")
                        print("[3] Get revenge")
                        key = getkey()
                        if key == "1":
                            clearscreen()
                            scrollText("You got mad. -5 XP, -10 Happiness \n")
                            experience -= 5
                            happiness = specialcombine(happiness, -10, 0, 100)
                            wait(0.5)
                            clearscreen()
                        if key == "2":
                            clearscreen()
                            scrollText("You laughed it off. +5 XP, +10 Happiness \n")
                            experience += 5
                            happiness = specialcombine(happiness, 10, 0, 100)
                            wait(0.5)
                            clearscreen()
                        if key == "3":
                            clearscreen()
                            scrollText("How will you get revenge? \n")
                            print("[1] Put his stapler in Jell-O")
                            print("[2] Put his stapler in Jell-O and put it in the freezer")
                            print("[3] Put his stapler in Jell-O and put it in the microwave")
                            print("[4] Put his stapler in Jell-O and put it in the microwave and turn it on")
                            key = getkey()
                            if key == "1":
                                clearscreen()
                                scrollText("You put his stapler in Jell-O. +5 XP, +10 Happiness \n")
                                experience += 5
                                happiness = specialcombine(happiness, 10, 0, 100)
                                wait(0.5)
                                clearscreen()
                            if key == "2":
                                clearscreen()
                                scrollText("You put his stapler in Jell-O and put it in the freezer. +10 Happiness \n")
                                scrollText("Jim Halpert was not happy and told Michael Scott -5 XP\n")
                                experience -= 5
                                happiness = specialcombine(happiness, 10, 0, 100)
                                wait(0.5)
                                clearscreen()
                            if key == "3":
                                clearscreen()
                                scrollText("You put his stapler in Jell-O and put it in the microwave. +10 Happiness \n")
                                scrollText("Jim Halpert was not happy, and couldn't find his stapler. +2 happiness\n")
                                experience -= 5
                                happiness = specialcombine(happiness, 12, 0, 100)
                                wait(0.5)
                                clearscreen()
                            if key == "4":
                                clearscreen()
                                scrollText("You put his stapler in Jell-O and put it in the microwave and turned it on.\n")
                                scrollText("The microwave blew up, started a fire, and destroyed a room. You are now required to pay the damages, you have been fired, and you are going to jail for recklessness.\n")
                                scrollText("You lost the game. \n")
                                wait(5)
                                clearscreen()
                                exit()
                if job == "Teacher":
                    if random.randint(1, 3) == 3:
                        scrollText("You see a student cheating on a test. What do you do? \n")
                        print("[1] Tell the student to stop")
                        print("[2] Silently give him a zero")
                        print("[3] Call the student out")
                        key = getkey()
                        if key == "1":
                            clearscreen()
                            scrollText("You told the student to stop. +5 XP, +1 Happiness \n")
                            experience += 5
                            happiness = specialcombine(happiness, 1, 0, 100)
                            wait(0.5)
                            clearscreen()
                        if key == "2":
                            clearscreen()
                            scrollText("You gave the student a zero. +5 XP, +5 Happiness \n")
                            experience += 5
                            happiness = specialcombine(happiness, 5, 0, 100)
                            wait(0.5)
                            clearscreen()
                            wait(0.5)
                            scrollText("The student comes up to you pleading for a higher grade. What do you do? \n")
                            print("[1] Give him a higher grade")
                            print("[2] Explain that cheating is wrong")
                            print("[3] Tell him to get out of your classroom")
                            key = getkey()
                            if key == "1":
                                clearscreen()
                                scrollText("You gave the student a higher grade. -5 XP, +5 Happiness \n")
                                experience -= 5
                                happiness = specialcombine(happiness, 5, 0, 100)
                                wait(0.5)
                                clearscreen()
                            if key == "2":
                                clearscreen()
                                scrollText("You explained that cheating is wrong. +5 XP \n")
                                experience += 5
                                wait(0.5)
                                clearscreen()
                            if key == "3":
                                clearscreen()
                                scrollText("You told him to get out of your classroom.\n")
                                wait(0.5)
                                clearscreen()
                                scrollText("The student tells the principal that you are a bad teacher.\n")
                                wait(0.5)
                                scrollText("The principal comes up to you and asks what happened. What do you do? \n")
                                print("[1] Tell the truth")
                                print("[2] Lie")
                                key = getkey()
                                if key == "1":
                                    clearscreen()
                                    scrollText("You told the truth.\n")
                                    wait(0.5)
                                    scrollText("The principal tells you that you shouldn't tell a student to get out of your classroom. -10 XP \n")
                                    experience -= 10
                                    clearscreen()
                                if key == "2":
                                    clearscreen()
                                    scrollText("You lied.\n")
                                    wait(0.5)
                                    scrollText("The principal believes you. +5 XP \n")
                                    experience += 5
                                    clearscreen()
                if job == "Microsoft":
                    scrollText("E")
                if job == "IT Tech":
                    if random.randint(1, 3) == 3:
                        scrollText("A customer's computer has 37 viruses. What do you do? \n")
                        print("[1] Tell the customer to buy a new computer")
                        print("[2] Ask the customer how he got the viruses")
                        print("[3] Request that the customer sends in the computer")
                        key = getkey()
                        if key == "1":
                            clearscreen()
                            scrollText("You told the customer to buy a new computer. +5 XP\n")
                            experience += 5
                            wait(0.5)
                            clearscreen()
                        if key == "2":
                            clearscreen()
                            scrollText("You asked the customer how he got the viruses.\n")
                            wait(0.5)
                            print("The customer says he tried to download free movies from a sketchy website")
                            wait(0.5)
                            scrollText("You tell the customer that he should not download free movies from sketchy websites. +5 XP \n")
                            experience += 5
                            wait(0.5)
                            clearscreen()
                        if key == "3":
                            clearscreen()
                            scrollText("You requested that the customer sends in the computer.\n")
                            wait(0.5)
                            scrollText("The customer says that he will send in the computer.\n")
                            wait(0.5)
                            scrollText("The customer never sends in the computer. -5 XP \n")
                            experience -= 5
                            wait(0.5)
                            clearscreen()
                if job == "Walmart":
                    if random.randint(1, 3) == 3:
                        scrollText("You see a customer stealing a pack of gum. What do you do? \n")
                        print("[1] Tell the customer to stop")
                        print("[2] Do nothing. You don't get paid enough to care.")
                        print("[3] Call the police")
                        key = getkey()
                        if key == "1":
                            clearscreen()
                            scrollText("You told the customer to stop. +5 XP \n")
                            experience += 5
                            wait(0.5)
                            clearscreen()
                        if key == "3":
                            clearscreen()
                            scrollText("You called the police. +5 XP \n")
                            experience += 5
                            wait(0.5)
                            clearscreen()
                            scrollText("The police arrive and arrest the customer. +5 XP \n")
                            experience += 5
                            wait(0.5)
                            clearscreen()
                    else:
                        scrollText("A customer comes up to you asking where he can find potassium cyanide. What do you do? \n")
                        print("[1] Tell the customer that you don't know")
                        print("[2] Tell the customer that Walmart does not sell potassium cyanide")
                        print("[3] Tell the customer that you shouldn't be asking that question")
                        key = getkey()
                        if key == "1":
                            clearscreen()
                            scrollText("You told the customer that you don't know. +5 XP \n")
                            experience += 5
                            wait(0.5)
                            clearscreen()
                        if key == "2":
                            clearscreen()
                            scrollText("You told the customer that Walmart does not sell potassium cyanide. +5 XP \n")
                            experience += 5
                            wait(0.5)
                            clearscreen()
                        if key == "3":
                            clearscreen()
                            scrollText("You told the customer that you shouldn't be asking that question. +5 XP \n")
                            experience += 5
                            wait(0.5)
                            clearscreen()
                            scrollText("You have a sketchy feeling about the customer. What do you do?\n")
                            print("[1] Call the police")
                            print("[2] Do nothing")
                            key = getkey()
                            if key == "1":
                                clearscreen()
                                scrollText("You called the police. +5 XP \n")
                                experience += 5
                                wait(0.5)
                                clearscreen()
                                scrollText("The police talk to you and reveal that the customer was a serial killer. +15 XP \n")
                                experience += 15
                                wait(0.5)
                                clearscreen()
                            if key == "2":
                                clearscreen()
                                allowedserialkiller = True

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
        if key == "3":
            scrollText("You want to take the day off. What will your excuse be? \n")
            print("[1] I have a headache")
            print("[2] I have a stomach ache")
            print("[3] I have a fever")
            print("[4] Go back")
            key = getkey()
            if key == "1":
                scrollText("You said you have a headache. \n")
                tookDayOff = True
                wait(2)
                clearscreen()
            if key == "2":
                scrollText("You said you have a stomach ache. \n")
                tookDayOff = True
                wait(2)
                clearscreen()
            if key == "3":
                scrollText("You said you have a fever. \n")
                tookDayOff = True
                wait(2)
                clearscreen()
            if key == "4":
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
            key = None
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
            key = None
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
    if key == "5":
        scrollText("You are now at the specialty store. What will you do?\n")
        print("[1] View property")
        print("[2] View cars")
        print("[3] Go back")
        key = getkey()
        if key == "1":
            clearscreen()
            scrollText(f"You currently live in {residence}.\n")
            scrollText("What would you like to do?\n")
            print("[1] View houses")
            print("[2] View apartments")
            print("[3] View bigger houses")
            print("[4] View mansions")
            print("[5] Go back")
            key = getkey()
            if key == "1":
                clearscreen()
                scrollText("Houses:\n")
                print("[1] Small Craftsman - $100,000")
                print("[2] Medium Craftsman - $200,000")
                print("[3] Large Craftsman - $300,000")
                print("[4] Small Colonial - $400,000")
                print("[5] Medium Colonial - $500,000")
                print("[6] Large Colonial - $600,000")
                print("[7] Small Tudor - $700,000")
                print("[8] Medium Tudor - $800,000")
                print("[9] Large Tudor - $900,000")
                print("[q] Go back")
                key = getkey()
                if key == "1":
                    if balance >= 100000:
                        residence = "Small Craftsman"
                        balance -= 100000
                        scrollText("You bought a Small Craftsman. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "2":
                    if balance >= 200000:
                        residence = "Medium Craftsman"
                        balance -= 200000
                        scrollText("You bought a Medium Craftsman. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "3":
                    if balance >= 300000:
                        residence = "Large Craftsman"
                        balance -= 300000
                        scrollText("You bought a Large Craftsman. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "4":
                    if balance >= 400000:
                        residence = "Small Colonial"
                        balance -= 400000
                        scrollText("You bought a Small Colonial. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "5":
                    if balance >= 500000:
                        residence = "Medium Colonial"
                        balance -= 500000
                        scrollText("You bought a Medium Colonial. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "6":
                    if balance >= 600000:
                        residence = "Large Colonial"
                        balance -= 600000
                        scrollText("You bought a Large Colonial. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "7":
                    if balance >= 700000:
                        residence = "Small Tudor"
                        balance -= 700000
                        scrollText("You bought a Small Tudor. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "8":
                    if balance >= 800000:
                        residence = "Medium Tudor"
                        balance -= 800000
                        scrollText("You bought a Medium Tudor. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "9":
                    if balance >= 900000:
                        residence = "Large Tudor"
                        balance -= 900000
                        scrollText("You bought a Large Tudor. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "q":
                    clearscreen()

            if key == "2":
                clearscreen()
                scrollText("Apartments:\n")
                print("[1] Small Apartment - $100,000")
                print("[2] Medium Apartment - $200,000")
                print("[3] Large Apartment - $300,000")
                print("[4] Small Condo - $400,000")
                print("[5] Medium Condo - $500,000")
                print("[6] Large Condo - $600,000")
                print("[7] Small Penthouse - $700,000")
                print("[8] Medium Penthouse - $800,000")
                print("[9] Large Penthouse - $900,000")
                print("[q] Go back")
                key = getkey()
                if key == "1":
                    if balance >= 100000:
                        residence = "Small Apartment"
                        balance -= 100000
                        scrollText("You bought a Small Apartment. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "2":
                    if balance >= 200000:
                        residence = "Medium Apartment"
                        balance -= 200000
                        scrollText("You bought a Medium Apartment. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "3":
                    if balance >= 300000:
                        residence = "Large Apartment"
                        balance -= 300000
                        scrollText("You bought a Large Apartment. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "4":
                    if balance >= 400000:
                        residence = "Small Condo"
                        balance -= 400000
                        scrollText("You bought a Small Condo. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "5":
                    if balance >= 500000:
                        residence = "Medium Condo"
                        balance -= 500000
                        scrollText("You bought a Medium Condo. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "6":
                    if balance >= 600000:
                        residence = "Large Condo"
                        balance -= 600000
                        scrollText("You bought a Large Condo. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "7":
                    if balance >= 700000:
                        residence = "Small Penthouse"
                        balance -= 700000
                        scrollText("You bought a Small Penthouse. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "8":
                    if balance >= 800000:
                        residence = "Medium Penthouse"
                        balance -= 800000
                        scrollText("You bought a Medium Penthouse. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "9":
                    if balance >= 900000:
                        residence = "Large Penthouse"
                        balance -= 900000
                        scrollText("You bought a Large Penthouse. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "q":
                    clearscreen()

            if key == "3":
                clearscreen()
                scrollText("Bigger houses:")
                print("[1] Small Contemporary - $1,000,000")
                print("[2] Medium Contemporary - $1,500,000")
                print("[3] Large Contemporary - $2,000,000")
                print("[4] Small Modern - $2,500,000")
                print("[5] Medium Modern - $3,000,000")
                print("[6] Large Modern - $3,500,000")
                print("[q] Go back")
                key = getkey()
                if key == "1":
                    if balance >= 1000000:
                        residence = "Small Contemporary"
                        balance -= 1000000
                        scrollText("You bought a Small Contemporary. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "2":
                    if balance >= 1500000:
                        residence = "Medium Contemporary"
                        balance -= 1500000
                        scrollText("You bought a Medium Contemporary. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "3":
                    if balance >= 2000000:
                        residence = "Large Contemporary"
                        balance -= 2000000
                        scrollText("You bought a Large Contemporary. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "4":
                    if balance >= 2500000:
                        residence = "Small Modern"
                        balance -= 2500000
                        scrollText("You bought a Small Modern. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "5":
                    if balance >= 3000000:
                        residence = "Medium Modern"
                        balance -= 3000000
                        scrollText("You bought a Medium Modern. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "6":
                    if balance >= 3500000:
                        residence = "Large Modern"
                        balance -= 3500000
                        scrollText("You bought a Large Modern. +20 Happiness\n")
                        happiness = specialcombine(happiness, 20, 0, 100)
                        wait(2)
                        clearscreen()
                    else:
                        scrollText("You don't have enough money!\n")
                        wait(2)
                        clearscreen()
                if key == "q":
                    clearscreen()
    if key == "a":
        experience += 10000

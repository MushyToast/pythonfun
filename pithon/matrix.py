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


#PYFIGLET
scrollText(pyfiglet.figlet_format("The", font="big"), 0.001)
scrollText(pyfiglet.figlet_format("Matrix", font="big"), 0.001)

#VARIABLES
balance = 0
day = -1
job = "Unemployed"
residence = "Apartment"
happiness = 100
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
    day += 1
    if day == 7:
        day = 0
    if day == 5 or day == 6:
        scrollText("It's the weekend! You have no work. \n", 0.01)
    if day == 4:
        scrollText("It's Friday! Today is payday!. \n", 0.01)
        balance += jobinfo[job]["WeeklyPay"]
    weekday = weekdays[day]
    print(weekday)
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
            else:
                experience +=  random.randint(1, 10)
                scrollText("You went to work. \n", 0.01)
                wait(5)
                scrollText("Still at work... \n", 0.01)
                wait(2)
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
                    wait(2)
                    clearscreen()
                scrollText("You went back to work. \n")
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
            
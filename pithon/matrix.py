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
happiness = 100
jobinfo = {
    "Unemployed": {"WeeklyPay": 0, "WeeklyHours": 0},
    "McDonalds": {"WeeklyPay": 620, "WeeklyHours": 40},
    "Walmart": {"WeeklyPay": 800, "WeeklyHours": 40},
    "Amazon": {"WeeklyPay": 900, "WeeklyHours": 40},
    "Google": {"WeeklyPay": 1000, "WeeklyHours": 50},
    "Microsoft": {"WeeklyPay": 1200, "WeeklyHours": 50},
    "Apple": {"WeeklyPay": 1250, "WeeklyHours": 50},
    "IT Tech": {"WeeklyPay": 1300, "WeeklyHours": 60},
    "Dunder Mifflin": {"WeeklyPay": 1500, "WeeklyHours": 60},
    "Teacher": {"WeeklyPay": 900, "WeeklyHours": 60},

}

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#ACTUAL CODE

scrollText("This is the Matrix. A never ending cycle. Go to work. Get paid. Go to work. Get paid. \n", 0.01)
scrollText("You are fresh out of college. You have no job. You have no money. You are single. \n", 0.01)

while True:
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
            clearscreen()
            print("You go to work.")
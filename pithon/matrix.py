#IMPORTS
import time
import random
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

scrollText("This is the Matrix. A never ending cycle. Go to work. Get paid. Go to work. Get paid.")
scrollText("You are fresh out of college. You have no job. You have no money. You are single.")

while True:
    clearscreen()
    scrollText("You have $" + str(balance) + " in your bank account.")
    scrollText("You are " + job + " and work " + str(jobinfo[job]["WeeklyHours"]) + " hours a week.")
    scrollText("You are " + str(happiness) + "% happy.")
    scrollText("What would you like to do?")
    scrollText("1. Go to work")
    scrollText("2. Change job")
    scrollText("3. Go to the store")
    scrollText("4. Go to the gym")
    scrollText("5. Go to the bar")
    scrollText("6. Go to the casino")
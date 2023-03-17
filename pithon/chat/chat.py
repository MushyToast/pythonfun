import json
import os
from datetime import datetime
import time
from getkey import getkey
import sys
from colorama import Fore, Back, Style

data = []


def getextime():
    return round(time.time())


def getFileDir(dir):
    here = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(here, dir)
    return directory


accountdatadir = getFileDir("accounts.json")
filedir = getFileDir("chatlog.json")

with open(filedir, "r") as f:
    data = json.load(f)


def gettime():
    time = ""
    time += str(datetime.now().year)
    time += "-"
    time += str(datetime.now().month)
    time += "-"
    time += str(datetime.now().day)
    time += " "
    time += str(datetime.now().hour)
    time += ":"
    time += str(datetime.now().minute)
    return time


def saveChats():
    with open(filedir, "w") as f:
        json.dump(data, f)


def printChats():
    for chat in data:
        sys.stdout.write(Style.BRIGHT)
        print("(" + chat["Time"] + ") " +
              chat["Author"] + ": " + chat["Message"])
        sys.stdout.write(Style.RESET_ALL)


def writeToChat(authr, msg, time):
    data.append({"Author": authr, "Message": msg, "Time": time})
    saveChats()


def clearscreen():
    os.system("clear")


name = ""
done = False
usednames = ""

while True:
    if done == True:
        print("aa")
        break
    time.sleep(2)
    clearscreen()
    print("Welcome to the chat! Please login/signup!")
    print("[1] Login")
    print("[2] Signup")
    key = getkey()
    if key == "1":
        clearscreen()
        name = input("Username > ")
        password = input("Password > ")
        with open(accountdatadir, "r") as f:
            accounts = json.load(f)
        for account in accounts:
            if account["Username"] == name:
                if account["Password"] == password:
                    name = account["Username"]
                    print("Logged in! Welcome, " + name + "!")
                    time.sleep(2)
                    done = True
                else:
                    print("Incorrect password!")
                    time.sleep(2)
            else:
                print("Username not found")
                time.sleep(2)
    elif key == "2":
        clearscreen()
        name = input("Username > ")
        password = input("Password > ")
        with open(accountdatadir, "r") as f:
            accounts = json.load(f)
        for account in accounts:
            if account["Username"] == name and done != True:
                print("Username already in use!")
                time.sleep(2)
            else:
                accounts.append({"Username": name, "Password": password})
                with open(accountdatadir, "w") as f:
                    json.dump(accounts, f)
                print("Account created!")
                time.sleep(2)
                done = True
                break


print(f"Hello {name}!")

antispamcount = 0
lasttime = 0

clearscreen()
while True:
    if getextime() - lasttime < 2:
        antispamcount += 1
        if antispamcount >= 4:
            print(Fore.RED + Style.DIM + "() System: Please do not spam." + Fore.RESET + Style.RESET_ALL)
            time.sleep(5)
            clearscreen()
            antispamcount = 0
            lasttime = getextime()
    else:
        antispamcount = 0
        lasttime = getextime()
    printChats()
    msg = input("> ")
    clearscreen()
    writeToChat(name, msg, gettime())

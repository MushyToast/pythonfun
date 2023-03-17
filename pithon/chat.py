import json
import os
from datetime import datetime
import time
from colorama import Fore, Back, Style

data = []

def getextime():
    return round(time.time())

def getFileDir(dir):
    here = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(here, dir)
    return directory

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
        
        print("(" + chat["Time"] + ") " + chat["Author"] + ": " + chat["Message"])
        

def writeToChat(authr, msg, time):
    data.append({"Author": authr, "Message": msg, "Time": time})
    saveChats()

def clearscreen():
    os.system("clear")

while True:
    name = input("Welcome to the chatrooms! What's your name?\n")
    if "system" in name.lower():
        print("Name cannot contain 'system'!")
        time.sleep(1)
        clearscreen()
    else:
        clearscreen()
        break
print(f"Hello {name}!")

antispamcount = 0
lasttime = 0

clearscreen()
while True:
    if getextime() - lasttime < 2:
        antispamcount += 1
        if antispamcount >= 4:
            print("() System: Please do not spam.")
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
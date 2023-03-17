import json
import os

data = []

def getFileDir(dir):
    here = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(here, dir)
    return directory

filedir = getFileDir("chatlog.json")

with open(filedir, "r") as f:
    data = json.load(f)

def saveChats():
    with open(filedir, "w") as f:
        json.dump(data, f)

def printChats():
    for chat in data:
        print(chat["Author"] + ": " + chat["Message"])

def writeToChat(authr, msg):
    data.append({"Author": authr, "Message": msg})
    saveChats()

def clearscreen():
    os.system("clear")

name = input("Welcome to the chatrooms! What's your name?\n")
print(f"Hello {name}!")

clearscreen()
while True:
    printChats()
    msg = input()
    writeToChat(name, msg)
    clearscreen()
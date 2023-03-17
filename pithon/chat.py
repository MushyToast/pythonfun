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


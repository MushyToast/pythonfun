import json
import random
import os

def getFileDir(dir):
    here = os.path.dirname(os.path.abspath(__file__))

    directory = os.path.join(here, dir)
    return directory

coins = {"Bytecoin"}

bytecoindir = getFileDir("bytecoin.json")

with open (bytecoindir, "r") as f:
    Bytecoindata = json.load(f)

print(Bytecoindata)
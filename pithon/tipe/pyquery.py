#pyQuery, mushytoast, Make python easier
import math
import random
import sys
import time

def deleteline(lines):
    for x in range(1, lines):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

def offsetprint(text, offset):
    for x in range(0, offset):
        sys.stdout.write(" ")
    print(text)

def wait(seconds):
    time.sleep(seconds)

def rad(angle):
    return math.radians(angle)

def strlist(_list):
    for x in _list:
        sys.stdout.write(x)

def randintfromseed(min, max, seed):
    random.seed(seed)
    return random.randint(min, max)

def randint(min, max):
    return random.randint(min, max)

def setletter(newletter, string, index):
    nlist = []
    newstring = ""
    for x in string:
        nlist.append(x)
    nlist[index] = newletter
    for y in nlist:
        newstring = newstring + y
    return newstring
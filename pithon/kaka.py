from getkey import getkey
keys = []
empty = []
import json
import sys
stri = ""

def deline(amount):
    for x in range(0, amount):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


while True == True:
    key = getkey()
    keys.append(key)
    stri = ""
    for x in keys:
        stri = stri + x
    deline(9999)
    print(stri)
    f = open('keys.json', 'w').close()
    f = open('keys.json', 'w')
    json.dump(stri, f)


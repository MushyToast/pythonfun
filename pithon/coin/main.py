import json
import random
import time
import os
from getkey import getkey, keys

def getFileDir(dir):
    here = os.path.dirname(os.path.abspath(__file__))

    directory = os.path.join(here, dir)
    return directory

def saveData():
    with open (plrdatadir, "w") as f:
        json.dump(plrdata, f)

def clearscreen():
    os.system("clear")

coins = {"Bytecoin", "Catcoin", "Cryptonite"}

plrdatadir = getFileDir("playerdata.json")

with open (plrdatadir, "r") as f:
    plrdata = json.load(f)

print("\n\n\n\n\n")

while True: 
    print("Welcome to Metacoin, the futuristic cryptocurrency simulator!")
    print("You can buy, sell, and trade coins, and even mine them!")

    print("Current Data:")
    print("Cash: " + str(plrdata["PlayerCash"]))
    print("Bytecoin: " + str(plrdata["CoinHoldings"]["Bytecoin"]))
    print("Catcoin: " + str(plrdata["CoinHoldings"]["Catcoin"]))
    print("Cryptonite: " + str(plrdata["CoinHoldings"]["Cryptonite"]))
    print("~~~")
    print("Mining Power: " + str(plrdata["MiningPower"]))
    print("Miners: " + str(plrdata["Miners"]))

    print("What would you like to do?")
    print("1. Buy Miners")
    print("2. Mine")
    print("4. Buy Coins")
    print("5. Sell Coins")
    key = getkey()
    if key == "1":
        clearscreen()
        print("Which miners would you like to buy?")
        print("[1]. [1] Basic QuadroX6000 2010 - 1000 Cash - 3 Mining Power - avg 0.4 coins/min")
        print("[2]. [2] Bundle QuadroXS6000 2012 - 2000 Cash - 6 Mining Power - avg 0.8 coins/min")
        print("[3]. [3] Quadro XR1000 Mini 2013 - 3000 Cash - 9 Mining Power - avg 1.2 coins/min")
        print("[4]. [4] Quadro XR1000 2014 - 4000 Cash - 12 Mining Power - avg 1.6 coins/min")
        print("[5]. [5] Quadro X150 2015 - 5000 Cash - 15 Mining Power - avg 2.0 coins/min")
        print("[6]. [6] Quadro X200 2015 - 6000 Cash - 18 Mining Power - avg 2.4 coins/min")
        print("[7]. [7] Quadro XS200 2015 - 7000 Cash - 21 Mining Power - avg 2.8 coins/min")
        print("[8]. [8] Quadro X300 2016 - 8000 Cash - 24 Mining Power - avg 3.2 coins/min")
        print("[9]. [9] Quadro X400 2016 - 9000 Cash - 27 Mining Power - avg 3.6 coins/min")
        print("[R]. [0] Quadro X500 2019 - 10000 Cash - 30 Mining Power - avg 4.0 coins/min")
        print("[C]. [q] Quadro XS Super Series 3000 2021 - 11000 Cash - 33 Mining Power - avg 9.4 coins/min")
        print("[V]. [w] Quadro XS Super Series 4000 2021 - 12000 Cash - 36 Mining Power - avg 10.8 coins/min")
        key = getkey()
        if key == "1":
            if plrdata["PlayerCash"] >= 1000:
                plrdata["PlayerCash"] -= 1000
                plrdata["MiningPower"] += 3
                plrdata["Miners"] += 1
                saveData()
                clearscreen()
                print("You bought a Basic QuadroX6000 2010!")
            else:
                clearscreen()
                print("You don't have enough cash!")
                time.sleep(2)
                clearscreen()
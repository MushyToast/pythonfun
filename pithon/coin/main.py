import json
import random
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
    os.system("cls")

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
    print("3. Sell Miners")
print("4. Buy Coins")
print("5. Sell Coins")
key = getkey()
if key == "1":
    print("Welcome to the Miner shop!")
    print("There are 7 types of miners.")
    print("[1] Basic Miner - 1000 coins, avg 0.74 coins/min, +5 mining power")
    print("[2] Advanced Miner - 5000 coins, avg 1.5 coins/min, +10 mining power")
    print("[3] Professional Miner - 10000 coins, avg 3 coins/min, +20 mining power")
    print("[4] Elite Miner - 25000 coins, avg 5 coins/min, +30 mining power")
    print("[5] Master Miner - 50000 coins, avg 10 coins/min, +50 mining power")
    print("[6] Legendary Miner - 100000 coins, avg 20 coins/min, +100 mining power")
    print("[7] Godly Miner - 250000 coins, avg 50 coins/min, +200 mining power")
    print("Which miner would you like to buy?")
    key = getkey()
    if key == "1":
        if plrdata["PlayerCash"] >= 1000:
            plrdata["PlayerCash"] -= 1000
            plrdata["Miners"] += 1
            plrdata["MiningPower"] += 5
            print("You bought a Basic Miner!")
            clearscreen()
        else:
            print("You don't have enough money!")
            clearscreen()
    elif key == "2":
        if plrdata["PlayerCash"] >= 5000:
            plrdata["PlayerCash"] -= 5000
            plrdata["Miners"] += 1
            plrdata["MiningPower"] += 10
            print("You bought an Advanced Miner!")
            clearscreen()
        else:
            print("You don't have enough money!")
            clearscreen()
    elif key == "3":
        if plrdata["PlayerCash"] >= 10000:
            plrdata["PlayerCash"] -= 10000
            plrdata["Miners"] += 1
            plrdata["MiningPower"] += 20
            print("You bought a Professional Miner!")
            clearscreen()
        else:
            print("You don't have enough money!")
            clearscreen()
    elif key == "4":
        if plrdata["PlayerCash"] >= 25000:
            plrdata["PlayerCash"] -= 25000
            plrdata["Miners"] += 1
            plrdata["MiningPower"] += 30
            print("You bought an Elite Miner!")
            clearscreen()
        else:
            print("You don't have enough money!")
            clearscreen()
    elif key == "5":
        if plrdata["PlayerCash"] >= 50000:
            plrdata["PlayerCash"] -= 50000
            plrdata["Miners"] += 1
            plrdata["MiningPower"] += 50
            print("You bought a Master Miner!")
            clearscreen()
        else:
            print("You don't have enough money!")
            clearscreen()
    elif key == "6":
        if plrdata["PlayerCash"] >= 100000:
            plrdata["PlayerCash"] -= 100000
            plrdata["Miners"] += 1
            plrdata["MiningPower"] += 100
            print("You bought a Legendary Miner!")
            clearscreen()
        else:
            print("You don't have enough money!")
            clearscreen()
    elif key == "7":
        if plrdata["PlayerCash"] >= 250000:
            plrdata["PlayerCash"] -= 250000
            plrdata["Miners"] += 1
            plrdata["MiningPower"] += 200
            print("You bought a Godly Miner!")
            clearscreen()
        else:
            print("You don't have enough money!")
            clearscreen()
    else:
        print("Invalid input!")

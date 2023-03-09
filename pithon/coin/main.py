import json
import random
import os

def getFileDir(dir):
    here = os.path.dirname(os.path.abspath(__file__))

    directory = os.path.join(here, dir)
    return directory

coins = {"Bytecoin", "Catcoin", "Cryptonite"}

plrdatadir = getFileDir("playerdata.json")

with open (plrdatadir, "r") as f:
    Bytecoindata = json.load(f)

print("\n\n\n\n\n")

print("Welcome to Metacoin, the futuristic cryptocurrency simulator!")
print("You can buy, sell, and trade coins, and even mine them!")

print("Current Data:")
print("Cash: " + str(Bytecoindata["PlayerCash"]))
print("Bytecoin: " + str(Bytecoindata["CoinHoldings"]["Bytecoin"]))
print("Catcoin: " + str(Bytecoindata["CoinHoldings"]["Catcoin"]))
print("Cryptonite: " + str(Bytecoindata["CoinHoldings"]["Cryptonite"]))
print("~~~")
print("Mining Power: " + str(Bytecoindata["MiningPower"]))
print("Miners: " + str(Bytecoindata["Miners"]))
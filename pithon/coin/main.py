import json
import random

coins = {"Bytecoin"}

Bytecoindata = {}

with open ("home/codespace/.python/current/bin/python3/workspaces/pythonfun/pithon/coin/bytecoin.json", "r") as f:
    Bytecoindata = json.load(f)

print(Bytecoindata)
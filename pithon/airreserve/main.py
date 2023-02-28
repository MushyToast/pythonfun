import os
import json

plane1data = {}

with open ('plane1.json' ,'r') as f:
    plane1data = json.load(f)

print(plane1data)
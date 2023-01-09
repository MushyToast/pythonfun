import pyquery as pi
import random
import json

words = 0

with open('words.json', 'r') as f:
    total = json.load(f)
    print(total)
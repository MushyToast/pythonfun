import pyquery as pi
import random
import json
from colorama import Fore

words = ""

with open('pithon/tipe/words.json', 'r') as f:
    total = json.load(f)
    for x in range(1, 10):
        words += (random.choice(total)) + " "
print(words)

import pyquery as pi
import random
import json

words = []

with open('pithon/tipe/words.json', 'r') as f:
    total = json.load(f)
    for x in range(1, 10):
        words.append(random.choice(total))
for x in words:
    print(x)

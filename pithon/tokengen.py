import random
import os
from pyquery import setletter

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

def generate_token(length):
    token = 'DO-NOT-SHARE-THIS|OTG:- '
    for i in range(length):
        if random.randint(0, 1):
            token += random.choice(letters)
        elif random.randint(0, 10) != 10:
            token += random.choice(digits)
        else:
            if token.count("_") < 8:
                token += "_"
    while token.count("_") < 8:
        token = setletter("_", token, random.randint(23, len(token)-1))
    return token

print("\n\n\n\n\n")

while True:
    length = 4096
    token1 = generate_token(length)
    token2 = generate_token(length)
    print('\n')
    print(token1)
    print(token2)
    if token1 == token2:
        print("Token collision detected!")
        break

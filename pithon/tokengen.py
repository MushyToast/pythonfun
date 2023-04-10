import random
import os

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

def generate_token(length):
    token = 'DO-NOT-SHARE-THIS|OTG:-'
    for i in range(length):
        if random.randint(0, 1):
            token += random.choice(letters)
        elif random.randint(0, 10) != 10:
            token += random.choice(digits)
        else:
            token += "_"
    return token

print("\n\n\n\n\n")

while True:
    print(generate_token(4096))
    if random.randint(1, 100) == 34:
        break
    else:
        os.system('clear')

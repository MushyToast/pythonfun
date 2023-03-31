import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

def generate_token(length):
    token = 'DO-NOT-SHARE-THIS|OTG:-'
    for i in range(length):
        if random.randint(0, 1):
            token += random.choice(letters)
        else:
            token += random.choice(digits)
    return token

print("\n\n\n\n\n")

while True:
    print(generate_token(4096))
    print("\n\n\n\n\n")
    if random.randint(1, 100) == 34:
        break

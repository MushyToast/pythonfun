import random

letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

def generate_token(length):
    token = ''
    for i in range(length):
        if random.randint(0, 1):
            token += random.choice(letters)
        else:
            token += random.choice(digits)
    return token
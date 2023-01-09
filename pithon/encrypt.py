def toBinary(text):
    return ''.join(format(ord(i), '08b') for i in text)

wordflip = {
    'a': 'z',
    'b': 'y',
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'n',
    'n': 'm',
    'o': 'l',
    'p': 'k',
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd',
    'x': 'c',
    'y': 'b',
    'z': 'a'
}

text = input("Enter in text to be encrypted\n")

newtext = ""

for char in text:
    if char.isalpha() == True:
        newtext += wordflip[char.lower()]
    else:
        newtext += char

print(f"Encrypted text: {newtext}")
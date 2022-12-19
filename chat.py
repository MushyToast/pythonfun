import json

with open('chat.json', mode='r') as jsonfile:
    for x in jsonfile:
        print(x)
    jsonfile.append('yes he very much isnt')
    jsonfile.dump(jsonfile)
    for x in jsonfile:
        print(x)
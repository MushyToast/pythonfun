import json

def saveData(data):
    with open('pithon/business/saves/save.json', 'w') as f:
        json.dump(data, f)

def fetchData():
    with open('pithon/business/saves/save.json', 'r') as f:
        data = json.load(f)
    return data

def calculateOutgoings(data):
    outgoings = 0
    
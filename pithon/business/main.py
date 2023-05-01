import json

def saveData(data):
    with open('pithon/business/data.json', 'w') as f:
        json.dump(data, f)

def fetchData():
    with open('pithon/business/data.json', 'r') as f:
        data = json.load(f)
    return data


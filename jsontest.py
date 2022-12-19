import json

fle = open('jsontest.json')

py = json.load(fle)

print(py["Color"])
py["Money"]="so big"

print(py["Money"])
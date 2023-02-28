import os
import json

plane1data = {}

with open ('/home/codespaces/.python/current/bin/python3/workspaces/pythonfun/pithon/airreserve/plane1.json/' ,'r') as f:
    plane1data = json.load(f)

print(plane1data)
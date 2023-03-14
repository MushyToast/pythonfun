import requests
from time import sleep
import random
import asyncio
import os
import json

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

url = "https://api.profyle.net/api/users"
def getFileDir(dir):
    here = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(here, dir)
    return directory

params = {"userName":"quandale","displayName":"quandale","email":"h3gas7g@gmail.com","password":"qwu3ygg3gh4f73wg4897a"}

while True:
    async def main():
        passw = ""
        for i in range(0, 100):
            passw += random.choice(letters)
            params["password"] = passw
        name = ""
        for i in range(0, 63):
            name += random.choice(letters)
            name += random.choice(numbers)
            params["userName"] = name
            params["displayName"] = name
        email = ""
        for i in range(0, 5):
            email += random.choice(letters)
            email += random.choice(numbers)
            params["email"] = email + "@gmail.com"
        dir = getFileDir("count.json")
        with open(dir, "r") as f:
            count = json.load(f)
        count["count"] += 1
        
        with open(dir, "w") as f:
            json.dump(count, f)
        print(count["count"])
        print(params)
        response = requests.request("POST", url, json=params)
        print("\n\n\n\n")
        print(response)
    asyncio.run(main())
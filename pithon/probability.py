import random
import asyncio
from colorama import Fore as FORE
count = 0
async def checkNumber(number, desiredNumber, count):
    if number == desiredNumber:
        exit(FORE.GREEN + f"Desired number found: {number}, after {count} tries" + FORE.RESET)
min = input("Enter the minimum number: ")
max = input("Enter the maximum number: ")
desNum = input("Enter the desired number: ")
while True:
    count += 1
    number = random.randint(int(min), int(max))
    print(str(count) + ": " + str(number))
    asyncio.run(checkNumber(number, int(desNum), count))
    
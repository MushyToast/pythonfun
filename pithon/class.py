import random
import asyncio
count = 0
async def checkNumber(number, desiredNumber, count):
    if number == desiredNumber:
        exit(f"Desired number found: {number}, after {count} tries")
min = input("Enter the minimum number: ")
max = input("Enter the maximum number: ")
desNum = input("Enter the desired number: ")
while True:
    count += 1
    number = random.randint(1, 100000)
    print(str(count) + ": " + str(number))
    asyncio.run(checkNumber(number, 69420, count))
    
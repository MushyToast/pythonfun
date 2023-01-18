import random
import asyncio
count = 0
async def checkNumber(number, desiredNumber, count):
    if number == desiredNumber:
        exit(f"Desired number found: {number}, after {count} tries")
while True:
    count += 1
    number = random.randint(1, 1000)
    print(str(count) + ": " + number)
    asyncio.run(checkNumber(number, 69, count))
    
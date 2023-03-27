from perlin_noise import PerlinNoise
import random
import sys

noise = PerlinNoise(octaves=2, seed=random.randint(0, 999999999999))

resx = 50
resy = 50
scale = 15

def get_symbol(noisevalue):
    if noisevalue < -0.2:
        return '⬜'
    elif noisevalue < 0:
        return '⬜'
    elif noisevalue < 0.2:
        return '🔵'
    elif noisevalue < 0.3:
        return '🟨'
    else:
        return '🟨'

cells = {}

for x in range(resx):
    sys.stdout.write(str(x))
    for y in range(resy):
        sys.stdout.write(str(y))
        symbol = get_symbol(noise([x/scale, y/scale]))
        sys.stdout.write(symbol)
        cells[str(x) + ", " + str(y)] = symbol
    print('')

print("enter coordinate to get cell val")
cellx = input("x: ")
celly = input("y: ")

print(cells[str(cellx) + ", " + str(celly)])

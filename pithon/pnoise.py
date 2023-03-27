from perlin_noise import PerlinNoise
import random
import sys

customseed = 730961673295
seed = 0
if customseed == 0:
    seed = random.randint(0, 999999999999)
else:
    seed = customseed

noise = PerlinNoise(octaves=2, seed=seed)

resx = 20
resy = 20
scale = 50

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
    for y in range(resy):
        symbol = get_symbol(noise([x/scale, y/scale]))
        sys.stdout.write(symbol)
        cells[str(x) + ", " + str(y)] = symbol
    print('')

print("seed: " + str(noise.seed))
print("octaves: " + str(noise.octaves))
print("scale: " + str(scale))



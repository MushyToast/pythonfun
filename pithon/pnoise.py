from perlin_noise import PerlinNoise
import random
import sys

noise = PerlinNoise(octaves=2, seed=random.randint(0, 999999999999))

resx = 20
resy = 20
scale = 30

def get_symbol(noisevalue):
    if noisevalue < -0.2:
        return '⬜'
    elif noisevalue < 0:
        return '🪨'
    elif noisevalue < 0.2:
        return '🟩'
    elif noisevalue < 0.3:
        return '🟨'
    else:
        return '🟦'

for x in range(resx):
    for y in range(resy):
        sys.stdout.write(get_symbol(noise([x/scale, y/scale])))
    print('')

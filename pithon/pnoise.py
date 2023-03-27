from perlin_noise import PerlinNoise
import random
import sys

noise = PerlinNoise(octaves=20, seed=random.randint(0, 999999999999))

resx = 15
resy = 15
scale = 1000

def get_symbol(noisevalue):
    if noisevalue > 0.02:
        return 'a'
    elif noisevalue > 0.04:
        return 'b'
    elif noisevalue > 0.07:
        return 'c'
    elif noisevalue > 0.09:
        return 'd'
    else:
        return 'e'

for x in range(resx):
    for y in range(resy):
        sys.stdout.write(get_symbol(noise([x/scale, y/scale])))
    print('')

from perlin_noise import PerlinNoise
import random
import sys

noise = PerlinNoise(octaves=2, seed=random.randint(0, 999999999999))

resx = 50
resy = 50
scale = 1000

def get_symbol(noisevalue):
    if noisevalue < -0.5:
        return 'a'
    elif noisevalue < 0:
        return 'b'
    elif noisevalue < 0.5:
        return 'c'
    else:
        return 'd'

for x in range(resx):
    for y in range(resy):
        sys.stdout.write(get_symbol(noise([x/scale, y/scale])))
    print('')

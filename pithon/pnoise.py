from perlin_noise import PerlinNoise
import random
import sys

noise = PerlinNoise(octaves=20, seed=random.randint(0, 999999999999))

resx = 10
resy = 10
scale = 10000

def get_symbol(noisevalue):
    if noisevalue < 0.002:
        return 'a'
    elif noisevalue < 0.004:
        return 'b'
    elif noisevalue < 0.006:
        return 'c'
    elif noisevalue < 0.008:
        return 'd'
    else:
        return 'e'

for x in range(resx):
    for y in range(resy):
        print(noise([x/scale, y/scale]))

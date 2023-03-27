from perlin_noise import PerlinNoise
import random
import sys
import os 
import getkey

def clearscreen():
    os.system('clear')

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

def render(resx, resy, scale, seed, octaves, printdebuginfo):
    if seed == 0:
        seed = random.randint(0, 999999999999)
    noise = PerlinNoise(octaves=octaves, seed=seed)
    for x in range(resx):
        for y in range(resy):
            symbol = get_symbol(noise([x/scale, y/scale]))
            sys.stdout.write(symbol)
        print('')
    if printdebuginfo:
        print("seed: " + str(noise.seed))
        print("octaves: " + str(noise.octaves))
        print("scale: " + str(scale))
        return seed



scale = 16
resx = 100
resy = 100
octaves = 200
seed = render(resx, resy, scale, 0, octaves, True)

while True:
    key = getkey.getkey()
    if key == 'w':
        clearscreen()
        scale += 1
        seed = render(resx, resy, scale, seed, 2, True)
    elif key == 's':
        clearscreen()
        scale -= 1
        seed = render(resx, resy, scale, seed, 2, True)
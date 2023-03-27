from perlin_noise import PerlinNoise
import random
import sys
import os 
import getkey

def clearscreen():
    os.system('clear')

def get_symbol(noisevalue):
    if noisevalue < -0.4:
        return '⬜'
    elif noisevalue < -0.2:
        return '⬛'
    elif noisevalue < 0.2:
        if random.randint(1, 30) == 4:
            return '🟫'
        else:
            return '🟩'
    elif noisevalue < 0.3:
        return '🟨'
    else:
        return '🟦'

def render(resx, resy, scale, seed, octaves, printdebuginfo, offsetx, offsety):
    if seed == 0:
        seed = random.randint(-999999999999, 999999999999)
    noise = PerlinNoise(octaves=octaves, seed=seed)
    for x in range(resx):
        for y in range(resy):
            symbol = get_symbol(noise([x+offsetx/scale, y+offsety/scale]))
            sys.stdout.write(symbol)
        print('')
    if printdebuginfo:
        print("seed: " + str(noise.seed))
        print("octaves: " + str(noise.octaves))
        print("scale: " + str(scale))
        return seed



scale = 50
resx = 100
resy = 100
octaves = 2
seed = render(resx, resy, scale, 0, octaves, True, 0, 0)

while True:
    key = getkey.getkey()
    if key == 'e':
        clearscreen()
        scale += 1
        seed = render(resx, resy, scale, seed, octaves, True, 0, 0)
    elif key == 'q':
        clearscreen()
        scale -= 1
        seed = render(resx, resy, scale, seed, octaves, True, 0, 0)
    elif key == 'w':
        clearscreen()
        seed = render(resx, resy, scale, seed, octaves, True, 0, 1)
    elif key == 's':
        clearscreen()
        seed = render(resx, resy, scale, seed, octaves, True, 0, -1)
    elif key == 'a':
        clearscreen()
        seed = render(resx, resy, scale, seed, octaves, True, -1, 0)
    elif key == 'd':
        clearscreen()
        seed = render(resx, resy, scale, seed, octaves, True, 1, 0)
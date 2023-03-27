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
    for x in range(0+offsetx, resx+offsetx):
        for y in range(0+offsety, resy+offsety):
            symbol = get_symbol(noise([x/scale, y/scale]))
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
ofx = 0
ofy = 0
seed = render(resx, resy, scale, 0, octaves, True, ofx, ofy)


while True:
    key = getkey.getkey()
    if key == 'e':
        clearscreen()
        scale += 1
        seed = render(resx, resy, scale, seed, octaves, True, ofx, ofy)
    elif key == 'q':
        clearscreen()
        scale -= 1
        seed = render(resx, resy, scale, seed, octaves, True, ofx, ofy)
    elif key == 'w':
        clearscreen()
        ofy -= 1
        seed = render(resx, resy, scale, seed, octaves, True, ofx, ofy)
    elif key == 's':
        clearscreen()
        ofy += 1
        seed = render(resx, resy, scale, seed, octaves, True, ofx, ofy)
    elif key == 'a':
        clearscreen()
        ofx -= 1
        seed = render(resx, resy, scale, seed, octaves, True, ofx, ofy)
    elif key == 'd':
        clearscreen()
        ofx += 1
        seed = render(resx, resy, scale, seed, octaves, True, ofx, ofy)


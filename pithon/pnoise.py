#IMPORTS
from perlin_noise import PerlinNoise
import random
import sys
import os
import getkey

#FUNCTIONS

def clearscreen():
    os.system('clear')


def get_symbol(noisevalue):
    if noisevalue < -0.45:
        return '⬜'
    elif noisevalue < -0.3:
        return '⬛'
    elif noisevalue < 0:
        return '🟩'
    elif noisevalue < 0.1:
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

#VARIABLES

scale = 25 #the scale of the world, think of it as zoom, higher it is = more zoomed in
resx = 150 #the resolution of the display, higher it is = more cells, i reccomend keeping it at 150 but you can play around with it
resy = 150
octaves = 10 #the amount of octaves for the perlin noise, higher it is = more detail
ofx = 0 #the offset of the x axis. this is for the moving system, dont mess with this or the ofy variable
ofy = 0
step = 20 #the increment that you move in (cells) for the zooming and moving system
seed = render(resx, resy, scale, 0, octaves, True, ofx, ofy)

#MAIN

while True:
    key = getkey.getkey()
    if key == 'e':
        clearscreen()
        scale += step
        render(resx, resy, scale, seed, octaves, True, ofx, ofy)
    elif key == 'q':
        clearscreen()
        scale -= step
        render(resx, resy, scale, seed, octaves, True, ofx, ofy)
    elif key == 'w':
        clearscreen()
        ofx -= step
        render(resx, resy, scale, seed, octaves, True, ofx, ofy)
    elif key == 's':
        clearscreen()
        ofx += step
        render(resx, resy, scale, seed, octaves, True, ofx, ofy)
    elif key == 'a':
        clearscreen()
        ofy -= step
        render(resx, resy, scale, seed, octaves, True, ofx, ofy)
    elif key == 'd':
        clearscreen()
        ofy += step
        render(resx, resy, scale, seed, octaves, True, ofx, ofy)
    elif key == 'r':
        clearscreen()
        render(resx, resy, scale, seed, octaves, True, ofx, ofy)


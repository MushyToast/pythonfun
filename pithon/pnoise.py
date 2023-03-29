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
    if noisevalue < -0.2:
        return '⬜'
    elif noisevalue < -0.1:
        return '🟩'
    elif noisevalue < 0:
        return '🟩'
    elif noisevalue < 0.2:
        return '🟩'
    elif noisevalue < 0.3:
        return '🟨'
    else:
        return '🟦'
itemCells = {}
playerCash = 0

def checkcell(x, y):
    if str(x) + ', ' + str(y) in itemCells:
        return itemCells[str(x) + ', ' + str(y)]
    else:
        return False

for x in range(1000):
    itemCells[str(random.randint(-1000, 1000)) + ', ' + str(random.randint(-1000, 1000))] = '💵'
def getcell(x, y, seed, octaves, scale):
    noise = PerlinNoise(octaves=octaves, seed=seed)
    symbol = get_symbol(noise([x/scale, y/scale]))
    return symbol
def render(resx, resy, scale, seed, octaves, printdebuginfo, offsetx, offsety) -> int:
    if seed == 0:
        seed = random.randint(-999999999999, 999999999999)
    noise = PerlinNoise(octaves=octaves, seed=seed)
    iteratorx = 0
    iteratory = 0
    for x in range(0+offsetx, resx+offsetx):
        iteratorx += 1
        iteratory = 0
        for y in range(0+offsety, resy+offsety):
            iteratory += 1
            if iteratorx == 10 and iteratory == 10:
                playerpos = [x, y]
                sys.stdout.write('🧍')
            elif (str(x) + ', ' + str(y)) in itemCells:
                sys.stdout.write(itemCells[str(x) + ', ' + str(y)])
            else:
                symbol = get_symbol(noise([x/scale, y/scale]))
                sys.stdout.write(symbol)
            
        print('')
    print('pos: ' + str(playerpos))
    if printdebuginfo:
        print("seed: " + str(noise.seed))
        print("octaves: " + str(noise.octaves))
        print("scale: " + str(scale))
        return [seed, playerpos]

#VARIABLES

scale = 25 #the scale of the world, think of it as zoom, higher it is = more zoomed in
resx = 20 #the resolution of the display, higher it is = more cells, i reccomend keeping it at 100 but you can play around with it
resy = 20
octaves = 3 #the amount of octaves for the perlin noise, higher it is = more detail
ofx = 0 #the offset of the x axis. this is for the moving system, dont mess with this or the ofy variable
ofy = 0
step = 1 #the increment that you move in (cells) for the zooming and moving system
data = render(resx, resy, scale, 0, octaves, True, ofx, ofy)
seed = data[0]
playerpos = data[1]
playerCash = 0

#MAIN

while True:
    key = getkey.getkey()
    if key == 'e':
        clearscreen()
        scale += step
        playerpos = render(resx, resy, scale, seed, octaves, True, ofx, ofy)[1]
        print("cash: " + str(playerCash))
    elif key == 'q':
        clearscreen()
        scale -= step
        playerpos = render(resx, resy, scale, seed, octaves, True, ofx, ofy)[1]
        print("cash: " + str(playerCash))
    elif key == 'w' and getcell(playerpos[0]-1, playerpos[1], seed, octaves, scale) != '⬛' and getcell(playerpos[0]-1, playerpos[1], seed, octaves, scale) != '🟦':
        clearscreen()
        ofx -= step
        playerpos = render(resx, resy, scale, seed, octaves, True, ofx, ofy)[1]
        print("cash: " + str(playerCash))
    elif key == 's' and getcell(playerpos[0]+1, playerpos[1], seed, octaves, scale) != '⬛' and getcell(playerpos[0]+1, playerpos[1], seed, octaves, scale) != '🟦':
        clearscreen()
        ofx += step
        playerpos = render(resx, resy, scale, seed, octaves, True, ofx, ofy)[1]
        print("cash: " + str(playerCash))
    elif key == 'a' and getcell(playerpos[0], playerpos[1]-1, seed, octaves, scale) != '⬛' and getcell(playerpos[0], playerpos[1]-1, seed, octaves, scale) != '🟦':
        clearscreen()
        ofy -= step
        playerpos = render(resx, resy, scale, seed, octaves, True, ofx, ofy)[1]
        print("cash: " + str(playerCash))
    elif key == 'd' and getcell(playerpos[0], playerpos[1]+1, seed, octaves, scale) != '⬛' and getcell(playerpos[0], playerpos[1]+1, seed, octaves, scale) != '🟦':
        clearscreen()
        ofy += step
        playerpos = render(resx, resy, scale, seed, octaves, True, ofx, ofy)[1]
        print("cash: " + str(playerCash))
    elif key == 'r':
        clearscreen()
        playerpos = render(resx, resy, scale, seed, octaves, True, ofx, ofy)[1]
        print("cash: " + str(playerCash))
    elif key == 't':
        clearscreen()
        itemCells[str(playerpos[0]) + ', ' + str(playerpos[1]+1)] = '🐷'
        playerpos = render(resx, resy, scale, seed, octaves, True, ofx, ofy)[1]
        print("cash: " + str(playerCash))
    if checkcell(playerpos[0], playerpos[1]) == '💵':
        playerCash += 1
        del itemCells[str(playerpos[0]) + ', ' + str(playerpos[1])]
        clearscreen()
        playerpos = render(resx, resy, scale, seed, octaves, True, ofx, ofy)[1]
        print("cash: " + str(playerCash))
    


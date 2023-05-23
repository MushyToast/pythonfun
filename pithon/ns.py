from perlin_noise import PerlinNoise
import random
from colorama import Fore, Back, Style

noise = PerlinNoise(octaves=10, seed=random.randint(-999999999999, 999999999999))

def get_symbol(noisevalue):
    if noisevalue < -0.1:
        return Style.DIM + "●" + Style.RESET_ALL
    elif noisevalue < 0.1:
        return Style.NORMAL + "●" + Style.RESET_ALL
    else:
        return Style.BRIGHT + "●" + Style.RESET_ALL
    

for x in range(0, 100):
    for y in range(0, 100):
        symbol = get_symbol(noise([x/100, y/100]))
        print(symbol, end='')
    print('')

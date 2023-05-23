from perlin_noise import PerlinNoise
import random
from colorama import Fore, Back, Style

noise = PerlinNoise(octaves=10, seed=random.randint(-999999999999, 999999999999))

def get_symbol(noisevalue):
    if noisevalue < -0.1:
        return Style.DIM + "●"
    elif noisevalue < -0.2:
        return Fore.BLACK + "●"

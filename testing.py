import random
import time

class colors:
    red = '\033[91m'
    blue = '\033[94m'
    green = '\033[92m'
    gray = '\033[90m'
    white = '\033[97m'
    normal = '\033[0m'
    purple = '\033[95m'
    tan = '\033[93m'
    cyan = '\033[96m'
    bright = '\033[1m'

def checkrizz():
    rng = random.randint(1, 10)
    rizz = 0
    if rng == 1:
        rizz = True
    else:  
        rizz = False


    if not rizz:
        print(colors.bright + colors.red + "Rizz is not true" + colors.normal)
    else:
        print(colors.bright + colors.green + "Rizz is true" + colors.normal)

print("Test")

for i in range(100):
    checkrizz()
    time.sleep(0.05)

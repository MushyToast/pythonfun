
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

def main(text):
    print(colors.cyan + text)

main("i <3 python")



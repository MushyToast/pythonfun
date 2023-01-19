import sys
import time
import os

def clear():
    os.system('clear')


def scrollText(text):
    for i in text:
        print(i, end='')
        sys.stdout.flush()
        time.sleep(0.1)

scrollText("Hello World!")

clear()
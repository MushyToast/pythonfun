import random
import sys
import time
import pyfiglet

def scroll(text):
   for char in text:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(0.05)
result = pyfiglet.figlet_format("Random Number Generator", font="big")
print(result)

scroll("Welcome to the random number generator\n")
scroll("Enter in the range for the number. Let's start with the upper number. What do you want the max number to be?\n")
maxquartile = input()
scroll("Great, thanks!\n")
scroll("Let's do the lower number now. What do you want the min number to be?\n")
minquartile = input()
scroll("Ok, generating a random number!\n")

maxquartile = int(maxquartile)
minquartile = int(minquartile)

print("Your random number is", random.randint(minquartile, maxquartile))
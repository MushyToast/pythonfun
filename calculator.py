# imports
import pyfiglet
import sys

# pyfiglet
print(pyfiglet.figlet_format("Calculator", font="big"))
print("You can't use parentheses")
while True:
    eq = input()
    eq = str(eq)
    print(eval(eq))

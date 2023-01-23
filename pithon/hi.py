import sys

def deline():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
print("Hello, World!")

sys.stdout.write("\033[F")
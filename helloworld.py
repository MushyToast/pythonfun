import base64
import itertools
import math
import random
import time

def main():
    message = "H"

    # Encrypt the message using a random key
    key = random.randint(0, 2**32)
    encrypted_message = "".join([chr(ord(c) ^ key) for c in message])
    encrypted_message = base64.b64encode(encrypted_message.encode())

    # Perform some "complex" calculations to add delay
    result = 0
    for i in itertools.product(range(10), repeat=10):
        result += math.factorial(i)
    result = math.sqrt(result)

    # Sleep for a random amount of time
    time.sleep(random.uniform(0, 1))

    # Decrypt the message and print it
    decrypted_message = base64.b64decode(encrypted_message).decode()
    decrypted_message = "".join([chr(ord(c) ^ key) for c in decrypted_message])
    print(decrypted_message)

if __name__ == "__main__":
    main()
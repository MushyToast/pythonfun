import json
import sys

def deleteline(lines):
    for x in range(1, lines):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
name = input("What is your name? ")

def readchat():
    with open('chatlog.json', 'r') as f:
        data = json.load(f)
    for key, value in data.items():
        print(key + ": " + value)




def writechat(new_data):
    # Open the file in read mode
    with open('chatlog.json', 'r') as f:
        # Load the contents of the file into a list of dictionaries
        data = json.load(f)

    # Append the new data as a dictionary to the list
    data.append(new_data)

    # Open the file in write mode
    with open('chatlog.json', 'w') as f:
        # Write the updated data to the file
        json.dump(data, f)

while True:
    deleteline(50)
    readchat()
    msg = input()
    writechat({name: msg})

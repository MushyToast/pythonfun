import webbrowser
import openai
from getkey import getkey, keys
import os

key = os.getenv('DALLEAPIKEY')

openai.api_key = key
time = 0
lastinput = ''
while True:
    time = time + 1
    ai_prompt = ''
    uselastprompt = False
    if time != 1:
        print("Use last prompt? Y for yes, N for no.")
        key = getkey()
        if key == 'y':
            uselastprompt = True
            ai_prompt = lastinput
    if uselastprompt == False:
        ai_prompt = input("Enter in an image prompt: ")
        lastinput = ai_prompt
    print('Generating..')
    response = openai.Image.create(
        prompt=ai_prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    webbrowser.open_new_tab(image_url)
    print("Successfully generated!")


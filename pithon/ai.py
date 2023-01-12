import webbrowser
import openai
from getkey import getkey, keys
import os
from time import sleep as wait

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
        n=4,
        size="1024x1024"
    )
    urls = []
    image_url1 = response['data'][0]['url']
    image_url2 = response['data'][1]['url']
    image_url3 = response['data'][2]['url']
    image_url4 = response['data'][3]['url']
    urls.append(image_url1)
    urls.append(image_url2)
    urls.append(image_url3)
    urls.append(image_url4)
    for x in urls:
        webbrowser.open_new_tab(x)
        wait(0.1)

    print("Successfully generated!")


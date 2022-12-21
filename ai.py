import webbrowser
import openai
import getkey

key = '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'
openai.api_key = key

while True:
    print("Use last prompt? Y for yes, N for no.")
    key = getkey.getkey()
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


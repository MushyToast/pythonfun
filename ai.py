import openai
import webbrowser
key = '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'
openai.api_key = key

while True:
    ai_prompt = input("Enter in an image prompt: ")
    print('Generating..')
    response = openai.Image.create(
        prompt=ai_prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    webbrowser.open_new_tab(image_url)
    print("Successfully generated!")





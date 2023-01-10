import requests

url = input("Enter in a URL to get the HTML from\n")

r = requests.request("GET", url)

with open('requested.html', 'w') as f:
    f.write(r.text)
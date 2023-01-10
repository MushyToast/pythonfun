import requests

while True:
    url = input("Enter in a URL to get the HTML from\n")

    try:
        r = requests.request("GET", url)
    except requests.exceptions.RequestException as e:
        print(e, " Error")

    with open('requested.html', 'w') as f:
        f.write(r.text)
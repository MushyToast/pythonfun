import requests

url = 'http://mushytoast.tech'
while True:
    r = requests.request("GET", url)
    print(r.status_code)
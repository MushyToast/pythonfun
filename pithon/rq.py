import requests

i = -1
url = 'http://mushytoast.tech'
while True:
    
    r = requests.request("GET", url)
    print(r.status_code)
    i += 1
    print(str(i) + "\n\n\n\n")
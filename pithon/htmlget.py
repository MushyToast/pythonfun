import requests

url = input("Enter in a URL to get the HTML from\n")

r = requests.request("GET", url)

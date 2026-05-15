# Send a POST to httpbin.org/post with a fake login dictionary

import requests

url = "https://httpbin.org/post"

payload = {'username': 'yourname', 'password': '1234'}

r = requests.post(url, data = payload)

print(r.text)
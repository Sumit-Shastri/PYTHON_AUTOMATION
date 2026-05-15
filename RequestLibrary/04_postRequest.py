import requests

r = requests.post('https://httpbin.org/post', data={'name':'value'})
print(r.text)
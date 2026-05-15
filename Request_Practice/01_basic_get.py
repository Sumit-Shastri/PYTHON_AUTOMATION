# Fetch any webpage
# print status code + first 500 characters of HTML

import requests

url = "https://quotes.toscrape.com/"

r = requests.get(url)
print("Status code : ", r.status_code)

print("First 500 elements : ")
print(r.text[:500])
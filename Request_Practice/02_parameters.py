# Use httpbin.org/get with 3-4 your own custom params
# Print the response nicely

import requests
import json

url = "https://httpbin.org/get"

r = requests.get(url, params = {'username':'name',
                                'password':'pass',
                                'email':'mail@email',
                                'phone':'xxx'})

print(json.dumps(r.json(), indent = 4))
import requests

r1 = requests.put('https://httpbin.org/put', data = {'key' : 'value'})
print("Put request : \n")
print(r1.text)
print("\n\n\n")

print("Delete request : \n")
r2 = requests.delete('https://httpbin.org/delete')
print("\n\n\n")

print("Head request : \n")
r3 = requests.head('https://httpbin.org/get')
print("\n\n\n")

print("options request : \n")
r4 = requests.options('https://httpbin.org/get')


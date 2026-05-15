import requests

url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar-x64-722ar.exe"

r = requests.get(url)
totalExpectedBytes = r.headers[('Contentx`-Length')]
print("total content length : ", totalExpectedBytes)

bytesRecieved = 0

with open("winrar.exe", 'wb') as f:
    for chunk in r.iter_content(chunk_size = 128):
        print(f"{bytesRecieved} recieved out of {totalExpectedBytes}")
        f.write(chunk)
        bytesRecieved = bytesRecieved + 128


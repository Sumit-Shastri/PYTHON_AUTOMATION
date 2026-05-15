import requests

url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar-x64-722ar.exe"

r = requests.get(url)

fp = open("appli.exe", 'wb')
fp.write(r.content)
fp.close()
# Fetch books.toscrape.com
# Save full HTML into a .html file
# Open it in browser and see if it looks right

import requests

url = "https://books.toscrape.com"

r = requests.get(url)
with open("books.html", "w") as f:
    f.write(r.text)
    f.close()


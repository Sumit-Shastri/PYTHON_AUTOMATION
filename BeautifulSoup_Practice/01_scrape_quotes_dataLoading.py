# Scrape all quotes + authors from quotes.toscrape.com
# Save them to a CSV file

import requests

url = "https://quotes.toscrape.com"

r = requests.get(url)

with open("01_quotes.html", "w") as f:
    f.write(r.text)





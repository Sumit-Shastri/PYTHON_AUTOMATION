# Scrape all quotes + authors from quotes.toscrape.com
# Save them to a CSV file

import csv
from bs4 import BeautifulSoup

f = open("01_quotes.html" , "r")
data = f.read()
f.close()

soup = BeautifulSoup(data, "html.parser")

divs = soup.find_all("div", class_= "quote")

data = []
results = {}

for div in divs:

        innerTag = div.find("span", class_ = "text")
        innerTag2 = div.find("small", class_ = "author")

        quote = innerTag.get_text()
        author = innerTag2.get_text()

        data.append((quote, author))


with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])
    for row in data:
        writer.writerow(row)




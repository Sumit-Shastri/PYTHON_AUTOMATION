import os
import requests
from bs4 import BeautifulSoup

for file in os.listdir("htmls"):
    with open(f"htmls/{file}") as f:
        htmlContent = f.read()
        soup = BeautifulSoup(htmlContent, "html.parser")
        for link in soup.findAll("a"):
            print(link.get("href"))
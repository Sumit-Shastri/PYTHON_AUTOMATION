# Tag is one of the four kind  objects in Beautifulsoup

from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')

tag = soup.b
print(type(tag)) # <class 'bs4.element.Tag'>

# Attributes and methods of Tag


# Name
print("tag name : ", tag.name) # b

# changing
#tag.name = "blockquote"
print(tag)  # <blockquote class="boldest">Extremely bold</blockquote>

# Attributes

print("tag['class'] : ", tag['class'])

# dictionary of attributes

print("Dictionary of attributes : ", tag.attrs) # {'class': ['boldest']}



from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")
print(soup.prettify())


# Simple ways to navigate the data structure :

print("title : ", soup.title, "\n\n")   # <title> The DOrmouse Story </title>

print("title name : ", soup.title.name, "\n\n")  # title

print("title string : ", soup.title.string, "\n\n")  # The Dormouse's story

print("parent name : ", soup.title.parent.name, "\n\n")  # head

print("p : ", soup.p, "\n\n")

print("p['class'] : ", soup.p['class'], "\n\n")

print("a : ", soup.a, "\n\n")

print(" All a's : ", soup.find_all('a'), "\n\n")

print("Id = link3 : ", soup.find(id = 'link3'))



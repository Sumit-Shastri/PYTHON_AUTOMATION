import requests

links = ["https://atsslibrary.wordpress.com/library-broachers",
         "https://atsslibrary.wordpress.com/category/library-collection",
         "https://atsslibrary.wordpress.com/category/syllabus",
         "https://atsslibrary.wordpress.com/faq"]

for link in links:
    r = requests.get(link)
    with open(f"htmls/{link.split('/')[-1]}.html", 'w') as f:
        f.write(r.text)


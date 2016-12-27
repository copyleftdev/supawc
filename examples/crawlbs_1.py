import requests
from bs4 import BeautifulSoup as bs

html = requests.get("http://en.wikipedia.org/wiki/Kevin_Bacon")
soup = bs(html.content, "html.parser")
for link in soup.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

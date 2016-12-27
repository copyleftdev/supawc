import requests
from bs4 import BeautifulSoup as bs
import re


html = requests.get("http://en.wikipedia.org/wiki/Kevin_Bacon")
soup = bs(html.content, "html.parser")

for link in soup.find("div", {"id":"bodyContent"}).findAll("a",
                       href=re.compile("^(/wiki/)((?!:).)*$")):

    if 'href' in link.attrs:
        print(link.attrs['href'])

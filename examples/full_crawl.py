import requests
from bs4 import BeautifulSoup as bs
import re


target_url = "https://www.evoice.com/"

pages = set()

def getlinks(pageUrl):
    global pages
    html = requests.get(target_url+pageUrl)
    soup = bs(html.content, "html.parser")

    for link in soup.findAll("a", href=re.compile("(\/\w+\/\w+\/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:

                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getlinks(newPage)

getlinks("")

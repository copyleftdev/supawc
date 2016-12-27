import requests
from bs4 import BeautifulSoup as bs


def getTitle(url):
    try:
        html = requests.get(url)
    except Exception as e:
        return None
    try:
        bsObj = bs(html.content, "html.parser")
        title = bsObj.find('title')

    except Exception as e:
        return None
    return title.text


sites = ["http://www.google.com","http://www.yahoo.com", "http://www.cnn.com"]

for s in sites:
    print getTitle(s)

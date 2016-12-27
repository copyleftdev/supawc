import requests
from bs4 import BeautifulSoup as bs
import datetime
import random
import re



random.seed(datetime.datetime.now())

def get_Link(articleUrl):
    html = requests.get("http://en.wikipedia.org"+articleUrl)
    soup = bs(html.content, "html.parser")
    return soup.find('div', {"id": "bodyContent"}).findAll('a',
                     href=re.compile("^(/wiki/)((?!:).)*$"))


links = get_Link("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = get_Link(newArticle)

import requests
from bs4 import BeautifulSoup as bs


def get_siblings():
    html = requests.get("http://www.pythonscraping.com/pages/page3.html")
    soup = bs(html.content,"html.parser")
    for sibling in soup.findAll("tr",{"class":"gift"}):
        print(sibling.get_text())



get_siblings()

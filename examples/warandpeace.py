import requests
from bs4 import BeautifulSoup as bs

url = "http://www.pythonscraping.com/pages/warandpeace.html"


def get_red(url):
    redlst = []
    redreq = requests.get(url)
    soup = bs(redreq.content, 'html.parser')
    for redtxt in soup.findAll("span", {"class", "red"}):
        print redtxt.text

def get_green(url):
    greenlst = []
    greenreq = requests.get(url)
    soup = bs(greenreq.content, 'html.parser')
    for greentxt in soup.findAll("span", {"class", "green"}):
        print greentxt.get_text()


get_red(url)
get_green(url)

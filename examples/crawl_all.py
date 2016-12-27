import requests
from bs4 import BeautifulSoup as bs
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())



def getInternalLinks(url):
    """"Retrieve a list of all internal links found on a page"""
    internallinks = []
    pp = "(\/\w+\/\w+\/)"
    html = requests.get(url)
    soup = bs(html.content, "html.parser")

    for link in soup.findAll("a", re.compile(pp)):
        if link.attrs['href'] is None:
            if link.attrs['href'] not in internallinks:
                internallinks.append(link.attrs['href'])
    return internallinks


print getInternalLinks("http://www.evoice.com")

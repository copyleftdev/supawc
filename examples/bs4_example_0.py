import requests
from bs4 import BeautifulSoup as bs

try:
    r = requests.get("http://pythonscraping.com/pages/page1.html")
    soup = bs(r.content, "html.parser")
    print soup.html.body.h1
except Exception as e:
    print "Unable to establish connection to host"

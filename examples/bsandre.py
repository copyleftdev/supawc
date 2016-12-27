import requests
from bs4 import BeautifulSoup as bs
import re
html = requests.get("http://www.pythonscraping.com/pages/page3.html")
bsObj = bs(html.content,'html.parser')
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])

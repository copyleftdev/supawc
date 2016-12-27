import requests
from bs4 import BeautifulSoup as bs
import re




def collect_alerts():
    html = requests.get("https://www.us-cert.gov/ncas/alerts")
    soup = bs(html.content, "html.parser")

    for alert in soup.findAll("a", href=re.compile("(/ncas/alerts/TA[0-9]+-[0-9]+[a-z A-Z])")):
        if 'href' in alert.attrs:
            print(alert.attrs['href'])


collect_alerts()

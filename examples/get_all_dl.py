import requests
from bs4 import BeautifulSoup as bs
import re






def collect_dropdown_artifacts(url):

    html = requests.get(url)
    soup = bs(html.content, "html.parser")

    for dropdown in soup.findAll('select', {"class": "form-control"}):
        print dropdown.option.text


collect_dropdown_artifacts("https://qaorigin.metrofax.com/Buy-Now/Billing-Info")

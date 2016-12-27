import requests
from bs4 import BeautifulSoup as bs
import unittest
from selenium import webdriver
import xmlrunner



def prefix_content(ltp, prefix):
    remix = []

    for each_el in ltp:
        remix.append("{}{}".format(prefix,each_el))

    return remix

def clist_get_links(content):
    domains = []

    soup = bs(content, "html.parser")
    try:

        for links in soup.find_all('li'):
            domains.append(links.a['href'])
    except Exception as e:
        pass

    return domains


r = requests.get("https://www.craigslist.org/about/sites")

test_link = prefix_content(clist_get_links(r.content), "https:")



class TestCraigListFQDN(unittest.TestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome()

    def test_craiglist_FQDN(self):
        for links in test_link:
            self.driver.get(links)


    def  tearDown(self):
        self.driver.quit()






if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
                  verbosity=2, failfast=False, buffer=False, catchbreak=False)

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import unittest
import xmlrunner


def get_cl_listings():
    names = []
    urls = []
    r = requests.get("https://www.craigslist.org/about/sites")
    soup = bs(r.content, "html.parser")
    for sec in soup.findAll('li'):
        try:
            names.append(sec.get_text().encode('utf-8'))
            urls.append(sec.a['href'].encode('utf-8'))
        except Exception as e:
            pass
    return dict(zip(names, urls))


domain_listings = get_cl_listings()






class CrawlerTests(type):
    def __new__(mcs, name, bases, dict):

        def gen_test(a, b):
            def test(self):
                """Testing {}  title is present in landing page""".format(a)
                r = requests.get(b)
                self.assertEqual(r.status_code, 200)
            return test

        for k, v in domain_listings.iteritems():
                exclude = ['http:','https:']
                test_name = "test_%s" % k
                if any(x in v for x in exclude):
                    dict[test_name] = gen_test(k, v)
                else:
                    dict[test_name] = gen_test(k, "http:{}".format(v))

        return type.__new__(mcs, name, bases, dict)

class CrawlerTestSequence(unittest.TestCase):
    __metaclass__ = CrawlerTests

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
                  verbosity=2, failfast=False, buffer=False, catchbreak=False)

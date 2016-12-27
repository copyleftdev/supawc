from urllib import urlopen

html = urlopen("http://www.cnn.com")
print(html.read())

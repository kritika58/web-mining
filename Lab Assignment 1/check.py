import urllib.request
from bs4 import BeautifulSoup

url = "https://csivit.com"
html = urllib.request.urlopen(url)
print(html.getheader('Content-Type'))

soup = BeautifulSoup(html,"lxml")

if html.getheader('Content-Type')=='text/html':
    htmlBytes = html.read()
    # Note that feed() handles Strings well, but not bytes
    # (A change from Python 2.x to Python 3.x)
    htmlString = htmlBytes.decode("utf-8")
    print(htmlString)
# print(soup)
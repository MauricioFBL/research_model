import urllib.request as urllib2
from bs4 import BeautifulSoup, SoupStrainer

url = "https://remoteok.com"
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
website = opener.open(url)

html = website.read()
# print(html)
soup = BeautifulSoup(html, "html.parser")

for h in soup.find_all('h2'):
    # print(h.get('h3').text)
    print(str.strip(h.text))


# for element in soup.find_all('h3'):
#     link = element.get('text')
#     print(link)
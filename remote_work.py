import urllib.request as urllib2
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

class remoteok_scrapper():
    url = "https://remoteok.com"
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    website = opener.open(url)
    today = (str)(dt.date.today())

    html = website.read()
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    position = []
    enterprise = []
    sallarie = []
    publish = []
    # position = []
    for h in soup.find_all('h2', {"itemprop": "title"}):
        # print(h.get('h3').text)
        position.append(str.strip(h.text))
        # print(str.strip(h.text))

    for h in soup.find_all('h3', {"itemprop": "name"}):
        # print(h.get('h3').text)
        enterprise.append(str.strip(h.text))
        # print(str.strip(h.text))

    for h in soup.find_all("div", {"class": "location"}):
        sallarie.append(str.strip(h.text))
        # print(str.strip(h.text))

    for i in soup.findAll('time'):
            if i.has_attr('datetime'):
                publish.append(i['datetime'])
                print(i['datetime'])

    for a in soup.find_all('a', href=True):
        print("Found the URL:", a['href'])

    # print(sallarie)
    sallary = [element for element in sallarie if element.startswith('💰 ')]
    location = [element for element in sallarie if not element.startswith('💰 ')]

    df = pd.DataFrame(list(zip(position, enterprise,sallary,location,publish)),
                columns =['Posicion', 'Empresa','Salario','Ubicacion','Fecha de publicacion'])
    # print(df.head(5))
    print(df)
    df['Sitio'] = 'https://remoteok.com'

    print(df)
    df.to_csv(F'REMOTEOK_{today}_OFFERS.csv', encoding='utf-8-sig',index=False)



    # for element in soup.find_all('h3'):
    #     link = element.get('text')
    #     print(link)
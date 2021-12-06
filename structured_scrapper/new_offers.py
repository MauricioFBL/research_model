import urllib.request as urllib2
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
from common import config


class NewOffer:
    def __init__(self):
        self._config = config()['newoffers']
        self._queries = self._config['remoteok']['queries'] 
        self.url = self._config['remoteok']['url']
        self.soup = self._get_html(self.url)
        self._get_data(self.soup,self._queries)

    def _get_html(self, url):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        website = opener.open(url)
        html = website.read()
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def _get_data(self, soup, queries):
        print(queries)
        position = [str.strip(p.text) for p in soup.select(queries['position_name'])]
        enterprise = [str.strip(p.text) for p in soup.select(queries['enterprise_name'])]
        # location = [str.strip(p.text) for p in soup.find_all("div", {"class": "location"}) if not (str.strip(p.text)).startswith('💰 ')]
        # sallary = [str.strip(p.text) for p in soup.find_all("div", {"class": "location"}) if (str.strip(p.text)).startswith('💰 ')]
        location = [str.strip(p.text) for p in soup.select(queries['location_salary']) if not (str.strip(p.text)).startswith('💰 ')]
        sallary = [str.strip(p.text) for p in soup.select(queries['location_salary']) if (str.strip(p.text)).startswith('💰 ')]
        publish = [i['datetime'] for i in soup.select(queries['publish_date']) if i.has_attr('datetime')]
        
        position_url = [("https://remoteok.com/"+a['href']) for a in soup.find_all("a",{"rel": "noindex nofollow"})]
        position_url_2 = [("https://remoteok.com/"+a['href']) for a in soup.select(queries['offer_url'])]
        
        print("________________"*5)
        print(position_url_2,len(position_url_2))
        print("________________"*5)
        print(position_url,len(position_url))

        for h in soup.find_all("div",{'class':'description'}):
            a =''
            # print('---------------------------------------------')
            for x in h.find_all('div',{'class':'markdown'}):
                a = a + x.text
                # print(a)

        df = pd.DataFrame(list(zip(position, enterprise,sallary,location,publish,position_url)),
            columns =['Posicion', 'Empresa','Salario','Ubicacion','Fecha de publicacion', 'URL de la vacante'])
        df['Home URL'] = 'https://remoteok.com'
        df['Nombre del Sitio'] = 'REMOTEOK'
        print(df)
        today = dt.date.today()
        df.to_csv(f'REMOTEOK_{today}_offers.csv',encoding='utf-8-sig', index=False)
    


    def get_description(self,urls):
        descriptons = []
        for url in urls:
            soup = self._get_html(url)
            



if __name__=='__main__':
    a = NewOffer()
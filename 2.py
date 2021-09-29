import requests
from bs4 import BeautifulSoup

URL = 'https://yandex.ru/maps/covid19?ll=41.775580%2C54.894027&z=3'
HEADER = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177',
            'accept' : '*/*'}


def get_html(url,  params = None):
    r = requests.get(url, headers = HEADER, params = params)
    r.encoding = 'utf-8'
    return r



def get_stat(site):
    soup = BeautifulSoup(site, 'html.parser')
    a = soup.find_all('tr', class_ = 'covid-table-view__item' )

    stat = []

    for i in a: 
        b = i.find('td', class_  = "covid-table-view__item-name").get_text()
        c = i.find('span', class_ = "covid-table-view__item-cases-diff-text").get_text()
        d = i.find('td', class_  = "covid-table-view__item-deaths").get_text()
        k = [b , c , d]
        stat.append(k)
        
    for i in stat:
        for j in i:
            print(j)

    print(stat)
    


def parse(url):
    url = url
    get_html1 = get_html(url)
    if get_html1.status_code == 200:
        get_stat(get_html1.text)



parse(URL)




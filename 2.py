import requests
from bs4 import BeautifulSoup

URL = 'https://yandex.ru/web-maps/covid19'
HEADER = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177',
            'accept' : '*/*'}


def get_html(url,  params = None):
    r = requests.get(url, headers = HEADER, params = params)
    r.encoding = 'utf-8'
    return



def get_stat(site):
    soup = BeautifulSoup(site, 'html.parser')
    a = soup.find_all('tr', class_ = 'covid-table-view__item' )
    b = soup.find_all('tr', class_ = 'covid-table-view__item' )
    print(a)
    print(b)



def parse(url):
    url = url
    get_html1 = get_html(url)
    if get_html1.status_code == 200:
        get_stat(get_html1.text)
    else:
        print(get_html1.status_code)



parse(URL)




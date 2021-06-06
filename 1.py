import requests
from bs4 import BeautifulSoup

URL = 'https://yandex.ru/covid19/stat'
HEADER = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177',
            'accept' : '*/*'}


def get_html(url, params = None):
    r = requests.get(url, headers = HEADER, params = params)
    return r


def get_content(html):

    soup = BeautifulSoup(html,  'html.parser')



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()




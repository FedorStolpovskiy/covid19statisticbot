c

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADER = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177',
            'accept' : '*/*'}


def get_html(url, params = None):
    r = requests.get(url, headers = HEADER, params = params)
    return r




def get_content(html):
    soup = BeautifulSoup(html,  'html.parser')
    items = soup.find_all("a", class_ = "proposition_link")

    print(items)

    cars = []
    for item in items:
        a = item.find('div', class_ = 'proposition_equip size13')
        l = a.find('span', class_ = 'link').get_text(strip=True)
        #print(l)
        cars.append({
            'title': item.find('span', class_ ='link').get_text(strip=True),
            'additional information' : l

            

        })

    for i in cars:
        print(i)

        


    

    """print(items)"""



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()



"""
class = proposition_link

class = Additional information







"""
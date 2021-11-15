from selenium import webdriver



def main(url):
    driver = webdriver.Chrome()
    driver.get(url)
    btn = driver.find_element_by_class_name('covid-table-view__expand')
    btn.click()
    a = driver.find_elements_by_class_name('covid-table-view__item')

    stat = []

    for i in a:
        a = i.find_element_by_class_name('covid-table-view__item-name').text
        b = i.find_element_by_class_name('covid-table-view__item-cases').text
        c = i.find_element_by_class_name('covid-table-view__item-cases-diff').text
        d = i.find_element_by_class_name('covid-table-view__item-cases-diff-text').text

        k = [a, b, c, d]
        stat.append(k)

    return stat

URL = 'https://yandex.ru/maps/covid19?ll=41.775580%2C54.894027&z=3' 




if __name__ == '__main__':
    main(URL)

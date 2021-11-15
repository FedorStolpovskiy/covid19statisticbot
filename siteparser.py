from selenium import webdriver



def main(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
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


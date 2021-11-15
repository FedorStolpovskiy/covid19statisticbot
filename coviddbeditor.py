from siteparser_copy import * #сделал отдельно код просто, потому что для меня так читабельнее 
import sqlite3
import datetime

date = str(datetime.date.today())

URL = 'https://yandex.ru/maps/covid19?ll=41.775580%2C54.894027&z=3'

stat = main()

sqlite_stat = sqlite3.connect('bdforbot.db')

cur = sqlite_stat.cursor()


def input_data(stat, nowdate, sqlite_stat):
    for i in stat:
        i.insert(0, nowdate)
        cur.execute(f"INSERT INTO citiesinfo VALUES(?, ?, ?, ?, ?)", i)
    
    sqlite_stat.commit()
    return sqlite_stat

def update_data(stat, nowdate, database):#сначала удаляем данные, потом загружаем новые
    cur.execute("DELETE FROM citiesinfo")
    sqlite_stat.commit()
    input_data(stat, nowdate, database)
    return sqlite_stat

#input_data(stat, a, sqlite_stat)#вызываем эту ф-цию 1 раз

update_data(stat, date, sqlite_stat)








#0 - date, 1 - city, 2 - total, 3 - new infections, 4 - deaths 

"""
создаем бд 
вносим данные
заупскаем таймер 


удаляем данные
вносим новые 
перезапускаем таймер 
(то что после двух enter'ров нужно цеклически повторять)


"""

#statdb = open()
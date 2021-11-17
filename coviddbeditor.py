from siteparser import *
import sqlite3
import datetime
import time


URL = 'https://yandex.ru/maps/covid19?ll=41.775580%2C54.894027&z=7'


sqlite_stat = sqlite3.connect('bdforbot.db')

cur = sqlite_stat.cursor()


def input_data(stat, nowdate, sqlite_stat):
    for i in stat:
        i.insert(0, nowdate)
        cur.execute(f"INSERT INTO citiesinfo VALUES(?, ?, ?, ?, ?)", i)
    
    sqlite_stat.commit()
    return sqlite_stat

def update_data(stat, nowdate, database):
    cur.execute("DELETE FROM citiesinfo")
    sqlite_stat.commit()
    input_data(stat, nowdate, database)
    return sqlite_stat

while(True):
    date = str(datetime.date.today())
    stat = main(URL)
    update_data(stat, date, sqlite_stat)
    time.sleep(21600)

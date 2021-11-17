import telebot
import sqlite3

from telebot.types import Message


def get_stat(): 
	sqlite_stat = sqlite3.connect('bdforbot.db')
	cursor = sqlite_stat.cursor()
	cursor.execute("""SELECT * FROM citiesinfo""")
	records = cursor.fetchall()
	cursor.close()

	return records
    

records = get_stat()
records1 = []
for i in records:
	i = list(i)
	records1.append(i)




bot = telebot.TeleBot("1288067636:AAECQyobWJUOkt8W2i-NXF7ywpidVQp6RiQ")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup =telebot.types.ReplyKeyboardMarkup()
	buttonC1 = telebot.types.KeyboardButton(records[0][1])
	buttonC2 = telebot.types.KeyboardButton(records[1][1])
	buttonC3 = telebot.types.KeyboardButton(records[2][1])
	buttonC4 = telebot.types.KeyboardButton(records[3][1])
	buttonC5 = telebot.types.KeyboardButton(records[4][1])
	buttonNOT = telebot.types.KeyboardButton('Уведомления🔔')

	markup.row(buttonC1, buttonC2)
	markup.row(buttonC3, buttonC4)
	markup.row(buttonC5, buttonNOT)

	bot.send_message(message.chat.id, "Этот бот показывает количество заболевших коронавирусом", "выберете город", reply_markup=markup)
	bot.send_message(message.chat.id, "выбирете город",reply_markup=markup)



@bot.message_handler(content_types=['text'])
def out_stat(message, findcity = 0): 
	for k in records1:
		if k[1].lower() == message.text.lower(): 
			textmessage = 'Статистика короновируса по региону: {0}\nНовых случаев сегодня({1}): {2}\nВсего заболевших: {3}\nСмертей: {4}'.format(k[1], k[0], k[3], k[2], k[4])
			bot.send_message(message.chat.id, textmessage) 
			findcity = 1
			if findcity == 1: 
				break

	if message.text == 'Уведомления🔔': 
		bot.send_message(message.chat.id, 'Пока недоступно🙁')

	if findcity == 0 and message.text !='Уведомления🔔': 
		bot.send_message(message.chat.id, 'нет региона')
	

bot.polling()	

































"""
есть ли смцсл ставить это под функцию?:
конект с бд √
настройка курсора √ - alt + 251
селект и сортировка - 1 ф-ция 
передача готовых данных боту - 2 ф-ция


"""












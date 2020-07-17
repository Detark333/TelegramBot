import telebot
import requests
from bs4 import BeautifulSoup as BS

p = {'amazon': 'AMZN',
     'microsoft': 'MSFT',
     'сбербанк': 'SBER',
     'bank of america': 'BAC',
     'jp morganchase': 'JPM',
     'mcdonalds': 'MCD',
     'twitter': 'TWTR',
     'disney': 'DIS',
     'gazprom': 'GAZP',
     'rosneft': 'ROSN'}

bot = telebot.TeleBot('1312256074:AAFxu8qZNOKCM5IUEdLRoJGAMScPL2joHgU')


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты мне написал, я показываю котировки акций /start')
    bot.send_message(message.chat.id, 'Я могу показать доступные акции по команде /acts')
    bot.send_message(message.chat.id, 'Для просмотра стоимости акций введите название фирмы')

@bot.message_handler(commands=["acts"])
def start_message(message):
    for x in p.keys():
        bot.send_message(message.chat.id, x)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if str(message.text) in p.keys():
        r = requests.get('https://smart-lab.ru/forum/' + str(p[message.text]))
        html = BS(r.content, 'html.parser')
        for el in html.select('.forum_content'):
            temp_low = el.select('.forum_top_panel .nocenter .temp_micex_info .temp_micex_info_item')[0].text
        bot.send_message(message.chat.id, temp_low)
    else:
        bot.send_message(message.chat.id, "Этих акций еще нет")


if __name__ == '__main__':
    bot.polling(none_stop=True)

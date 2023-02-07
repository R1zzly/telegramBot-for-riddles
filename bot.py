import telebot
import random

from config import TOKEN
from questions import mysterys

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Приветствую вас <b>{message.from_user.first_name}</b>, правила игры в /help'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    mess = f'Я буду отправлять вам загадки вы вводите ответ. Вводить ответы нужно с 1 заглавной и остальное маленькими буквами. Чтобы начать играть /mystery'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['mystery'])
def mystery(message):
    global ran
    ran = random.randint(0, len(mysterys))
    bot.send_message(message.chat.id, mysterys[ran].desc, parse_mode='html')
    global flag
    flag = 1

@bot.message_handler(content_types=['text'])
def message_handler(message):
    if flag == 1:
        if str(mysterys[ran].answer) == message.text:
            tr = f'Правильный ответ {message.from_user.first_name}, продолжайте в том же духе'
            bot.send_message(message.chat.id, tr, parse_mode='html')

        else:
            fs = f'К сожалению не правильно, правильный ответ {mysterys[ran].answer}'
            bot.send_message(message.chat.id, fs, parse_mode='html')
    else:
        mess = f'Неизвестная команда или текст <u>{message.text}</u>, я не понимаю вас'
        bot.send_message(message.chat.id, mess, parse_mode='html')

bot.polling(none_stop=True)
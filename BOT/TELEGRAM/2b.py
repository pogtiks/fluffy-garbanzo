import telebot
import random
from telebot import types

f = open('C:\BOT\TELEGRAM\cts.txt', 'r', encoding='UTF-8')
facts =f.read().split('\n')
f.close()

f =open('C:\BOT\TELEGRAM\hinks.txt', 'r', encoding='UTF=8')
thinks = f.read().split('\n')
f.close()

bot = telebot.TeleBot('5732284121:AAE_g__CdGBmomaaJavij2V8EH1LQYmPYIE')

@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.keyboardButton('Факт')
    item2=types.KeyboardButton('Поговорка')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Нажми:n\Факи для получения интересного факта.\nПоговорка-для получения мудрой цитаты', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    elif message.text.strip() == 'Поговорка':
        answer = random.choice(thinks)
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)
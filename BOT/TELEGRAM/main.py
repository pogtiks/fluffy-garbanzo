import telebot

bot = telebot.TeleBot('5732284121:AAE_g__CdGBmomaaJavij2V8EH1LQYmPYIE')

@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Вопросы?')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, message.text )

bot.polling(none_stop=True, interval= 0)
#5732284121:AAE_g__CdGBmomaaJavij2V8EH1LQYmPYIE
import telebot,wikipedia,re


bot = telebot.TeleBot('5732284121:AAE_g__CdGBmomaaJavij2V8EH1LQYmPYIE')

wikipedia.set_lang('ru')

def getwiki (s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content
        wikimas=wikitext.split('.')
        wikimas=wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('=='in x):
                if(len((x.strip()))>3):
                    wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^{\}]*\}', '', wikitext2)
        return  wikitext2
    except Exception as e:
        return "В вики нету инфы."

@bot.message_handler(commands=['start'])
def start(m,res=False):
    bot.send_message(m.chat.id,"Отправьте любое слово и я чекну его в вики.")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id,getwiki(message.text))

bot.polling(none_stop=True, interval=0)
#5732284121:AAE_g__CdGBmomaaJavij2V8EH1LQYmPYIE
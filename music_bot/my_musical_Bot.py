import telebot
import config
import os
import time

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':        
            f = open('music/'+file, 'rb')
#            res = bot.send_voice(message.chat.id, f, None)
#            print(res)
            bot.send_voice(message.chat.id, f)
        time.sleep(3)
        
@bot.message_handler(commands=["start"])
def send_welcome(message):
    hi = ("Привет!")
    bot.reply_to(message, hi)
                    


if __name__ == '__main__':
    bot.polling(none_stop=True)
import config
import telebot
from telebot import types
from tools import save_fs
from tools import read_fs

tb = telebot.TeleBot(config.token)

@tb.message_handler(commands=["start"])
def send_welcome(message):
#    markup = types.ReplyKeyboardHide()
#    video = open('cards/start.gif', 'rb')
#    tb.send_video(message.chat.id, video)
    hi1 = ("Hi! I am Luchok!")
    hi2 = " А как тебя зовут?"
    hi = hi1 + hi2
# sendMessage
    tb.send_message(message.chat.id, hi)
    fs = 10                             
    save_fs(fs)

@tb.message_handler(content_types=["text"])
def tell_messages(message):
    final_state = int(read_fs())
# sendMessage
    hi = "Привет, " + message.text + "!"
    tb.send_message(message.chat.id, hi)
# sendMessage
    hi = "Загрузи свое фото и я расскажу о тебе все:=)"
    tb.send_message(message.chat.id, hi)  
# getFile
# Downloading a file is straightforward
# Returns a File object
    import requests
    file_info = tb.get_file(message.file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))
    
# http://telepot.readthedocs.io/en/latest/

#    https://api.telegram.org/file/bot<token>/<file_path>
# https://api.telegram.org/'231969410:AAEpcRPgFj-bSHgEUUnkFsAOTfAdc-Sp8Ws'/getUpdates
     
@tb.message_handler(commands=["help"])
def send_welcome(message):
    tb.reply_to(message, "Описантие программы")



if __name__ == '__main__':
     tb.polling(none_stop=True)
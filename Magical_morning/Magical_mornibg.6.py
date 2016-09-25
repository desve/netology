import config
import telebot
import quote
from telebot import types
from keyboad_for_bot import save_fs
from keyboad_for_bot import read_fs

tb = telebot.TeleBot(config.token)

@tb.message_handler(commands=["start"])
def send_welcome(message):
#    markup = types.ReplyKeyboardHide()
#    tb.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
    print("1")
    photo = open('photo.png', 'rb')
    print("2")
    tb.send_photo(message.chat.id, photo)
    print("3")
    tb.send_photo(message.chat.id, "FILEID")
    print("4")
    
    tb.reply_to(message, "Как тебя зовут?")
    final_state = 1                              # Начало работы
    save_fs(final_state)
                    
@tb.message_handler(commands=["help"])
def send_help(message):
    tb.reply_to(message, "Описантие программы")

@tb.message_handler(content_types=["text"])
def send_text(message):
    final_state = int(read_fs())
    if final_state == 1:                         # Начало работы. Продолжение
        hi1 = "Привет," + message.text + "!" +"\n"
        hi2 = ("А я Бот, точнее таким меня считают =:) На самом же деле , \
я - твой друг, который научит тебя никуда не опаздывать и просыпаться рано !")
        hi3 = "Как твои дела?\n\n\n"
        tb.reply_to(message, hi1) 
        tb.reply_to(message, hi2) 
        tb.reply_to(message, hi3) 

 

if __name__ == '__main__':
     tb.polling(none_stop=True)
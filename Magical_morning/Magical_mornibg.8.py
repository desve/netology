import config
import telebot
import quote
from telebot import types
from keyboad_for_bot import save_fs
from keyboad_for_bot import read_fs

tb = telebot.TeleBot(config.token)

@tb.message_handler(commands=["start"])
def send_welcome(message):
    video = open('photo.gif', 'rb')
    tb.send_video(message.chat.id, video)
    hi1 = ("Привет! Я - Бот, точнее таким меня считают =:) На самом же деле , \
я - твой друг, который научит тебя никуда не опаздывать и просыпаться рано!:))")
    hi2 = " А как тебя зовут?"
    hi = hi1 + hi2
    tb.reply_to(message, hi)
    final_state = 1                              
    save_fs(final_state)
                    
@tb.message_handler(commands=["help"])
def send_help(message):
    tb.reply_to(message, "Описантие программы")

@tb.message_handler(content_types=["text"])
def send_text(message):
    final_state = int(read_fs())
    
    if final_state == 1:                         
#        hi = "Чудесного утра, " + message.text + "!"
        hi = "Как твои дела?"
        tb.reply_to(message, hi) 
        final_state = 2                      
        save_fs(final_state)
        
    elif final_state == 2: 
        hi = "Чyдесного тебе утра, " + message.text + "!"
        tb.reply_to(message, hi) 
        final_state = 3     
        save_fs(final_state)
        markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        itembtn = types.KeyboardButton('Цитата дня')
        markup.add(itembtn)
        tb.send_message(message.chat.id, "Получи совет дня на сегодня", 
                        reply_markup=markup)
        print(8)
                        
    elif message.text == 'Цитата дня':
        print_line = quote.quote_of_the_Day()
        tb.send_message(message.chat.id, print_line)
        final_state = 4     
        save_fs(final_state)
        markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        itembtn = types.KeyboardButton('Мы в Instagram')
        markup.add(itembtn)
        tb.send_message(message.chat.id, "Присоединяйся к нам!", 
                        reply_markup=markup)
        
    elif message.text == 'Мы в Instagram':
        print_line = 'https://www.instagram.com/magical_morning/'
        tb.send_message(message.chat.id, print_line)


        

if __name__ == '__main__':
     tb.polling(none_stop=True)
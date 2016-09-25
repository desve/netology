import config
import telebot
import quote
from telebot import types

tb = telebot.TeleBot(config.token)

@tb.message_handler(commands=["start"])
def send_welcome(message):
    tb.reply_to(message, "Привет!")
    
    markup = types.ReplyKeyboardMarkup(row_width=1,              # Высота
                                       one_time_keyboard=False,  # Убрать после 
                                      )                          # использования
    itembtn1 = types.KeyboardButton('Цитата дня')
    itembtn2 = types.KeyboardButton('Мы в Instagram')
    itembtn3 = types.KeyboardButton('/start')
    markup.add(itembtn1, itembtn2, itembtn3)
    tb.send_message(message.chat.id, "Получи совет дня на сегодня", 
                    reply_markup=markup)
                    
@tb.message_handler(commands=["help"])
def send_welcome(message):
    tb.reply_to(message, "Описантие программы")

@tb.message_handler(content_types=["text"])
def repeat_all_messages(message):
#    print_line = message.text
    if message.text == 'Цитата дня':
        print_line = quote.quote_of_the_Day()
    elif message.text == 'Мы в Instagram':
        print_line = 'https://www.instagram.com/magical_morning/'
    tb.send_message(message.chat.id, print_line)

if __name__ == '__main__':
     tb.polling(none_stop=True)
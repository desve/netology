import config
import telebot
import quote
from telebot import types

tb = telebot.TeleBot(config.token)

@tb.message_handler(commands=["start"])
def send_welcome(message):
    tb.send_message(message, "text")
                    
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
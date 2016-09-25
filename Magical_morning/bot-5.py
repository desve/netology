import config
import telebot
import quote
from telebot import types

tb = telebot.TeleBot(config.token)

@tb.message_handler(commands=["start"])
def send_welcome(message):
    tb.reply_to(message, quote.quote_of_the_Day())
    
@tb.message_handler(commands=["help"])
def send_welcome(message):
    tb.reply_to(message, "Для начала работы нажмие /start")


if __name__ == '__main__':
     tb.polling(none_stop=True)
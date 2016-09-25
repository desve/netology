import config
import telebot
from telebot import types

tb = telebot.TeleBot(config.token)

@tb.message_handler(commands=["start"])
def send_welcome(message):
    tb.reply_to(message, "Начало работы")

@tb.message_handler(commands=["help"])
def send_welcome(message):
    tb.reply_to(message, "Описантие программы")

@tb.message_handler(content_types=["text"])
def repeat_all_messages(message):
    tb.send_message(message.chat.id, message.text)
    markup = types.ReplyKeyboardMarkup()
    markup.row('a', 'v')
    markup.row('c', 'd', 'e')
    tb.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)


if __name__ == '__main__':
     tb.polling(none_stop=True)
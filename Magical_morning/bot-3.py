import config
import telebot
from telebot import types

tb = telebot.TeleBot(config.token)

@tb.message_handler(content_types=["text"])
def repeat_all_messages(message):
    tb.send_message(message.chat.id, message.text)

    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('a')
    itembtn2 = types.KeyboardButton('v')
    itembtn3 = types.KeyboardButton('d')
    markup.add(itembtn1, itembtn2, itembtn3)
    tb.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)


if __name__ == '__main__':
     tb.polling(none_stop=True)
import config
import telebot
from telebot import types
from keyboad_for_bot import taro_kb
from keyboad_for_bot import save_kb
from keyboad_for_bot import read_kb
from keyboad_for_bot import save_arcan_num_1
from keyboad_for_bot import save_arcan_num
from keyboad_for_bot import read_arcan_num

tb = telebot.TeleBot(config.token)

@tb.message_handler(commands=["start"])
def send_welcome(message):
    
    markup = types.ReplyKeyboardMarkup()
    markup.row('Перетасуем колоду')
    tb.send_message(message.chat.id, "Начало гадания", reply_markup=markup)


@tb.message_handler(content_types=["text"])
def repeat_all_messages(message):
    
    if message.text == 'Перетасуем колоду':
        
        kb = []
        kb = taro_kb(22)
        save_kb(kb)                       # Запоминаем клавиатуру
        save_arcan_num_1()                # Запоминаем arcan_num = 1
        markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton(kb[0])
        btn2 = types.KeyboardButton(kb[1])
        btn3 = types.KeyboardButton(kb[2])
        btn4 = types.KeyboardButton(kb[3])
        btn5 = types.KeyboardButton(kb[4])
        btn6 = types.KeyboardButton(kb[5])   
        btn7 = types.KeyboardButton(kb[6])
        btn8 = types.KeyboardButton(kb[7])
        btn9 = types.KeyboardButton(kb[8])
        btn10 = types.KeyboardButton(kb[9])
        btn11 = types.KeyboardButton(kb[10])
        btn12 = types.KeyboardButton(kb[11])
        btn13 = types.KeyboardButton(kb[12])   
        btn14 = types.KeyboardButton(kb[13])
        btn15 = types.KeyboardButton(kb[14])
        btn16 = types.KeyboardButton(kb[15])
        btn17 = types.KeyboardButton(kb[16])
        btn18 = types.KeyboardButton(kb[17])
        btn19 = types.KeyboardButton(kb[18])
        btn20 = types.KeyboardButton(kb[19])   
        btn21 = types.KeyboardButton(kb[20])
        btn22 = types.KeyboardButton(kb[21])
        markup.row(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        markup.row(btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)
        markup.row(btn16, btn17, btn18, btn19, btn20, btn21, btn22)
        tb.send_message(message.chat.id, "Выберете карту:", reply_markup=markup)
    
    else:
        arcan_num = int(read_arcan_num()) # Подсчет выбранных карт
        print('arcan_num', arcan_num)
        arcan_num += 1
        save_arcan_num(arcan_num)
        arcan_max = 3
        if arcan_num <= arcan_max:
            kb = read_kb()
            i = -1                            # Поиск выбранной буквы
            num_del = -1
            for elem in kb:
                i += 1
                if elem == message.text:
                    num_del = i
            kb[num_del] = chr(1)               # Клавиша деактивирована
            save_kb(kb)                        # Запоминаем обновленную клавиатуру  
        
            markup = types.ReplyKeyboardMarkup(row_width=1, 
                                               one_time_keyboard=True)
            btn1 = types.KeyboardButton(kb[0])
            btn2 = types.KeyboardButton(kb[1])
            btn3 = types.KeyboardButton(kb[2])
            btn4 = types.KeyboardButton(kb[3])
            btn5 = types.KeyboardButton(kb[4])
            btn6 = types.KeyboardButton(kb[5])   
            btn7 = types.KeyboardButton(kb[6])
            btn8 = types.KeyboardButton(kb[7])
            btn9 = types.KeyboardButton(kb[8])
            btn10 = types.KeyboardButton(kb[9])
            btn11 = types.KeyboardButton(kb[10])
            btn12 = types.KeyboardButton(kb[11])
            btn13 = types.KeyboardButton(kb[12])   
            btn14 = types.KeyboardButton(kb[13])
            btn15 = types.KeyboardButton(kb[14])
            btn16 = types.KeyboardButton(kb[15])
            btn17 = types.KeyboardButton(kb[16])
            btn18 = types.KeyboardButton(kb[17])
            btn19 = types.KeyboardButton(kb[18])
            btn20 = types.KeyboardButton(kb[19])   
            btn21 = types.KeyboardButton(kb[20])
            btn22 = types.KeyboardButton(kb[21])
            markup.row(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
            markup.row(btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)
            markup.row(btn16, btn17, btn18, btn19, btn20, btn21, btn22)
            tb.send_message(message.chat.id, "Выберете карту:", 
                            reply_markup=markup)
        else:
            print("end")

@tb.message_handler(commands=["help"])
def send_welcome(message):
    tb.reply_to(message, "Описантие программы")



if __name__ == '__main__':
     tb.polling(none_stop=True)
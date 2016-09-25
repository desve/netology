import config
import telebot
from telebot import types
from keyboad_for_bot import taro_kb
from keyboad_for_bot import save_kb
from keyboad_for_bot import read_kb
from keyboad_for_bot import save_fs
from keyboad_for_bot import read_fs
from keyboad_for_bot import save_fs_2
from keyboad_for_bot import read_fs_2
from keyboad_for_bot import save_fs_3
from keyboad_for_bot import read_fs_3


tb = telebot.TeleBot(config.token)

@tb.message_handler(commands=["start"])
def send_welcome(message):
#    markup = types.ReplyKeyboardHide()
    video = open('cards/start.gif', 'rb')
    tb.send_video(message.chat.id, video)
    hi1 = ("Привет! Я - Бот, точнее таким меня считают =:) На самом же деле , \
я - твой друг, который пасскажет, что тебя ждет впереди:))")
    hi2 = " А как тебя зовут?"
    hi = hi1 + hi2
    tb.reply_to(message, hi)
    final_state = 10                              
    save_fs(final_state)

@tb.message_handler(content_types=["text"])
def tell_messages(message):
    final_state = int(read_fs())
    print(final_state)
    
    if final_state == 10:
        hi = "Привет, " + message.text + "!"
        tb.reply_to(message, hi) 
        hi = "Хочешь узнать, что тебя ждет?"
        tb.reply_to(message, hi)        
        final_state = 20     
        save_fs(final_state)
    
    elif final_state == 20:
        
        hi = "Тогда Поехали!:)"
        tb.reply_to(message, hi) 
        markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Развитие ситуации")
        btn2 = types.KeyboardButton("Принять решение")
        btn3 = types.KeyboardButton("Взаимоотношения")
        btn4 = types.KeyboardButton("Что будет")        
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        tb.send_message(message.chat.id, "Что ты хочешь узнать?", reply_markup=markup)        
        final_state = 30     
        save_fs(final_state)
      
    elif final_state == 30: 
        if message.text == "Развитие ситуации":
            final_state_2 = 10     
            save_fs_2(final_state_2)  
        elif message.text == "Принять решение":
            final_state_2 = 20     
            save_fs_2(final_state_2)              
        elif message.text == "Взаимоотношения":
            final_state_2 = 30     
            save_fs_2(final_state_2)  
        elif message.text == "Что будет":
            final_state_2 = 40     
            save_fs_2(final_state_2)   
        print(final_state_2)
        markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Крест")
        btn2 = types.KeyboardButton("План")      
        markup.row(btn1, btn2)
        tb.send_message(message.chat.id, "Для начала выбери расклад", reply_markup=markup)         
        final_state = 40     
        save_fs(final_state)      
      
    elif final_state == 40: 
        if message.text == "Крест":
            final_state_3 = 10     
            save_fs_3(final_state_3)  
        elif message.text == "План":
            final_state_3 = 20     
            save_fs_3(final_state_3)              
        markup = types.ReplyKeyboardMarkup()
        markup.row('Перетасуем колоду')
        tb.send_message(message.chat.id, "Начало гадания", reply_markup=markup)
        final_state = 50     
        save_fs(final_state)    
      
    elif final_state == 50:  
        kb = []
        kb = taro_kb(22)
        save_kb(kb)                       # Запоминаем клавиатуру
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
        final_state = 60     
        save_fs(final_state) 
        
    elif final_state == 60:  
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
    


@tb.message_handler(commands=["help"])
def send_welcome(message):
    tb.reply_to(message, "Описантие программы")



if __name__ == '__main__':
     tb.polling(none_stop=True)
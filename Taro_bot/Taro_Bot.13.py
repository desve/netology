import config
import telebot
from telebot import types
from PIL import Image
from keyboad_for_bot import taro_kb
from keyboad_for_bot import save_kb
from keyboad_for_bot import read_kb
from keyboad_for_bot import save_fs
from keyboad_for_bot import read_fs
from keyboad_for_bot import save_fs_2
from keyboad_for_bot import read_fs_2
from keyboad_for_bot import save_fs_3
from keyboad_for_bot import read_fs_3
from keyboad_for_bot import change_cards
from keyboad_for_bot import save_taro
from keyboad_for_bot import read_taro
from keyboad_for_bot import generate_markup
from image_generator import image_generator_cross
from image_generator import image_generator_plan
from image_generator import prediction


tb = telebot.TeleBot(config.token)

@tb.message_handler(commands=["start"])
def send_welcome(message):
#    markup = types.ReplyKeyboardHide()
#    video = open('cards/start.gif', 'rb')
#    tb.send_video(message.chat.id, video)
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
    final_state_2 = int(read_fs_2())
    final_state_3 = int(read_fs_3())
    print("final_state=", final_state) 
    print("final_state_2=", final_state_2) 
    print("final_state_3=", final_state_3) 
    
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
        tb.send_message(message.chat.id, "На что погадаем?", reply_markup=markup)        
        final_state = 30     
        save_fs(final_state)
      
    elif final_state == 30: 
        if message.text == "Развитие ситуации":
            final_state_2 = 10            # fs2 = 10 Развитие ситуации 
            save_fs_2(final_state_2)  
        elif message.text == "Принять решение":
            final_state_2 = 20            # fs2 = 20 Принять решение
            save_fs_2(final_state_2)              
        elif message.text == "Взаимоотношения":
            final_state_2 = 30            # fs2 = 30 Взаимоотношения
            save_fs_2(final_state_2)  
        elif message.text == "Что будет":
            final_state_2 = 40            # fs3 = 40 Что будет
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
            final_state_3 = 10            # fs3 = 10 Крест 
            save_fs_3(final_state_3)  
        elif message.text == "План":
            final_state_3 = 20            # fs3 = 20 План  
            save_fs_3(final_state_3)              
        markup = types.ReplyKeyboardMarkup()
        markup.row('Перетасуем колоду')
        tb.send_message(message.chat.id, "Начало гадания", reply_markup=markup)
        final_state = 50     
        save_fs(final_state)    
      
    elif final_state == 50:               # Начало
        kb = []
        kb = taro_kb(22)                  # Создаем клавиатуру арканов
        save_kb(kb)                       # Запоминаем клавиатуру
        taro_cards = []                   # Создаем колоду
        taro_cards = change_cards()       # Тусуем колоду
        save_taro(taro_cards)             # Запоминаем колоду
        markup = generate_markup(kb)
        tb.send_message(message.chat.id, "Выберете карту:", reply_markup=markup)
        final_state = 60     
        save_fs(final_state) 
        
    elif final_state == 60:               # 1 карта 
        kb = read_kb()
        taro_cards = read_taro()          # Читаем колоду
        i = -1                            # Поиск выбранной буквы
        num_del = -1
        for elem in kb:
            i += 1
            if elem == message.text:
                num_del = i
        kb[num_del] = chr(1)               # Клавиша деактивирована
        save_kb(kb)                        # Запоминаем обновленную клавиатуру
                                           # Создаем пустое изображение
        background = Image.new('RGBA', (450, 780), (255, 255, 255, 255))
        if final_state_3 == 10:            # Крест
            photo = "rwsun.jpg"
            image_generator_cross(background, photo, 0, 0, 0)
        elif final_state_3 == 20:          # План
            photo = "rwsun.jpg"
            image_generator_plan(background, photo, 0, 0, 0, 0)
        hi = prediction(taro_cards, final_state_2, final_state_3, 1) 
        tb.reply_to(message, hi)           # Выводим значение 1-й карты 
        photo = open('out.png', 'rb')      # Вывод карты
        tb.send_photo(message.chat.id, photo)   
        markup = generate_markup(kb)
        tb.send_message(message.chat.id, "Выберете карту:", 
                        reply_markup=markup)
        final_state = 70     
        save_fs(final_state) 
        
    elif final_state == 70:                # 2 карта 
        kb = read_kb()
        taro_cards = read_taro()          # Читаем колоду
        i = -1                             # Поиск выбранной буквы
        num_del = -1
        for elem in kb:
            i += 1
            if elem == message.text:
                num_del = i
        kb[num_del] = chr(1)               # Клавиша деактивирована
        save_kb(kb)                        # Запоминаем обновленную клавиатуру
                                           # Создаем пустое изображение
        background = Image.new('RGBA', (450, 780), (255, 255, 255, 255))
        if final_state_3 == 10:            # Крест
            photo = "rwsun.jpg"
            image_generator_cross(background, photo, photo, 0, 0)
        elif final_state_3 == 20:          # План
            photo = "rwsun.jpg"
            image_generator_plan(background, photo, photo, 0, 0, 0)
        hi = prediction(taro_cards, final_state_2, final_state_3, 2) 
        tb.reply_to(message, hi)           # Выводим значение 1-й карты 
        photo = open('out.png', 'rb')      # Вывод карты
        tb.send_photo(message.chat.id, photo)            
        markup = generate_markup(kb)        
        tb.send_message(message.chat.id, "Выберете карту:", 
                        reply_markup=markup)
        final_state = 80     
        save_fs(final_state) 
        
    elif final_state == 80:               # 3 карта 
        kb = read_kb()
        taro_cards = read_taro()          # Читаем колоду
        i = -1                            # Поиск выбранной буквы
        num_del = -1
        for elem in kb:
            i += 1
            if elem == message.text:
                num_del = i
        kb[num_del] = chr(1)               # Клавиша деактивирована
        save_kb(kb)                        # Запоминаем обновленную клавиатуру
                                           # Создаем пустое изображение
        background = Image.new('RGBA', (450, 780), (255, 255, 255, 255))
        if final_state_3 == 10:            # Крест
            photo = "rwsun.jpg"
            image_generator_cross(background, photo, photo, photo, 0)
        elif final_state_3 == 20:          # План
            photo = "rwsun.jpg"
            image_generator_plan(background, photo, photo, photo, 0, 0)
        hi = prediction(taro_cards, final_state_2, final_state_3, 3) 
        tb.reply_to(message, hi)           # Выводим значение 1-й карты 
        photo = open('out.png', 'rb')      # Вывод карты
        tb.send_photo(message.chat.id, photo)
        markup = generate_markup(kb)          
        tb.send_message(message.chat.id, "Выберете карту:", 
                        reply_markup=markup)
        final_state = 90     
        save_fs(final_state)   
        
    elif final_state == 90:               # 4 карта 
        background = Image.new('RGBA', (450, 780), (255, 255, 255, 255))
        taro_cards = read_taro()          # Читаем колоду
        hi = prediction(taro_cards, final_state_2, final_state_3, 4) 
        tb.reply_to(message, hi)           # Выводим значение 1-й карты 
        if final_state_3 == 10:            # Крест
            photo = "rwsun.jpg"
            image_generator_cross(background, photo, photo, photo, photo)
            photo = open('out.png', 'rb')      # Вывод карты
            tb.send_photo(message.chat.id, photo)
        elif final_state_3 == 20:          # План
            photo = "rwsun.jpg"
            image_generator_plan(background, photo, photo, photo, photo, 0)
            photo = open('out.png', 'rb')      # Вывод карты
            tb.send_photo(message.chat.id, photo)
            kb = read_kb()
            i = -1                         # Поиск выбранной буквы
            num_del = -1
            for elem in kb:
                i += 1
                if elem == message.text:
                    num_del = i
            kb[num_del] = chr(1)           # Клавиша деактивирована
            save_kb(kb)                    # Запоминаем обновленную клавиатуру
            markup = generate_markup(kb)          
            tb.send_message(message.chat.id, "Выберете карту:", 
                            reply_markup=markup)
        final_state = 100     
        save_fs(final_state)   
        
    elif final_state == 100:               # 5 карта 
        background = Image.new('RGBA', (450, 780), (255, 255, 255, 255))
        taro_cards = read_taro()          # Читаем колоду
        if final_state_3 == 10:            # Крест
            hi = "Пока все!:)"
            tb.reply_to(message, hi) 
        elif final_state_3 == 20:          # План
            hi = prediction(taro_cards, final_state_2, final_state_3, 5) 
            tb.reply_to(message, hi)       # Выводим значение 1-й карты 
            photo = "rwsun.jpg"
            image_generator_plan(background, photo, photo, photo, photo, photo)
        photo = open('out.png', 'rb')      # Вывод карты
        tb.send_photo(message.chat.id, photo)

        
        
@tb.message_handler(commands=["help"])
def send_welcome(message):
    tb.reply_to(message, "Описантие программы")



if __name__ == '__main__':
     tb.polling(none_stop=True)
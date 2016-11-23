#!/usr/bin/python3
# -*- coding: utf-8 -*- 

# @my_homework_bot v.1.0

# Ставим библиотеки
# sudo pip install pyTelegramBotAPI
# sudo pip install -U requests    # обновляем requests

import telebot
from telebot import types
import time

TOKEN = '291727399:AAGLAbS88bfeUzmrXZM7dzptNiOBro2pBW0'

# Запускаем ботика
bot = telebot.TeleBot(TOKEN)

# Команда '/start'.
@bot.message_handler(commands=["start"])
def send_welcome(message):
    
# Запоминаем конечное состояние
    f_s = '0'
# Записываем в файл
    file = open("tmp_f_s.txt", "w")    # пишем в файл "tmp_f_s.txt"
    file.write(f_s)
    file.close()

# Приветствие
    hi = 'Привет! Меня зовут @my_homework_bot v.1.0. Я буду выполнять домашние задания'  
# Печатаем приветствие и уберем клавиатуру перед началом
    markup = types.ReplyKeyboardHide()
    bot.send_message(message.chat.id, hi, reply_markup = markup)
    time.sleep(2) 
 
# Рисуем клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, \
                                       one_time_keyboard = True)
    hi_1 = "Поехали!"
    hi_2 = 'Задание # 1' 
    keyboad = types.KeyboardButton(hi_2)
    markup.row(keyboad)
    bot.send_message(message.chat.id, hi_1, reply_markup = markup)


# Обработка входного текста  

@bot.message_handler(func = lambda message: True, content_types = ['text'])
def get_messages(message):

    file = open("tmp_f_s.txt", "r")    
    f_s = file.read()               # считываем конечное состояние
    
#---------- final state = 0 ----------------------------------------------------

    if message.text == 'Задание # 1' and f_s == '0':
# Дана приезда
        hi = "Я помогу спланировать тебе твою поездку" + '\n' + '\n' + \
             "Введи дату приезда (в формате целого числа)"
        bot.send_message(message.chat.id, hi)
# Запоминаем конечное состояние
        f_s = '10'
# Записываем в файл
        file = open("tmp_f_s.txt", "w")    # пишем в файл "tmp_f_s.txt"
        file.write(f_s)
        file.close()

#---------- final state = 10 ----/дата приезда/---------------------------------

    elif f_s == '10': 
# Проверяем число или нет
        try: 
            int(message.text)
        except ValueError as e:
            hi = "Необходимо вводить целое число"
            bot.send_message(message.chat.id, hi)
# Конечное состояние остается прежним
            f_s = '10'
        else:    
# Запоминаем конечное состояние
            f_s = '20'
# Записываем в файл
            file = open("tmp_f_s.txt", "w")     # пишем в файл "tmp_f_s.txt"
            file.write(f_s)
            file.close()
# Записываем дату приезда
            file = open("tmp_info.txt", "w")    # пишем в файл "tmp_info.txt"
            file.write(str(message.text))
            file.close()           
# Дата отъезда
            hi = "Введи дату отъезда (в формате целого числа)"
            bot.send_message(message.chat.id, hi)

#---------- final state = 20 ----/дата отъезда/---------------------------------

    elif f_s == '20':
# Проверяем число или нет
        try: 
            int(message.text)
        except ValueError as e:
            hi = "Необходимо вводить целое число"
            bot.send_message(message.chat.id, hi)
# Конечное состояние остается прежним
            f_s = '20'
        else:  
# Читаем дату приезда
            file = open("tmp_info.txt", "r")  
            arrival_date = file.read()              
            file.close()   
            if int(message.text) < int(arrival_date):         
                hi_1 = "День отъезда должен быть больше дня приезда"
                hi_2 = ' Введи новую дату отъезда)'
                hi = hi_1 + hi_2
# Конечное состояние остается прежним
                f_s = '20'
            else:
# Подсчет количества дней
                days_es = int(message.text) - int(arrival_date) + 1            
                if days_es <= 90:
                    hi_1 = 'Пребывание в ES на ' + str(days_es) + ' дней разрешено!'
                    hi_2 = ' Каким бюджетом поездки ты располагаешь /руб/ ?'
                    hi = hi_1 + hi_2
                    f_s = '30'
# Записываем всео дней в es
                    file = open("tmp_info.txt", "w")    # пишем в файл "tmp_info.txt"
                    file.write(str(days_es))
                    file.close()  
                else:
                    hi_1 = 'Пичалька:=)! Пребывание в ES на ' + str(days_es) + ' дней ЗАПРОЕЩЕНО!'
                    hi_2 = ' Введи новую дату отъезда)'
                    hi = hi_1 + hi_2
# Конечное сочтояние остается прежним
                    f_s = '20'
            bot.send_message(message.chat.id, hi)                         
# Записываем в файл конечное состояние
            file = open("tmp_f_s.txt", "w")     # пишем в файл "tmp_f_s.txt"
            file.write(f_s)
            file.close()

#---------- final state = 30 ---------------------------------------------------

    elif f_s == '30':
# Проверяем число или нет
        try: 
            int(message.text)
        except ValueError as e:
            hi = "Необходимо вводить целое число"
            bot.send_message(message.chat.id, hi)
# Конечное сочтояние остается прежним
            f_s = '30'
        else:
# Курс евро 
            course_euro = 70 
            hi = 'Курс евро считаем ' + str(course_euro) + ' руб'
            bot.send_message(message.chat.id, hi)
# Подсчет необходимого бюджета
            file = open("tmp_info.txt", "r")  
            days_es = file.read()           
            file.close()   
            budget = int(message.text)
            min_budget = 50 * course_euro * int(days_es)
            hi = 'Для получения визы необходимо иметь ' + str(min_budget) + ' руб'
            bot.send_message(message.chat.id, hi)
            hi = 'Из расчета не менее 50 евро в день'
            bot.send_message(message.chat.id, hi)
            if min_budget > budget:
                hi = 'Эх-х-х-х! А на визу то не хватает...'
                time.sleep(2) 
                bot.send_message(message.chat.id, hi) 
                hi = 'Давай заново'
                bot.send_message(message.chat.id, hi)   
# Меняем дату отъезда
                hi = "Введи более ранюю дату отъезда (в формате целого числа)"
                bot.send_message(message.chat.id, hi)             
# Записываем в файл конечное состояние
                f_s = '0'
                file = open("tmp_f_s.txt", "w")     # пишем в файл "tmp_f_s.txt"
                file.write(f_s)
                file.close()   
# Рисуем клавиатуру
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True, \
                                       one_time_keyboard = True)
                hi_1 = "Поехали!"
                hi_2 = 'Задание # 1' 
                keyboad = types.KeyboardButton(hi_2)
                markup.row(keyboad)
                bot.send_message(message.chat.id, hi_1, reply_markup = markup)
                  
            else:
                time.sleep(2) 
                hi = 'Ура! Ты получишь визу и можешь ехать'
                bot.send_message(message.chat.id, hi)   
                
# Про циклы      
                time.sleep(3) 
                hi = 'Кстати, по поводу цикла... Это когда как=то так'
                bot.send_message(message.chat.id, hi)   
                for i in range(7):
                    if i % 2 == 0:
                        hi = '+     ++++++++++'
                        bot.send_message(message.chat.id, hi)   
                        time.sleep(1) 
                    if i % 2 != 0:
                        hi = '++++++++++     +'
                        bot.send_message(message.chat.id, hi)   
                        time.sleep(1) 
                        
                hi = 'Вот и все:=)'
                bot.send_message(message.chat.id, hi)          

# Мои вопросы      
                time.sleep(1) 
                hi = 'А сейчас мой вопрос)'
                bot.send_message(message.chat.id, hi)   
                hi = 'Как можно сохранять перемнные без записи их в файл?'
                bot.send_message(message.chat.id, hi)             
                hi = 'Даже если я их оюъявляю глобальными они при каждом новом выхове хэндлера пропадают  '
                bot.send_message(message.chat.id, hi) 

# Запуск через polling
if __name__ == '__main__':
    bot.polling(none_stop = True, interval = 0, timeout = 3)







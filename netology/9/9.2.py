#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import glob
import os
import os.path
import codecs

# Определяем где мы находимся
PATH = os.getcwd()

print('Из какой папки будем парсить файлы?')
print('1 - Migrations 2 - Advanced Migrations')

while True:
    var = input()
    if  var == '1':
# Переходим в папку Migrations
        os.chdir(PATH + '/Migrations')
        break
    elif var == '2':
        os.chdir(PATH + '/Advanced Migrations')
        break
    else:
        False
        print('необходимо ввести 1 или 2')

# Сохраняем имена всех .sql файлов
sql_files = glob.glob('*.sql')
print('Всего найдено %s .sql файлов' % len(sql_files))

files = []
while True:
    print('Рассматриваем %s файллов' % len(sql_files))
    print('введите запрос для парсинга')
    user_input = str(input())
# INSERT
# APPLICATION_SETUP 
# A400M
# 0.0
# 2.0
    for file in sql_files:
        print('Рассматриваем файл', file) 
        try:        
            file_encoding = 'utf-8'
            with codecs.open(file, encoding = file_encoding) as new_file:
                info = new_file.read()
        except:
            file_encoding = 'koi8-r'
            with codecs.open(file, encoding = file_encoding) as new_file:
                info = new_file.read()
        if info.find(user_input) > 0:
            files.append(file)
            print('В файле %s подстрока %s найдена' % (file, user_input)) 
        else:
            print('В файле %s подстрока %s не найдена' % (file, user_input))                 
    print('В %s файлах содержится подстрока %s' % (len(files), user_input))
    
    files, sql_files = [], files
    

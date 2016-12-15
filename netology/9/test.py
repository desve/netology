from urllib import request
import re

# Путь к папке в файлами
PATH = 'https://github.com/jmistx/Python_course/tree/master/Lesson_2.4/homework/Migrations/'
# Парсим
html = request.urlopen(PATH).read().decode('utf-8')

# Выбираем имена всех файлов
file_names = re.findall('/Migrations/(.*)" class="js-navigation-open' , html)
"""
for file in file_names:
    print(file)
"""    
# Выбираем из найденных файлов только .sql
# file_names = re.findall("[a-zA-Z0-9-_.%&#;]+\.(?:sql)", str(file_names))
file_names = re.findall('*.sql', str(file_names))



for file in file_names:
    print(file)
"""
sql_files = len(file_names)
print('Всего найдено %i .sql файлов' % sql_files)

# user_request = str(input)
user_request = 'INSERT'

# Парсим .sql файлы 
for file in file_names:
    path_file = PATH + file
    print(path_file)
    html = request.urlopen(path_file).read().decode('utf-8')
    print('В файле %s запрос встречается %s раз' % (file, html.count(user_request)))
    # оставляем только файлы с нужным запросом
    file_names = filter(lambda x:  html.count(user_request) > 0, file_names)
  

print('Итого осталось %i файлов из %i' % len(file_names, sql_files))


>>> fib = [0,1,1,2,3,5,8,13,21,34,55]
>>> result = filter(lambda x: x % 2, fib)

# Оставляем только те файлы в которых данный запрос встречается более 1-го раза
file_names = filter(lambda x:  html.count(user_request) > 0, file_names)
"""

from urllib import request
import re

print('Из какой папки будем парсить файлы?')
print('1 - Migrations 2 - Advanced Migrations')
while True:
    var = input()
    if  var == '1':
        PATH = 'https://github.com/jmistx/Python_course/tree/master/Lesson_2.4/homework/Migrations/'   
        break
    elif var == '2':
        PATH = 'https://github.com/jmistx/Python_course/tree/master/Lesson_2.4/homework/Advanced%20Migrations/'
        break
    else:
        print('необходимо ввести 1 или 2')
print('Парсим .sql файлы из папки ', PATH)

# Парсим
html = request.urlopen(PATH).read().decode('utf-8')

# Выбираем имена всех файлов
file_names = re.findall('/Migrations/(.*)" class="js-navigation-open' , html)

numder_files = len(file_names)
print('Всего найдено файлов', numder_files)

# Выбираем из найденных файлов только .sql             
file_names = list(filter(lambda file_names: file_names.rfind('.sql',
                         len(file_names)-4, len(file_names)) > 0, 
                         file_names))                   
numder_sql_files = len(file_names)                             
print('Из них  %s .sql файлов' % numder_sql_files)

sql_files = []
while True:
    print('введите запрос для парсинга')
    user_input = str(input())
    for i in range(50):
        file = file_names[i]
        path_file = PATH + file
#    print(i, path_file)
        try:
            sql_file = request.urlopen(path_file).read().decode('utf-8')
            if sql_file.find(user_input) > 0:
                print('в файле %s запрос %s найден' % (file, user_input))
                sql_files.append(file)
        except:
            print('файл %s не удается обработать' % file)
        
    print('%s файлов отвечают заданному запросу' % len(sql_files))
# Сохраняем новый вписок файлов обратно в file_names
    sql_files, file_names = [], sql_files

       
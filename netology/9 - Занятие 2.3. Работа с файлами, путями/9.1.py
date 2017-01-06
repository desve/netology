from urllib import request
import re

# Путь к папке в файлами
PATH = 'https://github.com/jmistx/Python_course/tree/master/Lesson_2.4/homework/Migrations/'
# Парсим
html = request.urlopen(PATH).read().decode('utf-8')

# Выбираем имена всех файлов
file_names = re.findall('/Migrations/(.*)" class="js-navigation-open' , html)

numder_files = len(file_names)
print('Всего найдено файлов', numder_files)
#for file in file_names:
#    print(file)
  
# Выбираем из найденных файлов только .sql
                  
file_names = list(filter(lambda file_names: file_names.rfind('.sql',
                         len(file_names)-4, len(file_names)) > 0, 
                         file_names))                   

sql_files = len(file_names)                             
print('Остается %s .sql файлов'% sql_files)
#for file in file_names:
#    print(file)

user_input = 'INSERT'
i = 0
for file in file_names:
    i += 1
    path_file = PATH + file
    print(i, path_file)
    try:
        sql_file = request.urlopen(path_file).read().decode('utf-8')
#        print(sql_file.count(user_input))
    except:
        print('файл %s не удается обработать' % file)


"""
#    if sql_file.find(user_input) > 0:
#        print('В файле %s подстрока %s найдена' % (file, user_input))
#        file_names = list(filter(lambda file_names: file_names.rfind('.sql',
#                         len(file_names)-4, len(file_names)) > 0, 
#                         file_names))    
"""


# ttps://github.com/jmistx/Python_course/tree/master/Lesson_2.4/homework/Migrations/20091127_4703479_A380_PDCR_suppression%20d&#39;une%20PDDS.sql

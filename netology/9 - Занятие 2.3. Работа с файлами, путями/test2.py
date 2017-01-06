from urllib import request
import re

# Путь к папке в файлами
PATH = 'https://github.com/jmistx/Python_course/tree/master/Lesson_2.4/homework/Advanced%20Migrations/'
# Парсим
html = request.urlopen(PATH).read().decode('utf-8')
print(html)

# Выбираем имена всех файлов
file_names = re.findall('/Advanced%20Migrations/(.*)" class="js-navigation-open' , html)

numder_files = len(file_names)
print('Всего найдено файлов', numder_files)
for file in file_names:
    print(file)
  
# Выбираем из найденных файлов только .sql
                  
file_names = list(filter(lambda file_names: file_names.rfind('.sql',
                         len(file_names)-4, len(file_names)) > 0, 
                         file_names))                   

sql_files = len(file_names)                             
print('Остается %s .sql файлов'% sql_files)
#for file in file_names:
#    print(file)

"""
user_input = 'INSERT'
for file in file_names:
    path_file = PATH + file
    print(path_file)
    sql_file = request.urlopen(path_file).read().decode('utf-8')
    num_user_input = sql_file.count(user_input)
    print('В файле %s совпадений %s' % (file, num_user_input))
"""



       

    
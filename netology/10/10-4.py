# sudo apt-get update
# sudo apt-get install imagemagick

# Занятие 2.4. Вызов внешних программ

def file_convert(file):
    global PATH
# Извлекаем файлы и обрабатываем их
    file_path_output = os.path.join(PATH, 'Result', file)
    command = 'convert ' + file + ' -resize 200 ' + file_path_output
    go = subprocess.call(command, shell = True)

def benchmark(func):
# Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        result = func(*args, **kwargs)
        print('Функция %s время выполнения %s' % (func.__name__, time.clock() - t))
        return result
    return wrapper

import subprocess
import os
import os.path
import glob

# Определяем наше местоположение на диске
global PATH
PATH = os.getcwd()

# Определяем откуда брать файлы
file_path_input = os.path.join(PATH, 'Source')

# Переходим к папке с исходными фото 
os.chdir(file_path_input)

# Создаем список, имеющихся там файлов
files = glob.glob('*.jpg')

# Создаем деректорию для обработанных фото
try:
    os.mkdir(os.path.join(PATH, 'Result'))
except FileExistsError:
    pass

@benchmark   
def files_convert_1(files):
# Обычный вызов подпрограммы
    for file in files:
        file_convert(file)

@benchmark         
def files_convert_2(files):
# Попытка организации параллейных процессов
    from multiprocessing import Pool
    if __name__ == '__main__':
        with Pool(4) as p:
            p.map(file_convert, files)
            
@benchmark         
def files_convert_3(files):
# Попытка организации параллейных процессов # 2
    import subprocess
    global PATH
    for file in files:
# Извлекаем файлы и обрабатываем их
        file_path_output = os.path.join(PATH, 'Result', file)
        command = 'convert ' + file + ' -resize 200 ' + file_path_output
        p = subprocess.Popen(command, shell = True)

@benchmark         
def files_convert_4(files):
    # Попытка организации параллейных процессов # 2
    import subprocess
    global PATH
    subprocess_list = []
    for file in files:
# Задаем путь для записи файла
        file_path_output = os.path.join(PATH, 'Result', file)
# Задаем команду
        command = 'convert {} -resize 200 {}'.format(file, file_path_output)
# Задаем аргументы
        argument = '{}, shell = True'.format(command)
# Задаем и добавляем субпроцесс
        subprocess_list.append('p = subprocess.Popen({})'.format(argument))
# Запускаем субпроцессы    
    for sub_process in subprocess_list:
        sub_process

# Обычный вызов подпрограммы
files_convert_1(files)

# Попытка организации параллейных процессов
files_convert_2(files)

# Попытка организации параллейных процессов # 2
files_convert_3(files) 

# Попытка организации параллейных процессов # 3 
files_convert_4(files)
        
print('Задание выполнено')


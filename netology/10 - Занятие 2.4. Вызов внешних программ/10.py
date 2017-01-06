# sudo apt-get update
# sudo apt-get install imagemagick

import subprocess
import os
import os.path
import glob

# Определяем наше местоположение на диске
import subprocess
import os
import os.path
import glob
from multiprocessing import Pool

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
os.mkdir(os.path.join(PATH, 'Result'))

def file_convert(file):
    global PATH
# Извлекаем файлы и обрабатываем их
    file_path_output = os.path.join(PATH, 'Result', file)
    command = 'convert ' + file + ' -resize 200 ' + file_path_output
    go = subprocess.call(command, shell = True)

"""  
# Обычный вызов подпрограммы
for file in files:
    file_convert(file)
""" 
 
# Попытка организации параллейных процессов
if __name__ == '__main__':
    with Pool(4) as p:
        p.map(file_convert, files)





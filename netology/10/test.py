import subprocess
import os
import os.path
import glob

# Определяем наше местоположение на диске
PATH = os.getcwd()
print(PATH)

# Определяем откуда брать файлы
file_path_input = os.path.join(PATH, 'Source')
# Переходим к папке с исходными фото 
os.chdir(file_path_input)
# Создаем список, имеющихся там файлов
files = glob.glob('*.jpg')

# Создаем деректорию для обработанных фото
os.mkdir(os.path.join(PATH, 'Result'))

# Извлекаем файлы и обрабатываем их
for file in files:
    file_path_output = os.path.join(PATH, 'Result', file)
    command = 'convert ' + file + ' -resize 200 ' + file_path_output
    go = subprocess.call(command, shell=True)

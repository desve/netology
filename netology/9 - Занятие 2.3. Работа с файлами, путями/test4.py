import codecs
import glob
import os
import os.path


file_encoding = {'1': 'utf-8', '2': 'utf-8', '3': 'koi8-r', 
                 '4': 'koi8-r', '5': 'ISO-8859-5', '6': 'ISO-8859-5',
                 '7': 'windows-1251', '8': 'windows-1251', 'e': ''}

PATH = os.getcwd()
os.chdir(PATH + '/Advanced Migrations')

file = '06_A400_Edit_WDDS.sql'


print('Рассматриваем файл', file) 
file_encoding = 'koi8-r'

try:        
    file_encoding = 'utf-8'
    with codecs.open(file, encoding = file_encoding) as new_file:
        info = new_file.read()
        print(info)
except:
    file_encoding = 'koi8-r'
    with codecs.open(file, encoding = file_encoding) as new_file:
        info = new_file.read()
        print(info)

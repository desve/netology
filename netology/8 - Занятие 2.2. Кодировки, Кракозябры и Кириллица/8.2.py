#!/usr/bin/python3
# -*- coding: utf-8 -*- 

# Занятие 2.2. Кодировки, Кракозябры и Кириллица

def input_json_1(file_name, file_encoding):    
# Парсинг .json
    import codecs
    import json
    import re
    import collections
    
    print('Для файла %s выбрана кодировка %s' % (file_name, file_encoding))
    with codecs.open(file_name, encoding = file_encoding) as news:
        info = json.load(news)

    words = []
    number_news = len(info['rss']['channel']['item'])
    for i in range(number_news):  
#
# По условиям задачи текст берем из "текса новостей"
# т.е. из info['rss']['channel']['item'][i]['description']['__cdata']
# аналогично можно брать и из info['rss']['channel']['item'][i]['title']['__cdata']
#
        text = info['rss']['channel']['item'][i]['description']['__cdata']
# Оставляем только текст
        result = re.findall(r'[а-я,А-Я]\w+', text)    
# Удаляем слова меньше 6 букв    
        result = list(filter(lambda x: len(x) > 6, result))    
# Добавляем новые слова в список
        words.extend(result)   
# Ищем pot-10 слов
    top_words = collections.Counter(words).most_common(10)    # Очень замечательная функция!
    print(top_words)
    return True
    
def input_xml(file_name, file_encoding):   
# Парсинг .xml
    import xml.etree.ElementTree as ET
    import codecs
    import re
    import collections

    print('Для файла %s выбрана кодировка %s' % (file_name, file_encoding))
    with codecs.open(file_name, encoding = file_encoding) as news:
        content = news.read()
        tree = ET.fromstring(content)

    words = []
    for info in tree.iter('description'):
        text = info.text
# Оставляем только текст        
        result = re.findall(r'[а-я,А-Я]\w+', text)    
# Удаляем слова меньше 6 букв    
        result = list(filter(lambda x: len(x) > 6, result))    
# Добавляем новые слова в список
        words.extend(result)   
# Ищем pot-10 слов
    top_words = collections.Counter(words).most_common(10)
    print(top_words)
    return True

def input_json_2(file_name, file_encoding):  
# Парсинг .json
    import codecs
    import json
    import re
    import collections

    print('Для файла %s выбрана кодировка %s' % (file_name, file_encoding))
    with codecs.open(file_name, encoding = file_encoding) as news:
        info = json.load(news)

    words = []
    number_news = len(info['rss']['channel']['item'])
    for i in range(number_news):  
#
# По условиям задачи текст берем из "текса новостей"
# т.е. из info['rss']['channel']['item'][i]['description']
# аналогично можно брать и из info['rss']['channel']['item'][i]['title']
#
        text = info['rss']['channel']['item'][i]['description']
# Оставляем только текст
        result = re.findall(r'[а-я,А-Я]\w+', text)    
# Удаляем слова меньше 6 букв    
        result = list(filter(lambda x: len(x) > 6, result))    
# Добавляем новые слова в список
        words.extend(result)   
# Ищем pot-10 слов
    top_words = collections.Counter(words).most_common(10)
    print(top_words)
    return True

def input_e(file_name, file_encoding):
# Выход из цикла
    print('Конец работы')
    return False
    
def input_error(file_name, file_encoding):
# Ввод не предусмотренного символа
    print("введите - '1', '2', '3', '4', '5', '6', '7', '8',или 'e'")
    return True

print('Привет! Какой файл будем открывать?')
print('1 - newsafr.json')
print('2 - newsafr.xml')
print('3 - newscy.json')
print('4 - newscy.xml')
print('5 - newsfr.json')
print('6 - newsfr.xml')
print('7 - newsit.json')
print('8 - newsit.xml')
print('e - Exit')

while True:
# Выбираем файл для парсинга
    user_input = input()
   
# Словарь вызываемых функций
    functions_input = {'1': input_json_1, '2': input_xml, '3': input_json_1, 
                       '4': input_xml, '5': input_json_1, '6': input_xml, 
                       '7': input_json_2, '8': input_xml, 'e': input_e}

# Словарь передаваемых файлов                     
    file_input = {'1': 'newsafr.json', '2': 'newsafr.xml', '3': 'newscy.json', 
                  '4': 'newscy.xml', '5': 'newsfr.json', '6': 'newsfr.xml', 
                  '7': 'newsit.json', '8': 'newsit.xml', 'e': ''}
                  
# Словарь кодировок файлов
    file_encoding = {'1': 'utf-8', '2': 'utf-8', '3': 'koi8-r', 
                     '4': 'koi8-r', '5': 'ISO-8859-5', '6': 'ISO-8859-5',
                     '7': 'windows-1251', '8': 'windows-1251', 'e': ''}
                       
    file_name = file_input.get(user_input, None)      
    file_encoding = file_encoding.get(user_input)  
    functions_input.get(user_input, input_error)(file_name, file_encoding) 
    
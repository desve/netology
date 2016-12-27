#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# Список стран из домашнего задания

def input_j(info):
# Записываем в формат .json
    import json
# Вариант 1 (Красивый)
    file_name = 'json_v_1.json'
    info_json = json.dumps(info, sort_keys = True, indent = 4)
    with open(file_name, 'w') as file:
         file.write(info_json)   
# Вариант 2 (Компактный)
    file_name = 'json_v_2.json'
    info_json = json.dumps(info, separators=(',', ':'))
    with open(file_name, 'w') as file:
         file.write(info_json)           
    return True

def input_y(info):
# Записываем в формат .yaml
    import yaml
    info_yaml = yaml.dump(info)
# Пишем в файл yaml.yaml   
    file_name = 'yaml.yaml'
    with open(file_name, 'w') as file:
         file.write(info_yaml)    
    return True
    
def input_c(info):
# Записываем в формат .csv
    import csv
# Вариант 1
    file_name = 'csv_v_1.csv'
    with open(file_name, 'w') as file:
        row = csv.DictWriter(file, info.keys())
        row.writeheader()
        row.writerow(info)
# Вариант 2        
    file_name = 'csv_v_2.csv'
    with open(file_name, 'w') as file:
        for key in info:
            file.write(key + '\n')
            row = csv.DictWriter(file, info[key].keys())
            row.writeheader()
            row.writerow(info[key])

    return True
    
def input_x(info):
# Записываем в формат .xml
    import dicttoxml                                 # pip install dicttoxml
    from xml.dom.minidom import parseString
# Вариант 1 (Бинарный)
    file_name = 'xml_v_1.xml'
    xml = dicttoxml.dicttoxml(countries)
    with open(file_name, 'wb') as file:
         file.write(xml)   
# Вариант 2 (Красивый)
    file_name = 'xml_v_2.xml'
    dom = parseString(xml)
    with open(file_name, 'w') as file:
         file.write(dom.toprettyxml())           
    return True
    
def input_e(info):
# Выход из цикла
    print('Конец работы')
    return False
    
def input_error(info):
# Ввод не предусмотренного символа
    print("введите одну из букв - 'j', 'y', 'c', 'x' или 'e'")
    return True

print('Итак, мы имеем словарь стран. В каком формате его сохранить?')
print('j - .json')
print('y - .yaml')
print('c - .csv')
print('x - .xml')
print('e - Exit')

# Самый простой способ чтения словаря
from countries import countries

while True:
# Выбираем режим
    user_input = input()
    functions_input = {'j': input_j, 'y': input_y, 'c': input_c, 'x': input_x,
                       'e': input_e}
    functions_input.get(user_input, input_error)(countries) 
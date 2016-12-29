#!/usr/bin/python3
# -*- coding: utf-8 -*- 

def input_json():
# Считываем словарь из json.json
    import json
    file_name = 'json.json'
    with open(file_name) as file:
        countries = json.load(file)
    return countries
    
def input_yaml():
# Считываем словарь из yaml.yaml
    import yaml
    file_name = 'yaml.yaml'
    with open(file_name) as file:
        countries = yaml.load(file, Loader = yaml.Loader)
    return countries
    
def input_csv():
# Считываем словарь из csv.csv
    import csv
    file_name = 'csv.csv'
# Считаем количество строк в файле  
    with open(file_name) as file:
        lines = file.read().count('\n')     
    with open(file_name) as file:
        countries = {}
        for line in range(0, lines, 3):       # ситываем по 3 строки из файла
            line_1 = file.readline()
            countriy = line_1[:-1].split(',')
            line_2 = file.readline()
            keys = line_2[:-1].split(',')
            line_3 = file.readline()
            info = line_3[:-1].split(',')
            country_info = dict(zip(keys, info))
            countries[str(countriy[0])] = country_info   
    return countries
    
def input_xml():
# Считываем словарь из xml.xml
    import xml.etree.ElementTree as ET
    file_name = 'xml.xml'
    tree = ET.parse(file_name)
    root = tree.getroot() 
    countries = {}
    for countriy in root:
        number_keys = len(countriy) 
        keys = []
        info = []
        for key in range(number_keys):
            keys.append(countriy[key].tag)
            info.append(countriy[key].text)
            countriy_info = dict(zip(keys, info))
            countries[countriy.tag] = countriy_info    
    return countries   
    
def input_j():
# Считываем словарь
    info =  input_json()
# Записываем в формат .json
    import json
# Вариант 1 (Красивый)
    file_name = 'output.json'
    info_json = json.dumps(info, sort_keys = True, indent = 4)
    with open(file_name, 'w') as file:
         file.write(info_json)   
    return True

def input_y():
# Считываем словарь
    info = input_yaml()
# Записываем в формат .yaml
    import yaml
    info_yaml = yaml.dump(info)
# Пишем в файл yaml.yaml   
    file_name = 'output.yaml'
    with open(file_name, 'w') as file:
         file.write(info_yaml)    
    return True
    
def input_c():
# Считываем словарь
    info = input_csv()
# Записываем в формат .csv
    import csv        
    file_name = 'output.csv'
    with open(file_name, 'w') as file:
        for key in info:
            file.write(key + '\n')
            row = csv.DictWriter(file, info[key].keys())
            row.writeheader()
            row.writerow(info[key])
    return True
    
def input_x():
# Считываем словарь
    info = input_xml()
# Записываем в формат .xml
    import dicttoxml                                 # pip install dicttoxml
    from xml.dom.minidom import parseString 
# Вариант 2 (Красивый)
    file_name = 'output.xml'
    xml = dicttoxml.dicttoxml(info)
    dom = parseString(xml)
    with open(file_name, 'w') as file:
         file.write(dom.toprettyxml())           
    return True
    
def input_e():
# Выход из цикла
    print('Конец работы')
    return False
    
def input_error():
# Ввод не предусмотренного символа
    print("введите одну из букв - 'j', 'y', 'c', 'x' или 'e'")
    return True

print('Итак, мы имеем словарь стран. В каком формате его сохранить?')
print('j - .json')
print('y - .yaml')
print('c - .csv')
print('x - .xml')
print('e - Exit')

while True:
# Выбираем режим
    user_input = input()
    functions_input = {'j': input_j, 'y': input_y, 'c': input_c, 'x': input_x,
                       'e': input_e}
    functions_input.get(user_input, input_error)()
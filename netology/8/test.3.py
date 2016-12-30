# -*- coding: utf-8 -*- 
def input_json(file_name):    
# Парсинг .json
    import codecs
    import json
#    import re
#    import collections
     
    encodings = {
        'UTF-8':      'utf-8',
        'CP1251':     'windows-1251',
        'KOI8-R':     'koi8-r',
        'IBM866':     'ibm866',
        'ISO-8859-5': 'iso-8859-5',
        'MAC':        'mac'
                }

    enc = encodings['CP1251']
    print(enc)
        
    try:
        with codecs.open(file_name, encoding = enc) as news:
            info = json.load(news)
            print('Выбираем кодировку ', enc)
            print(info)
    except:
        print('Кодировка %s не подходит' % enc)


file_name = 'newsit.json'        
input_json(file_name)
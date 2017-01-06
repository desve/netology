# Занятие 3.2. Работа с библиотекой requests, http запросы

import requests
import os
import glob

def translate_me(file_path_input, file_path_output, from_language, to_language):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """

    KEY = 'trnsl.1.1.20161216T160124Z.4a07c4b6a2f01566.ade260e6c684818698899fd08a9c15d72faca843'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

# Задаем направление перевода
    translation = from_language + '-' + to_language

# Читаем текст
    with open(file_path_input, 'r') as file:
        mytext = file.read()

    params = {
        'key': KEY,
        'text': mytext,
        'lang': translation,
    }

    response = requests.get(URL, params = params).json()
    new_text = ' '.join(response.get('text', []))

# Записываем текст
    with open(file_path_output, 'w') as file:
        file.write(new_text)

# Находим текущую директорию
PATH = os.getcwd()

# Создаем список файлов с именем из 2-х символов и расщмрениеи.txt
# находящихся в текущей директории
files = glob.glob('??.txt')

# Читаем файлы и записываем перевод
for file in files:

    from_language = file[:2]                            # язык с которого перевести
    to_language = 'RU'                                  # язык перевода (по умолчанию русский)
    file_input = from_language + '.txt'                 # файл с текстом
    file_output = 'out_' + from_language + '.txt'       # файл с переводом
    file_path_input = os.path.join(PATH, file_input)    # путь к файлу с текстом
    file_path_output = os.path.join(PATH, file_output)  # путь к файлу с результатом

    translate_me(file_path_input, file_path_output, from_language, to_language)
    print('Перевод %s - %s выполнен' % (from_language, to_language))

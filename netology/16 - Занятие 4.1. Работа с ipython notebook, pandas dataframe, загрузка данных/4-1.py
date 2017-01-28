# Занятие 4.1. Работа с ipython notebook, pandas dataframe, загрузка данных

import pandas as pd
import os

def input_years():
# Вводим года
    print('Введите сколько годов будет задано')
    number_years = int(input())
    years = []
    for number_year in range(number_years):
        print('Введите %s - год' % str(number_year+1))
        year = int(input())
        while year < 1880 or year > 2015:    # проверка
            print('Введите значение в интервале 1880- 2015')
            year = int(input())
        years.append(year)
    return years

def path_to_file(years):
# Находим пути к файлам
    global PATH
    file_path = []
    for year in years:
# Задаем путь к файлу с данными
        file_path.append(PATH + '/names/yob{}.txt'.format(year))
    return file_path

def common_frame(years):
# Строим общий фрейм данных
# Находим пути к нужным файлам
    file_path = path_to_file(years)
    for order, year in enumerate(years):
        if order == 0:
            frame_names = pd.read_csv(file_path[order], names=['Name', 'Gender', 'Count'])
        elif order > 0:
            names = pd.read_csv(file_path[order], names=['Name', 'Gender', 'Count'])
            frame_names = pd.merge(frame_names, names, on=['Name', 'Gender'])
    return frame_names

def count_top_3(years):
# Ищем top-3 популярных имен
# Строим общий фрейм имен
    frame_names = common_frame(years)
# Суммируем
    sum_columns = 0
    for order in range(len(years)):
        sum_columns += frame_names[frame_names.columns[2 + order]]
# Сортируем по колонке - сумма
    frame_names.insert(0, 'summa', sum_columns)
    frame_names = frame_names.sort_values(by = 'summa', ascending = False)
# Строим список имен
    top_3 = []
    for name in frame_names.Name:
        top_3.append(name)
    return top_3[:3]

def count_dynamics(years):
# Ищем динамику изменения количества имен за указанные года в разрезе полов
# Строим общий фрейм имен
    frame_names = common_frame(years)
    male = []
    female = []
    frame_names_male = frame_names[frame_names.Gender == 'M']
    frame_names_female = frame_names[frame_names.Gender == 'F']
    for order in range(len(years)):
        male.append(frame_names_male[frame_names_male.columns[order + 2]].sum())
        female.append(frame_names_female[frame_names_female.columns[order + 2]].sum())
# Строим словарь с динамикой
    dynamics = dict(M = male, F = female)
    return dynamics

# Получаем список годов
years = input_years()
print('Были введены года', years)

# Задаем путь к папке names. Считаем, что папка находится в текущей директории
global PATH
PATH = os.getcwd()

# Выводим top-3 популярных имен
print('Список популярных имен Top-3')
print(count_top_3(years))

# Выводим динамику изменения количества имен за указанные года в разрезе полов
print('Словарь динами иизменения количества имен за указанные года в разрезе полов')
print(count_dynamics(years))


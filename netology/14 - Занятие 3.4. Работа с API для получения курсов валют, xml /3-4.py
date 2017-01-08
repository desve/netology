#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Занятие 3.4. Работа с API для получения курсов валют, xml / soap

import osa
import os
import math

# Находим текущую директорию
PATH = os.getcwd()


# ---------- Задание 1 ----------
print('Задание 1')

# Определяем путь к файлу
file = 'temps.txt'
file_path = os.path.join(PATH, file)

# Читаем информацию из файла
temperature_F = []
with open(file_path, 'r') as file:
    info = file.read().split('\n')
for trip in info:
    temperature_F.append(trip.split(' '))

# Путь к сервису
URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'

# Считаем среднее значение температуры по Цельсию
summa_temperature = 0
for day, day_temperature in enumerate(temperature_F):
    client1 = osa.client.Client(URL)
    response = client1.service.ConvertTemp(Temperature = day_temperature[0],
                                           FromUnit = 'degreeFahrenheit',
                                           ToUnit = 'degreeCelsius')
    print('День %s температура F %s температура C %0.2f' % (day+1, day_temperature[0], response))
    summa_temperature += response
# выводим окончательное значение
print('Среднее значение температуры за %s дней составило %0.2f по Цельсию' %
      (len(temperature_F), summa_temperature/len(temperature_F)))


# ---------- Задание 2 ----------
print('\nЗадание 2')

# Определяем путь к файлу
file = 'currencies.txt'
file_path = os.path.join(PATH, file)

# Читаем информацию из файла
tickets = []
with open(file_path, 'r') as file:
    info = file.read().split('\n')
for trip in info:
    tickets.append(trip.split(' '))


# Путь к сервису
URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'

# Счиьаем общую сумму в рублях
summa_total = 0
for trip, ticket in enumerate(tickets):
    from_Currency = ticket[2]    # текущая валюта
    to_Currency = 'RUB'          # переводим все в рубли
    summa = int(ticket[1])       # сумма в текущей валюте
    if from_Currency == 'RUB':
        response = summa
    else:
        client2 = osa.client.Client(URL)
        response = client2.service.ConvertToNum(fromCurrency = from_Currency,
                                                toCurrency = to_Currency,
                                                amount = summa,
                                                rounding = False)
    print('Маршрут %s %s стоимость в %s - %s стоимрсть в рублях %s' %
         (trip+1, ticket[0], ticket[2], ticket[1], math.ceil(response)))   # округляем до целого чисда в больщую сторону
    summa_total += response

print('Общая сумма затрат на все поездки %s рублей' % math.ceil(summa_total))


# ---------- Задание 3 ----------
print('\nЗадание 3')

# Определяем путь к файлу
file = 'travel.txt'
file_path = os.path.join(PATH, file)

# Читаем информацию из файла
travel_mi = []
with open(file_path, 'r') as file:
    info = file.read().split('\n')
for way in info:
    travel_mi.append(way.split(' '))
# Преобразуем формат чисел (убираем ',')
for trip in travel_mi:
    trip[1] = trip[1].replace(',', '')

# Путь к сервису
URL = 'http://www.webservicex.net/length.asmx?WSDL'

# Считыаем суммарное расстояние пути в километрах
travel_total = 0
for way, travel in enumerate(travel_mi):

    Length_Value = float(travel[1])    # расстояние в милях
    client3 = osa.client.Client(URL)
    response = client3.service.ChangeLengthUnit(LengthValue = Length_Value,
                                                fromLengthUnit = 'Miles', toLengthUnit = 'Kilometers')
    print('Маршрут %s %s расстояние в %s - %s расстояние в километрах %0.2f' %
         (way+1, travel[0], travel[2], travel[1], response))   # округляем до целого чисда в больщую сторону
    travel_total += response

print('Общее расстояние %0.2f километров' % travel_total)

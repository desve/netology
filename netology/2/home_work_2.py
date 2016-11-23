#!/usr/bin/python3
# -*- coding: utf-8 -*- 

# Задание № 2

# Записываем конфигурацию поездок в файл config.py /в perl похоже не получится/

# Файл конфигурации для home_work_2
# Начало первой поезди в интервале 0 - 30 дней
INTERVAL_START = 20
# Продолжительность каждой поездки 0 - 20 дней
INTERVAL_IN_ES = 30
# Продолжительность между поездками 0 - 20 дней
INTERVAL_IN_RU = 30
# Количество поездок 0-10
INTERVAL_NUMBER_OF_TRIPS = 20
# В реальности вызываем эти данные через config.INTERVAL_...


from random import randrange

# В качестве дополнительной задачи будем генерировать все поездки и ошибки случайным образом
# Создаем календарь поездок

# Первый день поездки
start_day = randrange(1, INTERVAL_START)

end_day = 366

while end_day >= 365:
    calendar_trips = []
    number_of_trips = randrange(3, INTERVAL_NUMBER_OF_TRIPS)
    
    trips = range(number_of_trips) 

    current_day = start_day
    for trip in trips:
        in_es = randrange(1, INTERVAL_IN_ES)
        in_ru = randrange(1, INTERVAL_IN_RU)
        calendar_trips.append([current_day, current_day + in_es])
        current_day += in_es + in_ru

# Последний день поездки
    end_day = calendar_trips[number_of_trips-1][1]  

# Смотрим  даты поездок

print('У тебя в этом году %s поездок(-ки) в ES!' % number_of_trips)
print('Список', calendar_trips)
number_of_trip = 0
for trip in calendar_trips:
    number_of_trip += 1
    print('Поездка %s - с %s по %s' % (number_of_trip, trip[0], trip[1]))
    
# Добавляем случайные ошибки

# Ошибка в типе данны
def mistake_1():
    print('Генерируем ощибку в типе данных')
    mistake_date = randrange(start_day, end_day)
    number = randrange(len(calendar_trips))        # случайный номер в списке
    calendar_trips.insert(number, mistake_date)
    print('Новый список с ошибкой', calendar_trips)
    print('Порядковый номер ошибки в списке', number)
    
# Ошибка: дата приезда больше даты отъезда
def mistake_2():
    print('Генерируем ощибку: дата приезда больше даты отъезда')
    number = randrange(len(calendar_trips))        # случайный номер в списке
    calendar_trips[number][1], calendar_trips[number][0] = \
            calendar_trips[number][0], calendar_trips[number][1]    # меняем местами
    print('Новый список с ошибкой', calendar_trips)
    print('Порядковый номер ошибки в списке', number)
    
# Ошибка: наложение поездок
def mistake_3():
    print('Генерируем наложение поездок')
    if number_of_trips >= 2:
        number = randrange(len(calendar_trips) - 1)        # случайный номер в списке
        calendar_trips[number+1][0] = calendar_trips[number][1] - \
                randrange(calendar_trips[number][1] - calendar_trips[number][0])       
        print('Новый список с ошибкой', calendar_trips)
        print('Порядковый номер ошибки в списке', number+1)    
        
# Без ошибок
def no_mistake():
    print('Работа без ошибок')
  
# Вызаваем случайную ошибку
key_mistake = randrange(1, 5)
# При желании ее можно задать вручную
# key_mistake = 4
functions_mistake = {1: mistake_1, 2: mistake_2, 3: mistake_3, 4: no_mistake}
functions_mistake.get(key_mistake)()
  

    
# Обработка ошибок

# Ошибки в типе поездки
for visit in calendar_trips:
	if not isinstance(visit, list):
		raise Exception("Ошибка в типа поездки", visit)
		
# Ошибка: дата приезда больше даты отъезда
for visit in calendar_trips:
	if visit[0] > visit[1]:
		raise Exception("Ошибка: дата приезда больше даты отъезда", visit)
		
# Ошибка: наложение поездок
for number_visit in range(len(calendar_trips) - 1):
    for number_next_visit in range(number_visit + 1, len(calendar_trips)):
        for day in calendar_trips[number_next_visit]:
            if day >= calendar_trips[number_visit][0] and \
            day <= calendar_trips[number_visit][1]:
                raise Exception("Ошибка: наложение поездок", day)		
    
# Анализ
print('Анализ поездок')

residence_limit = 90
schengen_constraint = 180

days_in_eu = []
total_time_in_es = 0

for visit in calendar_trips:
	past_days = 0
	for past_visit in calendar_trips:
		if past_visit[0] <= visit[0] and past_visit[0] > visit[0] - schengen_constraint:
			past_days += past_visit[1] - past_visit[0] + 1
	days_in_eu.append(past_days)	
	total_time_in_es += visit[1] - visit[0] + 1


# print(days_in_eu)
# print(total_time_in_es)
	
for visit, days in zip(calendar_trips, days_in_eu):
	if days > residence_limit:
		print('В течение поездки %s вы пребывали в ЕС слишком долго: %s' % (visit, days))
	
if total_time_in_es > residence_limit:
    print('Вы не можете прибывать в ЕС так долго')

print('Вы пробудете в ЕС дней:', total_time_in_es)

# Задание # 3

print('Задание # 3')
print('Дата возвращения из последней поездки', end_day)
print('Введите дату начала следующей поездки')

next_start_day = 0
while next_start_day <= end_day:
    next_start_day = int(input())
    if next_start_day <= end_day:
        print('День начала следующей поездки должен быть больше дня приезда')
    
print('Дата начала следующей поездки', next_start_day)
print('Найдем последний возможный день пребывания в ES')

def trip_in_es(calendar_trips):

    residence_limit = 90
    schengen_constraint = 180
    
    condition_1 = True
    condition_2 = True

    days_in_eu = []
    total_time_in_es = 0

    for visit in calendar_trips:
    	past_days = 0
    	for past_visit in calendar_trips:
    		if past_visit[0] <= visit[0] and past_visit[0] > visit[0] - schengen_constraint:
	    		past_days += past_visit[1] - past_visit[0] + 1
    	days_in_eu.append(past_days)	
    	total_time_in_es += visit[1] - visit[0] + 1

    for visit, days in zip(calendar_trips, days_in_eu):
    	if days > residence_limit:
            condition_1 = False       
	        
    if total_time_in_es > residence_limit:
        condition_2 = False

    return condition_1 and condition_2
    
# Проверим возможна ли поездка хотя бы на 1 день

days_in_es = 1
calendar_trips.append([next_start_day, next_start_day + days_in_es])

if trip_in_es(calendar_trips) == True:
    print('Поездка возможна')
    while trip_in_es(calendar_trips) == True:
        days_in_es += 1
        calendar_trips.pop()    # удаляем последнюю поездку
# добавляем новую поездку (на 1 день длинее)
        calendar_trips.append([next_start_day, next_start_day + days_in_es])
    
    calendar_trips.pop()    
    calendar_trips.append([next_start_day, next_start_day + days_in_es-1])
    print('Календарь поездок', calendar_trips)    
        
else:
    print('SORRY! Поездка c этой датой не возможна')    
        



 
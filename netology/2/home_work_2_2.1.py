#!/usr/bin/python3
# -*- coding: utf-8 -*- 

# Задание № 2 v.2.0

# В качестве дополнительной задачи будем генерировать все поездки и ошибки случайным образом
# Добавляем случайные ошибки

def call_error(visits, mistake):
# Вызаваем случайную ошибку
    from random import randrange
    if mistake is True:
        key_mistake = randrange(1, 5)
        functions_mistake = {1: mistake_1, 2: mistake_2, 3: mistake_3, 4: no_mistake}
        functions_mistake[key_mistake](visits)      
    return visits

# Ошибка в типе данны
def mistake_1(visits):
    from random import randrange
    print('Генерируем ощибку в типе данных')
    start_day = visits[0][0]
    end_day = visits[-1][1]
    mistake_date = randrange(start_day, end_day)
    number = randrange(len(visits))        # случайный номер в списке
    visits.insert(number, mistake_date)
    print('Новый список с ошибкой', visits)
    print('Порядковый номер ошибки в списке', number)
    
# Ошибка: дата приезда больше даты отъезда
def mistake_2(visits):
    from random import randrange
    print('Генерируем ощибку: дата приезда больше даты отъезда')
    number = randrange(len(visits))        # случайный номер в списке
    visits[number][1], visits[number][0] = visits[number][0], visits[number][1]    # меняем местами
    print('Новый список с ошибкой', visits)
    print('Порядковый номер ошибки в списке', number)
    
# Ошибка: наложение поездок
def mistake_3(visits):
    from random import randrange
    print('Генерируем наложение поездок')
    number_of_trips = len(visits)
    if number_of_trips >= 2:
        number = randrange(len(visits) - 1)        # случайный номер в списке
        visits[number+1][0] = visits[number][1] - \
                randrange(visits[number][1] - visits[number][0])       
        print('Новый список с ошибкой', visits)
        print('Порядковый номер ошибки в списке', number+1)    
        
# Без ошибок
def no_mistake(visits):
    print('Работа без ошибок')

# Создание календаря поездок
def creating_calendar_trips():

# Записываем конфигурацию поездок в файл config.py /в perl похоже не получится/
# Файл конфигурации для home_work_2
# Начало первой поезди в интервале 0 - 30 дней
    INTERVAL_START = 20
# Продолжительность каждой поездки 0 - 20 дней
    INTERVAL_IN_ES = 30
# Продолжительность между поездками 0 - 20 дней
    INTERVAL_IN_RU = 30
# Количество поездок 0-10
    INTERVAL_NUMBER_OF_TRIPS = 5
# В реальности вызываем эти данные через config.INTERVAL_...

    from random import randrange

# Первый день поездки
    start_day = randrange(1, INTERVAL_START)

# Последний максимально возможный день поездки
    end_day = 366

# Создаем календарь поездок

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
            
        end_day = calendar_trips[-1][1]
    
# Смотрим  даты поездок

    print('У тебя в этом году %s поездок(-ки) в ES!' % number_of_trips)
    print('Список', calendar_trips)
    number_of_trip = 0
    for trip in calendar_trips:
        number_of_trip += 1
        print('Поездка %s - с %s по %s' % (number_of_trip, trip[0], trip[1]))
 
    return calendar_trips
    
# Обработка ошибок

def mistake_type(visits):
# Ошибки в типе поездки
    for visit in visits:
    	if not isinstance(visit, list):
	    	raise Exception("Ошибка в типа поездки", visit)
	    	
def mistake_dates(visits):	
# Ошибка: дата приезда больше даты отъезда
    for visit in visits:
    	if visit[0] > visit[1]:
	    	raise Exception("Ошибка: дата приезда больше даты отъезда", visit)	

def mistake_crossing_dates(visits):	
# Ошибка: наложение поездок
    for number_visit in range(len(visits) - 1):
        for number_next_visit in range(number_visit + 1, len(visits)):
            for day in visits[number_next_visit]:
                if day >= visits[number_visit][0] and \
                day <= visits[number_visit][1]:
                    raise Exception("Ошибка: наложение поездок", day)		
    
# вынесли в функцию самую часто используемую операцию
# в которой не хотелось бы ошибиться
def date_difference (leave, arrive):
	result = leave - arrive + 1
	return result

# сделали работу с длиной визитов более удобной
def visit_length (visit):
	return date_difference(visit[1], visit[0])

# получаем массив дней пребывания
def get_days_for_visits(visits):
	days_for_visits = []
	for visit in visits:
	    days_for_visit = 0
	    for past_visit in visits:
	        if visit[0] - schengen_constraint < past_visit[0] < visit[0]:
	            days_for_visit += visit_length(past_visit)
	    days_for_visit += visit_length(visit)
	    days_for_visits.append(days_for_visit)
	return days_for_visits
	
def print_days_future_visit(visits, date_in_future):
	visits_for_future = visits + [[date_in_future, date_in_future]]
	# используем объявленную функцию
	days_for_future_visits = get_days_for_visits(visits_for_future)
	days_in_es = residence_limit - days_for_future_visits[len(days_for_future_visits) - 1] + 1
	print ('Если въедем %s числа, сможем провести в шенгене %s дней' % (date_in_future, days_in_es))

def print_residence_limit_violation(visits):
	days_for_visits = get_days_for_visits(visits)	
		
	#при изменении кода он помогает нам удостовериться, что код работает как раньше
	assert (days_for_visits == [10, 10 + 30, 10 + 30 + 40, 10 + 30 + 40 + 20, 40 + 20 + 20])
			
	for visit, total_days in zip(visits, days_for_visits):
	    if total_days > residence_limit:
	        overstay_time = total_days - residence_limit
	        print('Во время визита', visit, 'количество время пребывания превышено на', overstay_time, 'дней')


residence_limit = 90
schengen_constraint = 180
   
# visits = creating_calendar_trips()
visits = [[1, 10], [61, 90], [101, 140], [141, 160], [271, 290]]

# True - задаем ошибку; None - работа без ошибок
mistake = None
# mistake = True
visits = call_error(visits, mistake)
print(visits)
    
# Обработка ошибок   
mistake_type(visits)              # ошибка в типе
mistake_dates(visits)	          # ошибка в датах
mistake_crossing_dates(visits)    # ошибка в наложении дат

# Анализ
print('Анализ поездок')

days_in_eu = []
total_time_in_es = 0

print_residence_limit_violation(visits)

print('Задание # 3')
end_day = visits[-1][1]
print('Дата возвращения из последней поездки', end_day)
print('Введите дату начала следующей поездки')

next_start_day = 0
while next_start_day <= end_day:
    next_start_day = int(input())
    if next_start_day <= end_day:
        print('День начала следующей поездки должен быть больше дня приезда')
    
print('Дата начала следующей поездки', next_start_day)
print('Найдем последний возможный день пребывания в ES')


print_days_future_visit(visits, next_start_day)

print(visits)


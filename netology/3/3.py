"""
2 Каждый из типов данных имеет свои особенности и сильные стороны. Которые делают применение именно дпнного типа
более эффективным в конкретном случае. 
Для списка это возможность изменять/добавлять элементы и наличие четкой 
последовательноти (элемент-порядковый номер).
Для кортежа наоборот - ненизменность элементов. В виде кортежа выводят свои результаты многие стандартные функции
Словарь позволяет хранить данные в формате ключ-значение. Таким образом появляется возможность обработки словаря по 
текстровому ключу, а не по порядковому номеру элемента
Множество- не упорядченный набор объектов. Основное достоинство- возможность анализа различных множеств. Пересечение, 
объеденение и т.д.

3 Примеры словарей
"""

passport = {
	'surname' : 'Desyatov',
	'name' : 'Vladimir',
	'number' : 1234567890,
	'date_of_issue' : '2013-09-15',
	'city' : 'Kazan'
	}
	
adress = {
	'country': 'Russia',
	'region' : 'Tatarstan',
	'street' : 'Vosstaniya',
	'house_number' : 10,
	'apartment' : 45
	}
	
books = {
	'Master_i_Margarita': {'author': 'Михаил Булгаков', 
				'genre': 'Мистика', 
				'format': 'pdf',
				'price' : 250
				},
	'Evgenii_Onegin': {'author': 'Александр Пушкин', 
				'format': 'mp3',
				'price': 110},
	'Voina_i_mir': {'author': 'Лев Толстой', 
				'format': 'epub', 
				'price': 185}
	}
	
films = {
	'Titanic': {'country': 'США', 
				'slogan': 'Ничто на Земле не сможет разлучить их', 
				'director': 'Джеймс Кэмерон',
				'year' : 1997,
				'time': 194
				},
	'Avatar': {'country': 'США', 
				'slogan': 'Это новый мир', 
				'director': 'Джеймс Кэмерон',
				'year' : 2009,
				'time': 162
				},
	'The_Fast_and_the_Furious' : {'country': 'США', 
				'slogan': 'Если у тебя есть то, что нужно... ты можешь получить всё', 
				'director': 'Роб Коэн',
				'year' : 2001,
				'time': 106
				}
	}
	
countries = {
	'USA': {'capital': 'Вашингтон', 
				'square':9519, 
				'population': 325,
				'currency': 'доллар'
				},
	'Russia': {'capital': 'Москва', 
				'square': 17125, 
				'population': 146,
				'currency': 'рубль'
				},
	'China': {'capital': 'Пекин', 
				'square': 9598, 
				'population': 1380,
				'currency': 'юань'
				}
	}


# 4 Задачи решаемые с помощью словарей

# 4.1 Объединение множеств

# множества class_1_a - ученики 1 а класса
# множество  class_1_b - ученики 1 б класса
# найти множество class_1 - список учеников 1 а и 1 б классов


class_1_a = {'Иванов', 'Петров', 'Сидоров'}
class_1_b = {'Абрамов', 'Авдеев', 'Агафонов'}
class_1 = class_1_a | class_1_b
print('Список учеников первых классов', class_1)

# 4.2 Разность множеств
# cards_1 - карты у 1-го игрока
# cards_2 - карты у 2-го игрока
# cards - всего карт в колоде
# the_rest_of_the_cards - остаток карт в колоде после раздачи


cards_1 = {1, 2, 3}
cards_2 = {4, 5, 6}
cards = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
the_rest_of_the_cards = cards - cards_1 - cards_2
print('После раздачи в колоде останенутся карты', the_rest_of_the_cards)


# 4.3 
# class_1 - все ученики 1-х классов
# Hockey - список, посесяющих хокейную секцию
# class_1_hockey - найдем учеников 1-х классов, посещающих хаккейную секцию

hockey = {'Абрамов', 'Петров', 'Кузнецов', 'Соколов', 'Тихонов', 'Аксенов'}
class_1_hockey = class_1 & hockey
print('Список первоклассеиков, посещяющих хоккейную секцию', class_1_hockey)


# 4.4 Проверяем все-ли участники хоккейной секции - первоклассники

if hockey <= class_1:
	print('Все участники хоккейной секции первоклассники')
else:
	print('Не все участники хоккейной секции первоклассники')
	
# 4.5 Подсчет количества не повторяющихся элементов.
# Вполне может пригодиться в реальной жизни)

a = {1, 1, 2, 16, 17, 56, 76, 1, 2, 100, 120}
print('В словаре а неповторящихся элементов ', len(a))

# 5 Добавление 5-и стран

countries = {
	'Thailand': {'sea': True, 
				'schengen': False, 
				'average_temperature': 30, 
				'currency_rate': 1.8,
				'the_rate_per_day' : 90},
	'Hungary': {'sea': False, 
				'schengen': True, 
				'average_temperature': 10, 
				'currency_rate': 0.3,
				'the_rate_per_day' : 15},
	'Germany': {'sea': True, 
				'schengen': True, 
				'average_temperature': 5, 
				'currency_rate': 80,
				'the_rate_per_day' : 4000},
	'Japan': {'sea': True, 
				'schengen': False, 
				'average_temperature': 15, 
				'currency_rate': 0.61,	
				'the_rate_per_day' : 31},
	'China': {'sea': True, 
				'schengen': False, 
				'average_temperature': 20, 
				'currency_rate': 9.67,
				'the_rate_per_day' : 484},
	'USA': {'sea': True, 
				'schengen': False, 
				'average_temperature': 18, 
				'currency_rate': 65.84,
				'the_rate_per_day' : 3292},
	'Switzerland': {'sea': False, 
				'schengen': False, 
				'average_temperature': 20, 
				'currency_rate': 66.17,	
				'the_rate_per_day' : 3292},
	'Brazil': {'sea': True, 
				'schengen': False, 
				'average_temperature': 25, 
				'currency_rate': 19.25,
				'the_rate_per_day' : 964},
	'Australia' : {'sea': True, 
				'schengen': False, 
				'average_temperature': 30, 
				'currency_rate': 49.96,
				'the_rate_per_day' : 2500},
				
	}

# Найдем теплые страны 'average_temperature' >= 25 и есть море 'sea': True

warm_countries = set()
sea_countries = set()
	
for country_name, properties in countries.items():
	if properties['average_temperature'] >= 25:
		warm_countries.add(country_name)
	if properties['sea']:
		sea_countries.add(country_name)
		
sea_warm_countries = warm_countries & sea_countries
				
print ('Страны с морем', sea_countries)
print ('Теплые страны', warm_countries)
print('Теплые страны с морем', sea_warm_countries)

# Найдем страны шенгена где мы сможеи прожить 30 дней имея 10 000 рублей

schengen_countries = set()
mounth_stay_countries = set()

for country_name, properties in countries.items():
	if properties['the_rate_per_day'] * 30 <= 10000:
		mounth_stay_countries.add(country_name)
	if properties['schengen']:
		schengen_countries.add(country_name)
		
schengen_mounth_stay_countries = schengen_countries & mounth_stay_countries
		
print ('Страны шенгена', schengen_countries)
print ('Страны где мы сможем прожить месяц', mounth_stay_countries)
print('Страны шенгена где мы сможем прожить месяц', schengen_mounth_stay_countries)

# 6 Тип данных list(countries.items())
"""
[('Australia', {'average_temperature': 30, 'currency_rate': 49.96, 'sea': True, 'the_rate_per_day': 2500, 'schengen': False}), 
('China', {'average_temperature': 20, 'currency_rate': 9.67, 'sea': True, 'the_rate_per_day': 484, 'schengen': False}), 
('Brazil', {'average_temperature': 25, 'currency_rate': 19.25, 'sea': True, 'the_rate_per_day': 964, 'schengen': False}), 
('USA', {'average_temperature': 18, 'currency_rate': 65.84, 'sea': True, 'the_rate_per_day': 3292, 'schengen': False}), 
('Hungary', {'average_temperature': 10, 'currency_rate': 0.3, 'sea': False, 'the_rate_per_day': 15, 'schengen': True}), 
('Thailand', {'average_temperature': 30, 'currency_rate': 1.8, 'sea': True, 'the_rate_per_day': 90, 'schengen': False}), 
('Germany', {'average_temperature': 5, 'currency_rate': 80, 'sea': True, 'the_rate_per_day': 4000, 'schengen': True}), 
('Switzerland', {'average_temperature': 20, 'currency_rate': 66.17, 'sea': False, 'the_rate_per_day': 3292, 'schengen': False}), 
('Japan', {'average_temperature': 15, 'currency_rate': 0.61, 'sea': True, 'the_rate_per_day': 31, 'schengen': False})]
"""

# Судя по скобкам данная операция возвращает список. Элементами которого являются кортеж,
# который в свою очередь состоит из двух элементов строки и словаря
# мне кажется как-то так=:)



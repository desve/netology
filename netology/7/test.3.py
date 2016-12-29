def input_csv():
    import csv
    from pprint import pprint
    file_name = 'csv.csv'
# Считаем количество строк в файле  
    with open(file_name) as file:
        countriies = {}
        lines = file.read().count('\n')     
    with open(file_name) as file:
        countriies = {}
        for line in range(0, lines, 3):       # ситываем по 3 строки из файла
            line_1 = file.readline()
            countriy = line_1[:-1].split(',')
            line_2 = file.readline()
            keys = line_2[:-1].split(',')
            line_3 = file.readline()
            info = line_3[:-1].split(',')
            countriy_info = dict(zip(keys, info))
            countriies[str(countriy[0])] = countriy_info
            
    pprint(countriies)
        
         

    
    
input_csv()

from pprint import pprint
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
	


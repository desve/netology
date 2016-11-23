visits = [[1, 10], [61, 90], [101, 140], [141, 160], [271, 290]]

def write_to_file(calendar_trips, file):
# Записываем в файл
    with open(file, 'w') as calendar_trips_file:
        for line in calendar_trips:
            line_to_file = str(line[0]) + ' ' + str(line[1]) + '\n'
            calendar_trips_file.write(line_to_file)   

def read_from_file(file):
# читаем из файла
    visits = []
    with open(file) as file:
        for line in file:
            visit = line.rstrip().split(" ")
            visits.append(list(map(int, visit)))           
    return visits

# Записываем календарь поездок в файл
write_to_file(visits, 'calendar_trips.txt')

# Читаем календарь поездок из файла
visits = read_from_file('calendar_trips.txt')

print(visits)


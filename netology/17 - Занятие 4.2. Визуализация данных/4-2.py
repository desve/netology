 Занятие 4.2. Визуализация данных

# Включаем отображение в блокноте
%matplotlib inline

def Ruth_and_Robert():
# Строим график изменения количества имен Ruth и Robert с 1900 по 2000
    import pandas as pd
    import os
# Находим текущую директоррию
    PATH = os.getcwd()
    names_by_year = {}
    for year in range(1900, 2000):
# Строим пути к файлам
        file_path = PATH + '/names/yob{}.txt'.format(year)
# Загружаем файлы
        names_by_year[year] = pd.read_csv(file_path,
        names=['Name','Gender','Count'])
        names_all = pd.concat(names_by_year, names=['Year', 'Pos'])
# Строим простой график
    name_dynamics_cols = (names_all.groupby([names_all.index.get_level_values(0),'Name'])
    .sum()
    .query('Name == ["Ruth", "Robert"]')
    .unstack('Name')
    ).plot()

def Ruth_and_Robert_histogram():
# Строим гистограмму по количеству их имен с 1900 по 2000
# с 5-летними промежутками (1900, 1905, 1910, …, 1995, 2000)
    import pandas as pd
    import os
# Находим текущую директоррию
    PATH = os.getcwd()
    names_by_year = {}
    for year in range(1900, 2000, 5):
        file_path = PATH + '/names/yob{}.txt'.format(year)
        names_by_year[year] = pd.read_csv(file_path,
        names = ['Name','Gender','Count'])
        names_all = pd.concat(names_by_year, names = ['Year', 'Pos'])
# Гистограмма
#    name_dynamics_cols = (names_all.groupby([names_all.index.get_level_values(0),'Name'])
    (names_all.groupby([names_all.index.get_level_values(0), 'Name'])
    .sum()
    .query('Name == ["Ruth", "Robert"]')
    .unstack('Name')
    ).plot.bar()

def names_R_circle(number_names_R):
# Строим круговую диаграмму по количеству имен, начинающихся на R за 1950 год
    import pandas as pd
    import os
# Находим текущую директоррию
    PATH = os.getcwd()
# Задаем год
    year = 1950
    file_path = PATH + '/names/yob{}.txt'.format(year)
    names_by_year = pd.read_csv(file_path, names=['Name','Gender','Count'])
# Круговая гистограмма
    pattern = 'R.*'
    names_R = names_by_year[names_by_year.Name.str.contains(pattern)]
    (names_R
    .groupby('Name')
    .sum()
    .sort_values(by = 'Count', ascending = False)
    .head(number_names_R)
    ).plot.pie(y = 'Count')

def name_consonant(row):
# Считаем количество согласных в имени
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z',
                  'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    count_consonants = 0
    for letter in row.Name:
        if letter in consonants:
            count_consonants += 1
    row.Name = count_consonants
    return row

def consonant_in_names_point(interval):
# Строим точечную диаграмму по количеству согласных букв в имени
# и частоте употребления за 100 лет
    import pandas as pd
    import os
# Находим текущую директоррию
    PATH = os.getcwd()
    names_by_year = {}
# Строим фрейм данных за указанный период
    for year in range(1900, 2000, interval):
        file_path = PATH + '/names/yob{}.txt'.format(year)
        names_by_year[year] = pd.read_csv(file_path, names = ['Name', 'Gender', 'Count'])
        names_all = pd.concat(names_by_year, names = ['Year', 'Pos'])
    name_by_consonants = names_all.apply(name_consonant, axis = 1)
    name_by_consonants.plot.scatter(x = 'Name', y = 'Count')

# Задание 1
# Строим график изменения количества имен Ruth и Robert с 1900 по 2000
Ruth_and_Robert()

# Задание 2
# Строим гистограмму по количеству их имен с 1900 по 2000
# с 5-летними промежутками (1900, 1905, 1910, …, 1995, 2000)
Ruth_and_Robert_histogram()

# Задание 3
# Строим круговую диаграмму по количеству имен, начинающихся на R за 1950 год
# Для первых 7 имент
number_names_R = 7
names_R_circle(number_names_R)

# Задание 4
# Строим точечную диаграмму по количеству согласных букв в имени
# и частоте употребления за 100 лет
# С интервалом 25 лет (для ускорения расчета)
interval = 25
consonant_in_names_point(interval)

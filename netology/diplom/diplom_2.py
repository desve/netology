import pandas as pd

# Включаем отображение в блокноте
%matplotlib inline

# Строим гистограммы распределения по возрасту 

# Задаем имя файла
file_name = 'groups_age.json'
# Задвем путь к файду
file_path = '/Users/vladimirdesatov/PycharmProjects/netology/diplom/{0}'.format(file_name)

# Читаем файд json
data = pd.read_json(file_path, orient='columns')

# Переименовываем колонки
data.columns = ['возраст 10-15', 'возраст 16-20', 'возраст 21-30', 'возраст 31-40', 'возраст 41-80', 'старше 81', 'Название группы']
# Переставляем колонки
data_1 = data[['Название группы', 'возраст 10-15', 'возраст 16-20', 'возраст 21-30', 'возраст 31-40', 'возраст 41-80', 'старше 81']]
for group in range(5):
    data = data_1[group:group+1]
    # Строим гистограмму
    # https://pythonworld.ru/novosti-mira-python/scientific-graphics-in-python.html
    data_view = data.groupby(data.index.get_level_values(0)).plot(kind='bar', title = 'Распределение по возрасту')
    plt.xlabel(data['Название группы'], {'fontname':'Times New Roman'}, fontweight='bold', fontsize=16)
    plt.ylabel('Количество участников группы', {'fontname':'Times New Roman'}, fontweight='light', fontsize=14)


# Строим гистограммы распределения по полу

# Задаем имя файла
file_name = 'groups_sex.json'
# Задвем путь к файду
file_path = '/Users/vladimirdesatov/PycharmProjects/netology/diplom/{0}'.format(file_name)

# Читаем файд json
data = pd.read_json(file_path, orient='columns')

# Переименовываем колонки
data.columns = ['пол не указан', 'женщины', 'мужчины', 'Название группы']

# Переставляем колонки
data_1 = data[['Название группы', 'пол не указан', 'женщины', 'мужчины']]
for group in range(5):
    data = data_1[group:group+1]
    # Строим гистограмму
    # https://pythonworld.ru/novosti-mira-python/scientific-graphics-in-python.html
    data_view = data.groupby(data.index.get_level_values(0)).plot(kind='bar', title = 'Распределение по  полу')
    plt.xlabel(data['Название группы'], {'fontname':'Times New Roman'}, fontweight='bold', fontsize=16)
    plt.ylabel('Количество участников группы', {'fontname':'Times New Roman'}, fontweight='light', fontsize=14)





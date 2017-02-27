# -*- coding: utf-8 -*-


def input_id():
    """ Вводим id пользователя """
    while True:
        try:
            user_id = int(input('Please enter a number: '))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return user_id


def authorize_in_vk():
    """ Авторизируемся в VK.com """

    from urllib.parse import urlencode, urlparse

    AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
    APP_ID = 5882265
    VERSION = '5.60'

    auth_data = {
        'client_id': APP_ID,
        'display': 'mobile',
        'response_type': 'token',
        'scope': 'friends',
        'v': VERSION
    }

    # Получаем токен
    # print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))

    TOKEN = 'd3ed3c92827c534fce49ce861f2044eb0a681b9ef1c609b62862831fa9fc9eef55a15bc8a03c212394522&expires_in=86400&user_id=150683960'


    TOKEN_URL = 'https://oauth.vk.com/blank.html#access_token={0}f&expires_in=86400&user_id=150683960'.format(TOKEN)

    o = urlparse(TOKEN_URL)
    fragments = dict((i.split('=') for i in o.fragment.split('&')))
    ACCESS_TOKEN = fragments['access_token']

    return ACCESS_TOKEN, VERSION



def id_followers(USER_ID):
    """Находим ID всех подписчиков пользователя """
    # Получаем TOKEN и версию API
    ACCESS_TOKEN, VERSION = authorize_in_vk()
    params = {'access_token': ACCESS_TOKEN,
              'v': VERSION, 'user_id': USER_ID}
    answer = VkApi(params)
    response = answer.users_getFollowers
    return response


def followers_groups(response):

    """ Получаем словарь подписчиков и их групп.
    В формате {'id подписчика': [id его группы]} """

    # Получаем TOKEN и версию API
    ACCESS_TOKEN, VERSION = authorize_in_vk()

    # Получаем словарь подписчиков и их груп. В формате {'id подписчика': [id его груп]}
    followers_and_groups = {}
    for user, user_id in enumerate(response.json()['response']['items']):

        # Находим список сообществ данного пользователя
        params = {'access_token': ACCESS_TOKEN,
                  'v': VERSION, 'user_id': user_id}
        answer = VkApi(params)
        response_2 = answer.groups_get

        try:
            response_2.json()['error']
            print('Подписчик {0} из {1} - id {2}: страница удалена либо заблокирована'
                  .format(user + 1, response.json()['response']['count'], user_id))
        except:
            print('Подписчик {0} из {1} - id {2}: подписан на {3} групп(ы)'
                  .format(user + 1, response.json()['response']['count'],
                  user_id, response_2.json()['response']['count']))


            groups = response_2.json()['response']['items']
            followers_and_groups[user_id] = groups

    # Составляем список всех груп
    all_groups = []
    for user_id in followers_and_groups:
        for group in followers_and_groups[user_id]:
            all_groups.append(group)

    return all_groups


def top_groups(all_groups):

    """ Получаем список групп.
        В формате : ['title': 'название', 'coutn': 'число подписчиков'] """

    import collections

    # Ищем top-100 групп
    top_100_id = collections.Counter(all_groups).most_common(5)

    # Получаем TOKEN и версию API
    ACCESS_TOKEN, VERSION = authorize_in_vk()

    # Преобразуем в требуемый формат
    top_100_name = []
    for serial_number, group in enumerate(top_100_id):
        # Получаем имя группы по id
        group_id = group[0]
        print('Группа {0} из TOP-5 - group_id= {1} обработана'.format(serial_number + 1, group_id))
        params = {'access_token': ACCESS_TOKEN,
                  'v': VERSION, 'group_id': group_id}
        # Ждем ответ на запрос
        response_is_received = None
        while not response_is_received:
            try:
                answer = VkApi(params)
                response = answer.groups_getById
                name_group = response.json()['response'][0]['name']
                group_info = {'title': name_group, 'count': group[1]}
                top_100_name.append(group_info)
                # Отыет получен
                response_is_received = True
            except KeyError:
                # Ответ не получен
                response_is_received = False
                # Ждем 1 сек
                time.sleep(1)

    return top_100_name, top_100_id


def save_to_json(file_name, info):
    """ Записываем результат в json """
    import simplejson as json
    info_json = json.dumps(info, sort_keys=False, indent=4, ensure_ascii=False, encoding='utf8')
    with open(file_name, 'w') as file:
        file.write(info_json)


def male_or_female(response):
    """ Нахоим количество мужчин и женщин """
    male = 0
    female = 0
    any = 0
    for user in response.json()['response']['items']:
        if user['sex'] == 1:
            female += 1
        elif user['sex'] == 2:
            male += 1
        elif user['sex'] == 0:
            any += 1
    return male, female, any


def age(response):
    """ Находим возраст участников """
    age_10_15 = 0
    age_16_20 = 0
    age_21_30 = 0
    age_31_40 = 0
    age_41_80 = 0
    age_81_older = 0
    age_no = 0
    age_only_birthday = 0
    for user in response.json()['response']['items']:
        # Проверяем наличие поля 'день рождения'
        try:
            # Проверяем наличие поля 'bdate'
            user['bdate']
            if user['bdate'].count('.') == 1:  # проверяем формат 'xx.xx'
                age_only_birthday += 1
            else:
                user_year = user['bdate'][-4:]  # если формат 'xx.xx.xxxx'
                age = 2017 - int(user_year)
                if age >= 10 and age <= 15:
                    age_10_15 += 1
                elif age >= 16 and age <= 20:
                    age_16_20 += 1
                elif age >= 21 and age <= 30:
                    age_21_30 += 1
                elif age >= 31 and age <= 40:
                    age_31_40 += 1
                elif age >= 41 and age <= 80:
                    age_41_80 += 1
                elif age >= 81:
                    age_81_older += 1
        except:
            # Если полу 'bdate' отсутствует
            age_no += 1
    return age_10_15, age_16_20, age_21_30, age_31_40, age_41_80, age_81_older, age_no, age_only_birthday


def sex_and_age(top_100_name, top_100_id):
    """ Находим распреление по возрасту и полу """

    import json

    top = 5 # выбираем Top-5 групп
    print('Находим распреление по возрасту и полу')
    groups_sex = []
    groups_age = []
    for group in range(top):
        time.sleep(5)
        # id группы
        group_id = str(top_100_id[group][0])
        print('Обрабатываем группу {0} из {1} - {2}'.format(group + 1, top, top_100_name[group]['title']))
        # Находим количество участников группы
        params = {'access_token': ACCESS_TOKEN,
                  'v': VERSION, 'group_id': group_id, 'count': 1}
        answer = VkApi(params)
        response = answer.groups_getMembers
        count_group = response.json()['response']['count']
        print('Всего в группе {0} подписчиков'.format(count_group))

        # Обрабатываем по 1000 запросов
        counts_id = 1000
        offset = 0
        male_s = 0
        female_s = 0
        any_s = 0
        age_10_15_s = 0
        age_16_20_s = 0
        age_21_30_s = 0
        age_31_40_s = 0
        age_41_80_s = 0
        age_81_older_s = 0
        age_no_s = 0
        age_only_birthday_s = 0
        for id in range(1, count_group, counts_id):
            step = offset + counts_id
            print('Обрабаьываем с {0} по {1} подписчика группы из {2}'.format(offset, step, count_group))
            # Параметры запроса
            params = {'access_token': ACCESS_TOKEN, 'v': VERSION,
                      'group_id': group_id, 'count': counts_id, 'offset': offset, 'fields': 'sex, bdate'}
            answer = VkApi(params)
            # Ждем ответ на запрос
            response_is_received = None
            while not response_is_received:
                try:
                    # Посылаем запрос
                    response = answer.groups_getMembers
                    # Проверяем выполнение запроса
                    print(response.json().keys())
                    response.json()['response']
                    # Отыет получен
                    print('Ответ получен')

                    response_is_received = True
                    time.sleep(0.5)
                except KeyError:
                    # Запрос отклонен
                    print('Запрос отклонен')
                    response_is_received = False
                    print(response.json())
                    # Ждем 2 сек
                    time.sleep(2)

            # Нахоим количество мужчин и женщин
            male, female, any = male_or_female(response)
            male_s += male
            female_s += female
            any_s += any

            # Находим возраст участников
            age_10_15, age_16_20, age_21_30, age_31_40, \
            age_41_80, age_81_older, age_no, age_only_birthday = age(response)

            age_10_15_s += age_10_15
            age_16_20_s += age_16_20
            age_21_30_s += age_21_30
            age_31_40_s += age_31_40
            age_41_80_s += age_41_80
            age_81_older_s += age_81_older
            age_no_s += age_no
            age_only_birthday_s += age_only_birthday

            # Смещаемся на 1000
            offset += counts_id
            print('offset=', offset)

        # Записываем пол
        # Результат записываем в список в формате
        # [{'title'; 'Название группы', 'male': кол-во женщин, 'female': кол-во мужчин, 'any': любой пол}]
        group_sex = {'title': top_100_name[group]['title'], 'female': female, 'male': male, 'any': any}
        # Добавляем в список
        groups_sex.append(group_sex)

        # Записываем пол
        # Результат записываем в список в формате
        # {'title': 'Название группы', '10_15': 10-15, '16_20': 16-20, '21_39': 21-39,
        # '31_40': 31-40, '41_80': 41-80, 'older_81': 81 и старше}
        group_age = {'title': top_100_name[group]['title'], '10_15': age_10_15, '16_20': age_16_20, '21_39': age_21_30,
                     '31_40': age_41_80, '41_80': age_41_80, '81_older': age_81_older}
        # Добавляем в список
        groups_age.append(group_age)


    return groups_sex, groups_age




class VkApi:

    """ Класс запросрв в ВК
    users_getFollowers - ID всех подписчиков пользователя
    groups_get - список сообществ данного пользователя
    groups_getById - имя группы по id """

    # http://mit.spbau.ru/files/Python_Classes.pdf - шпаргалка пр классам)
    # Список доступных методов https://vk.com/dev/methods

    def __init__(self, params):

        import requests
        import time

        PATH = 'https://api.vk.com/method/'

        # https://vk.com/dev/users.getFollowers
        # Находим ID всех подписчиков пользователя
        self.users_getFollowers = requests.get('{0}users.getFollowers'.format(PATH), params)

        # Находим список сообществ данного пользователя
        # https://vk.com/dev/groups.get
        self.groups_get = requests.get('{0}groups.get'.format(PATH), params)

        # Получаем имя группы по id
        # https://vk.com/dev/groups.getById
        self.groups_getById = requests.get('{0}groups.getById'.format(PATH), params)

        # Получаем список участников сообщества
        # https://vk.com/dev/groups.getMembers
        self.groups_getMembers = requests.get('{0}groups.getMembers'.format(PATH), params)


import time

# USER_ID = 32707600    # Ольга Бузова

# Вводим id пользователя
user_id = input_id()

# Получаем TOKEN и версию API
ACCESS_TOKEN, VERSION = authorize_in_vk()

# Находим ID всех подписчиков пользователя. Для печати использовать response.json()
response = id_followers(USER_ID)

# Получаем словарь подписчиков и их груп. В формате {'id подписчика': [id его группы]}
all_groups = followers_groups(response)

# Получаем список групп. В формате :
# ['title': 'название', 'coutn': 'число подписчиков'], [(id группы, количество подптсок на группу)]
top_100_name, top_100_id = top_groups(all_groups)

# Записываем результат в json
save_to_json('top_100_name.json', top_100_name)

# Находим распреление по возрасту и полу
groups_sex, groups_age = sex_and_age(top_100_name, top_100_id)

# Записываем результат в json
save_to_json('groups_sex.json', groups_sex)
save_to_json('groups_age.json', groups_age)
#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Занятие 3.3. Работа с API ВК, json, работа с менеджером пакетов

from urllib.parse import urlencode, urlparse
import requests
import collections

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.60'
APP_ID = 5809743

KEY = 'Q3Xq9uUr7wc3SYRtDf4d'

auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'response_type': 'token',
    'scope': 'friends',
    'v': VERSION
}

# Получаем токен
# print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))
token_url = 'https://oauth.vk.com/blank.html#access_token=8718321e969c03f09932c510b61bf51e32918902dcbd71e35789eb8401f6bc9c14c8c1f21365db2bc0b9b&expires_in=86400&user_id=150683960'

o = urlparse(token_url)
fragments = dict((i.split('=') for i in o.fragment.split('&')))
access_token = fragments['access_token']

params = {'access_token': access_token,
          'v': VERSION}

# Список доступных методов https://vk.com/dev/methods
# Находим ID всех моих друщей
response = requests.get('https://api.vk.com/method/friends.get', params)

# Получаем словарь моих друзей. В формате {'id друга': [id его друзей]}
my_friends = {}
for user_id in response.json()['response']['items']:
    print('id %s обработан' % user_id)
    response = requests.get('https://api.vk.com/method/friends.get', {'user_id': user_id})
    friends = response.json()['response']
    my_friends[user_id] = friends

print('У меня всего %s друзей' % len(my_friends))

"""
Для решения задачи без использования графов построим список всех друзей друзей
Так как у каждого друга какждый его друг встречается только один раз,
то чем больше раз втретится id в списке- тем больше людей с ним дружит
Если количество будет равно числу моих друзей- значит он является
общим другом для всех моих жрузей
"""

all_friends = []
for key in my_friends:
    for user in my_friends[key]:
        all_friends.append(user)

print('Всего найдено %s друзей друзей' % len(all_friends))

# Ищем top-10 id
top_id = collections.Counter(all_friends).most_common(10)
print(top_id)

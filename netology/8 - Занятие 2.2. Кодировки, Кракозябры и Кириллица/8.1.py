import codecs
import json
import re
import collections

with codecs.open('newsafr.json', encoding = "utf-8") as news:
    info = json.load(news)

words = []
number_news = len(info['rss']['channel']['item'])
for i in range(number_news):  
    text = info['rss']['channel']['item'][i]['description']['__cdata']
# Оставляем только текст
    result = re.findall(r'[а-я,А-Я]\w+', text)   
# Удаляем слова меньше 6 букв    
    result = list(filter(lambda x: len(x) > 6, result))
# Добавляем новые слова в список
    words.extend(result)
    
# Ищем pot-10 слов
top_words = collections.Counter(words).most_common(10)
print(top_words)


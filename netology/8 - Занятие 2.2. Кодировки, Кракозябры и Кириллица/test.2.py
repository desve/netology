import xml.etree.ElementTree as ET
import codecs
import re
import collections

file_name = 'newsit.xml'

with codecs.open(file_name, encoding = 'UTF-8') as news:
    content = news.read()
    tree = ET.fromstring(content)

    words = []
    for info in tree.iter('description'):
        text = info.text
        result = re.findall(r'[а-я,А-Я]\w+', text)    
# Удаляем слова меньше 6 букв    
        result = list(filter(lambda x: len(x) > 6, result))    
# Добавляем новые слова в список
        words.extend(result)   
# Ищем pot-10 слов
    top_words = collections.Counter(words).most_common(10)
    print(top_words)
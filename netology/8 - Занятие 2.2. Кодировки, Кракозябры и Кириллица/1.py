import codecs
import json
# from pprint import pprint

with codecs.open('newsafr.json', encoding = "utf-8") as news:
    text = json.load(news)

# number_news = len(text['rss']['channel']['item'])

for i in range(1):  
    text_info = text['rss']['channel']['item'][i]['description']['__cdata']
    print(text_info)
    
print(text_info)
text_info = list(filter(lambda x: len(x) > 6, text_info))
print('здесь')
print(text_info)
    


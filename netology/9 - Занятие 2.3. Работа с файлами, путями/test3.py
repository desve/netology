from urllib.parse import urlparse

PATH = 'https://github.com/jmistx/Python_course/tree/master/Lesson_2.4/homework/Migrations/'

parsed = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
print(parsed)
# ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', params='', query='', fragment='')

print('scheme  :', parsed.scheme)
print('netloc  :', parsed.netloc)
print('path    :', parsed.path)
print('params  :', parsed.params)
print('query   :', parsed.query)
print('fragment:', parsed.fragment)
print('username:', parsed.username)
print('password:', parsed.password)
print('hostname:', parsed.hostname, '(netloc in lower case)')
print('port    :', parsed.port)


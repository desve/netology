print('Из какой папки будем парсить файлы?')
print('1 - Migrations 2 - Advanced Migrations')

while True:
    var = input()
    if  var == '1':
        PATH = 'https://github.com/jmistx/Python_course/tree/master/Lesson_2.4/homework/Migrations/'   
        break
    elif var == '2':
        PATH = 'https://github.com/jmistx/Python_course/tree/master/Lesson_2.4/homework/Advanced%20Migrations/'
        break
    else:
        print('необходимо ввести 1 или 2')

print(PATH)
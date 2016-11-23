# на кого мы подписаны
# но они не ставят нам лайки и не пишут комметарии

follow = set()                         # на кого мы подписаны
comments = set()                       # кто пишет нам комментарии
likes = set()                          # кто ставит нам лайки
un_follow = set()                      # от кого отписаться

for line in open('follow.txt'):
    line = line.split('\n')            # из строки получаем список
    line = line[0]                     # избавляемся от последнего элемента (\n)
    follow.add(line)                   # добавляем в словарь

for line in open('comments.txt'):
    line = line.split('\n')            # из строки получаем список
    line = line[0]                     # избавляемся от последнего элемента (\n)
    comments.add(line)                 # добавляем в словарь

for line in open('likes.txt'):
    line = line.split('\n')            # из строки получаем список
    line = line[0]                     # избавляемся от последнего элемента (\n)
    likes.add(line)                    # добавляем в словарь

un_follow = follow - likes - comments

file = open('un_follow.txt', 'w')
for item in un_follow:
    file.write(item + '\n')

file.close()



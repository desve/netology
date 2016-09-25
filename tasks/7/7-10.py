# Переставить min and max

from random import randrange

print("Введите количество элементов")
n = int( input())

l =[randrange(0, n) for i in range(n)]

print(l)

max = 0
min = l[0]
i_min = 0

for i in range(n):
    if l[i] > max:
        max = l[i]
        i_max = i
    else:
        continue
        
for i in range(n):
    if l[i] < min:
        min = l[i]
        i_min = i
    else:
        continue

l[i_min], l[i_max] = l[i_max], l[i_min]

print(l)
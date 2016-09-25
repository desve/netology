# Переставить соседние

print("Введите количество элементов в списке")
n = int( input())

from random import randrange

l = []
l = [randrange(n) for i in range(n)]

print(l)

for i in range(1, n, 2):
    l[i-1], l[i] = l[i], l[i-1]
    
print(l)

    
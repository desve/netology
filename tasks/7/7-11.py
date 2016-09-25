# Удалить элемент

from random import randrange

print("Введите количество элементов")
n = int( input())
print("Ввседите индекс элемента")
k = int( input())

l = []
l = [randrange(n) for i in range(n)]
print(l)

for i in range(n):
    if i < k:
        l[i] = l[i]
    elif i == k:
        continue
    elif i > k:
        l[i-1] = l[i]
       
l.pop() 
print(l)
# Четные элементы

from random import randrange

print("Введите количество элементов")
n = int( input())

list = [randrange(1,n) for i in range(n)]
list2 = []
for elem in list:
    if elem % 2 == 0:
        list2.append(elem)
        
print(list)
print(list2)
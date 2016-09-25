# Больше предидущего

from random import randrange

print("Введите количество элементов списка")
n = int( input())

list = []
list2 = []

list = [randrange(1,n) for i in range(n)]

for i in range(n):
    if i == 0:
        continue
    if list[i-1] < list[i]:
        list2.append(list[i])
    
print(list)
print(list2)
# Наибольший элемент

from random import randrange

print("Введите количество элементов")
n = int( input())

l = []
l = [randrange(0, n) for i in range(n)]

for i in range(n):
    if i == 0:
        max = l[0]
        j = 0
    else:
        if l[i] > max:
            max = l[i]
            j = i
        
print(l)
print("Максимальный элемент", max)
print(j)
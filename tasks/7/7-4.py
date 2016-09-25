# Соседи одного знака

from random import randrange

print("Введите количество элементов")
n = int( input())

list=[]

list = [randrange(-n,n) for i in range(n)]
print(list)

for i in range(n):
    if i == 0:
        continue
    if list[i-1] < 0 and list[i] < 0:
        a1 = list[i-1]
        a2 = list[i]
        print(a1, a2)
        break
    elif list[i-1] > 0 and list[i] > 0:
        a1 = list[i-1]
        a2 = list[i]
        print(a1,a2)
        break
    else:
        continue
    
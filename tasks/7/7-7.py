# Шеренга

from random import randrange

print("Введите количество элементов")
n = int( input())
print("Введите рост Пети")
h = int( input())

l = []
l = [randrange(150, 200) for i in range(n)]
print(l)
l2 = []
max = 0
j = 0

while j != n:
    for i in range(j, n):
        if l[i] > max:
            max = l[i]
            i_max = i
        else:
            continue
        l[j], l[i_max] = max, l[j]
    j += 1
    max = 0
print(l)

for i in range(n):
    if h > l[0]:
        i_p = 0
    elif h < l[n-1]:
        i_p = n + 1
    elif h < l[i] and h > l[i+1]:
        i_p = i + 1
    
print(i_p)
# Уникальные элементы

from random import randrange

print("Ввндите количество элементов")
n = int( input())
l = [randrange(0, n) for i in range(n)]
print(l)
i1 = [0 for i in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        if l[i] != l[j]:
            continue
        elif l[i] == l[j]:
            i1[i] += 1
            i1[j] +=1
        else:
            continue

l1 = []
for i in range(n):
    if i1[i] == 0:
        l1.append(l[i])
    
print(l1)
            
            
        
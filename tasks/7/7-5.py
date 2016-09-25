# Больше своих соседей

from random import randrange

print("Ведите количество элементов")
n = int( input())

l = []
l = [randrange(0,n) for i in range(n)]

j = 0
for i in range(n):
    if i == 0:
        continue
    elif i == n-1:
        continue
    else:
        if l[i] > l[i-1] and l[i] > l[i+1]:
            j +=1
            
print(l)
print(j)




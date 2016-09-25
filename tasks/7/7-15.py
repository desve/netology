# Кегельбан

from random import randrange

print("Введите количество кеглей")
n = int( input())
print("Введите количество бросков")
k = int( input())
s = [0 for i in range(n)]
s1 = []

for i in range(k):
    l = randrange(1,n)
    r = randrange(1,n)
    if r < l:
        r, l = l, r
    for j in range(l, r+1):
        s[j] += 1
    
for i in range(n):
    if s[i] == 0:
        s1.append("!")
    else:
        s1.append(".")
        
print(s1)
        

    
# Количество разных элементов

print("Введите не убывающий список (через пробел)")

s = str( input())
l = s.split()

print(l)

n = len(l)
j = 1

for i in range(n):
    if i == 0:
        a = l[0]
    else:
        if l[i] == a:
            continue
        else:
            a = l[i]
            j += 1
            
print("Количество элементов в списке", j)
    
    
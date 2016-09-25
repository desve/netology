# Количество совпадающих пар

print("Введите список")
s = str( input())
l = s.split()
n = len(l)
a = 0
print(l)

for i in range(n):
    for j in range(i+1, n):
        if l[i] == l[j]:
            a += 1
            
print(a)            
            

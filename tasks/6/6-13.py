# Второй максимум

print("Введите последовательность натуральных чисел")

a1 = int( input())
a2 = int( input())

if a1 < a2:
    a1, a2 = a2, a1

n = 1
while n != 0:
    n = int( input())
    if n == 0:
        break
    if a2 > n:
        a1, a2 = a1, a2
    elif a1 > n and a2 < n:
        a1, a2 = a1, n
    elif a1 < n:
        a1, a2 = n, a1
    
print("Второй максимум", a2)
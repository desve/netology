# Максимальное число идущих подряд элементов

print("Введите последовательность натуральных чисел")

n = 1
a = 1
i = 0
max = 0

while n != 0:
    n = int( input())
    if a == n:
        i += 1
        if max < i:
            max = i
    else:
        a = n
        i = 1
        


print(i, max)
            
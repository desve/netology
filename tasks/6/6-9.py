# Максимум последовательности

print("Введите последовательность")

n = 1
a = 0

while n != 0:
    n = int( input())
    if a < n:
        a = n
print(a)
    
# Стандартное отклонение

import math

print("Введите последовательность чисел")

x = 1
n = -1
x1 = 0
x2 = 0
while x != 0:
    n += 1
    x = int( input())
    x1 = x1 + x
    x2 = x2 + x**2
    
s = x1 / n
sigma2 = x2 - 2 * s * x1 + n * s**2
sigma = math.sqrt(sigma2/(n-1))

print("Стандартное отклонение равно sigma=", sigma)


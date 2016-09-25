# Ряд3

import math

print("Введите число А=")
A = int( input())
print("Введите число В=, B < A")
B = int( input())

print("Ряд 3")

A1 = math.ceil(A/2) + math.ceil(A/2) - 1

for i in range(A1, B-1, -2):
    print(i)
print("Конец цикла")
# Номер числа Фибоначчи

print("Введите наткральное число")
A = int( input())

f2 = 0
f1 = 1
f = 1
i = 1
while A > f:
    f = f2 + f1
    f2, f1 = f1, f
    i += 1

if A == f:
    print("Номер числа Фибоначчи", i)
else:
    print("-1")


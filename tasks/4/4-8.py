# Суммафакториалов

print("Введите n=")
n = int( input())

s = 1
ss = 0

for i in range(1, n+1):
    s = i * s
    ss = ss + s
print("Сумма факториалов равна", ss)

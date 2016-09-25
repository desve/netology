# Минимальный делитель

print("Введите целое число не меньше 2-х")
n = int( input())

i = 2
while i <= n:
    if n % i == 0:
        print(i)
    i += 1
else:
    print("Конец задачи")
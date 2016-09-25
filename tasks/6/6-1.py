# Список квадратов

print("Введите целое число N=")
N = int( input())

i = 1
while i <= N:
    if i ** 2 <= N:
        print(i ** 2)
    else:
        break
    i += 1


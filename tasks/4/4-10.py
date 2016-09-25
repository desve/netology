# Лесенка

print("Введите число N=")
N = int( input())

x = 0

for i in range(1, N+1):
    x = x * 10 + i
    print(x)

print("Конец задания")
    
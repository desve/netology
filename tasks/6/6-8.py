# Среднее значение последовательности

print("Введите последовательность")

n = 1
i = 0
sum = 0

while n != 0:
    n = int( input())
    i += 1
    sum += n
else:
    print("Средне значкение", sum/(i-1))
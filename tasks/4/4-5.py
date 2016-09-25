# Сумма N чисел

print("Введите количество чисел N=")
N = int( input())

s = 0

for i in range(N):
    print("Введите число")
    s = s + int( input())
print("Сумма N чисел равна", s)
# Первая цифра после точки

print("Введите положительное число")
n = float( input())

m = int(n)
m1 = n - m
m2 = int(m1 * 10)

print("Первая цифра после запятой", m2)

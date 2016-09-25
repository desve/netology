# Сумма кубов

print("Введите n=")
n = int( input())

s = 0

for i in range(n+1):
    s = s + i**3
print("Сумма кубов равна", s)
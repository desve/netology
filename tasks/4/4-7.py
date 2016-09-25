# Факториал

print("Введите n=")
n = int( input())

s = 1

for i in range(1, n+1):
    s = s * i
print("Фпеториал равен", s)
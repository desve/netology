# Количество нулей

print("Введите число N=")
N = int( input())

s = 0

for i in range(1, N+1):
    print("Введите число", i)
    x = int(input())
    if x == 0:
        s += 1
    else:
        s = s
print("количество введенных 0 равно", s)
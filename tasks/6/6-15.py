# Числа Фибоначчи

print("Введите число n=")
n = int( input())

if n == 0:
    print(n, "0")
elif n == 1:
    print(n, "1")
else:
    f2 = 0
    f1 = 1
    for i in range(2, n+1):
        f = f2 + f1
        f2, f1 = f1, f
        
    print("n=", n, "f=", f)


# Минимум из 3-х чисел

print("Введите первое число")
a = int( input() )
print("Введите второе число")
b = int( input() )
print("Введите третье число")
c = int( input() )

if a <= b:
    if c <= a:
        print("Минимальное число", c)
    else:
        print("минимальное число", a)
else:
    if c <= b:
        print("Минимальное число", c)
    else:
        print("Минимальное число", b)
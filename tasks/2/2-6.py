# Совпадающие числа

print("Введите первое число")
a = int( input() )
print("Введите второе число")
b = int( input() )
print("Введите третье число")
c = int( input() )

if a == b and a == c and b == c:
    n = 3
elif a != b and a != c and b != c:
    n = 0
else:
    n = 2
    
print("Количество совпадающие чисел", n)
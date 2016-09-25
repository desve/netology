# Ряд 1
# Ряд чисел от A до B

print("Введите первое число ряда A=")
A = int( input())
print("Введите второе число ряда B=")
B = int( input())
if A > B:
    print("Значения введены не верно")
    
for i in range(A, B+1):
    print(i)
print("Конец цикла")
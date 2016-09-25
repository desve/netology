# Ряд 2

print("Введите первое число ряда А=")
A = int( input())
print("Введите второе чило ряда В=")
B = int( input())

print("Ряд 2")

if A <= B:
    for i in range(A, B+1):
        print(i)
    print("Конец цикла")
else:
    for i in range(A, B-1, -1):
        print(i)
    print("Конец цикла")
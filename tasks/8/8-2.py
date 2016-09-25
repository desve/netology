# Отрицательная степень

print("Введите основание степени а=")
a = float( input())
print("Введите показатель степени n=")
n = int( input())

def power(a, n):

    if n == 0:
        return 1
    elif n > 0:
        aa = a
        for i in range(1, n):
            a = a * aa
        if a % 1 == 0:
            a = int(a)
        else:
            a = round(a, 3)
        return a
    elif n < 0:
        aa = 1/a
        a = 1
        for i in range(abs(n)):
            a = a  * aa
        return a
print(power(a, n))
        

# Возведние в степень

print("Введите основание степени а=")
a = float( input())
print("Введите показатель степени n=")
n = int( input())

def power(a, n):

    if n == 0:
        return 1
    else:
        return a * power(a, n-1)
    
print(power(a, n))
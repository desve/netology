# Сумма цифр трехзначного числа

print("Ввндите трехзначноечисло")
n = int( input())
if n > 99 and n < 1000:
    n1 = int(n / 100)
    n2 = int((n - n1 * 100) / 10)
    n3 = n % 10
    nn = n1 + n2+ n3
    print("Сумма цифр трехзначного числа", nn)
else:
    print("Число введено не верно")
    
# Банковские проценты

print("Введите начальную сумму вклада x=")
x = int( input ())
print("Введите конечную сумму вклада y=")
y = int( input())
print("Введите проценты по вкладу p=")
p = int( input())

i = 0
sum = x

while sum < y:
    sum = sum + sum * (p/100)
    i += 1
    sum = round(sum, 2)
else:
    print(i, "год")
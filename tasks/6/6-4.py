# Утренняя пробежка

print("Введите начальную дистанцию x=")
x = int( input())
print("Введите конечную дистанцию y=")
y = int( input())

xn = x
i = 0

while xn <= y:
    xn = xn + 0.1 * xn
    i += 1
else:
    print(i+1)
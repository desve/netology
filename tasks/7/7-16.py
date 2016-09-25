# Ферзи

from random import randrange

x = [randrange(1,9) for i in range(8)]
field = False
while field != True:
    y = [randrange(1,9) for i in range(8)]
    print(".")
    c = 0
    for i in range (7):
        for j in range(i+1,8):
            if y[i] == y[j] and x[i] == x[j]:
                c = 1
    if c == 0:
        field = True
    else:
        field = False  
    
# x = [int(s) for s in input().split()]
# y = [int(s) for s in input().split()]

    
print(x)
print(y)

for i in range(8):
    if x[i] == 1:
        x1 = "a"
    elif x[i] == 2:
        x1 = "b"
    elif x[i] == 3:
        x1 = "c"
    elif x[i] == 4:
        x1 = "d"
    elif x[i] == 5:
        x1 = "e"
    elif x[i] == 6:
        x1 = "f"
    elif x[i] == 7:
        x1 = "g"
    elif x[i] == 8:
        x1 = 'h'
    print(x1, y[i])
print(" ")

s = []
s1 = "x x x x "
s2 = " x x x x"
s3 = "  a b c d e f g h"

for i in range(8, 0, -1):
    ss = str(i)
    if i % 2 == 0:
        ss = ss + s1
    else:
        ss = ss + s2
    for j in range(0,8):
        if y[j] == i:
            x_x = x[j]
            s_b = ss[:x_x]
            s_e = ss[x_x+1:]
            ss = s_b + "F" + s_e
    s_s = ""
    for m in range(9):
        s_s = s_s + ss[m] + " "
    print(s_s)
print(s3)

print("Проверка по горизонтали")
c = 0
for i in range(7):
    for j in range(i+1, 8):
        if y[i] == y[j]:
            print("NO!", y[i], y[j])
            c += 1
if c == 0:
    print("YES!")

c = 0    
print("Проверка по вертикали")      
for i in range(7):
    for j in range(i+1, 8):
        if x[i] == x[j]:
            print("NO!", x[i], x[j])
            c += 1
if c == 0:
    print("YES!")
    
c = 0
print("Проверка по 1-й диагонали")
for i in range(7):
    for j in range(i+1, 8):
        if x[i] == x[j] - 1 and y[i] == y[j] - 1:
            print("NO!", x[i], y[i], "-", x[j], y[j])
            c += 1
if c == 0:
    print("Yes!")
    
c = 0
print("Проверка по 2-й диагонали")
for i in range(7):
    for j in range(i+1, 8):
        if x[i] == x[j] + 1 and y[i] == y[j] + 1:
            print("NO!", x[i], y[i], "-", x[j], y[j])
            c += 1
if c == 0:
    print("Yes!")
    
c = 0
print("Проверка по 3-й диагонали")
for i in range(7):
    for j in range(i+1, 8):
        if x[i] == x[j] + 1 and y[i] == y[j] - 1:
            print("NO!", x[i], y[i], "-", x[j], y[j])
            c += 1
if c == 0:
    print("Yes!")
    
c = 0
print("Проверка по 4-й диагонали")
for i in range(7):
    for j in range(i+1, 8):
        if x[i] == x[j] - 1 and y[i] == y[j] + 1:
            print("NO!", x[i], y[i], "-", x[j], y[j])
            c += 1
if c == 0:
    print("Yes!")
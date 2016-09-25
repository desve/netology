# Ход коня
# a-h - поле по горизонтили
# 1-8 - поле по вертикале

print("Введите начальное поле по горизонтиле (a-h)")
x1 = str( input() )
if x1 == "a" or x1 == "b" or x1 == "c" or x1 == "d" or x1 == "e" or x1 == "f" or x1 == "g" or x1 == "h":
    x1 = x1
    if x1 == "a":
        x11 = 1
    elif x1 == "b":
        x11 = 2
    elif x1 == "c":
        x11 = 3
    elif x1 == "d":
        x11 = 4 
    elif x1 == "e":
        x11 = 5
    elif x1 == "f":
        x11 = 6
    elif x1 == "g":
        x11 = 7
    else:
        x11 = 8
else:
    print("Поле введено не верно")
    
print("Введите начальное поле по вертикали (1-8)")
y1 = int( input () )
if y1 == 1 or y1 == 2 or y1 == 3 or y1 == 4 or y1 == 5 or y1 == 6 or y1 == 7 or y1 == 8:
    y1 = y1
else:
    print("Поле введено не верно")


print("Введите конечное поле по горизонтиле (a-h)")
x2 = str( input() )
if x2 == "a" or x2 == "b" or x2 == "c" or x2 == "d" or x2 == "e" or x2 == "f" or x2 == "g" or x2 == "h":
    x2 = x2
    if x2 == "a":
        x22 = 1
    elif x2 == "b":
        x22 = 2
    elif x2 == "c":
        x22 = 3
    elif x2 == "d":
        x22 = 4 
    elif x2 == "e":
        x22 = 5
    elif x2 == "f":
        x22 = 6
    elif x2 == "g":
        x22 = 7
    else:
        x22 = 8   
else:
    print("Поле введено не верно")
    
print("Введите начальное поле по вертикали (1-8)")
y2 = int( input () )
if y2 == 1 or y2 == 2 or y2 == 3 or y2 == 4 or y2 == 5 or y2 == 6 or y2 == 7 or y2 == 8:
    y2 = y2
else:
    print("Поле введено не верно") 
    
if (x22 - x11) == 2 and (y2 - y1) == 1:
    print("YES! Это ход коня 1")
elif (x22 - x11) == 1 and (y2- y1) == 2:
    print("YES! Это ход коня 2")
elif (x11 - x22) == 1 and (y2 - y1) == 2:
    print("YES! Это ход коня 3")
elif (x11 - x22) == 2 and (y2 - y1) == 1:
    print("YES! Это ход коня 4")
elif (x11 - x22) == 2 and (y1 - y2) == 1:
    print("YES! Это ход коня 5")
elif (x11 - x22) == 1 and (y1 - y2) == 2:
    print("YES! Это ход коня 6")
elif (x22 - x11) == 1 and (y1 - y2) == 2:
    print("YES! Это ход коня 7")
elif (x22 - x11) == 2 and (y1 - y2) == 1:
    print("YES! Это ход коня 8")
else:
    print("NO! Конь так не ходит")
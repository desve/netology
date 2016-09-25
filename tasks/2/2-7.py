# Ход ладьи
# a-h - поле по горизонтили
# 1-8 - поле по вертикале

print("Введите начальное поле по горизонтиле (a-h)")
x1 = str( input() )
if x1 == "a" or x1 == "b" or x1 == "c" or x1 == "d" or x1 == "e" or x1 == "f" or x1 == "g" or x1 == "h":
    x1 = x1
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
else:
    print("Поле введено не верно")
print("Введите начальное поле по вертикали (1-8)")
y2 = int( input () )
if y2 == 1 or y2 == 2 or y2 == 3 or y2 == 4 or y2 == 5 or y2 == 6 or y2 == 7 or y2 == 8:
    y2 = y2
else:
    print("Поле введено не верно") 
    
if x1 == x2 or y1 == y2:
    print("YES! Это ход ладьи")
else:
    print("NO! Ладья так ходить не может")

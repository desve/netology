# Шахматная доска
# a-h - кдетки по горизонтили
# 1-8 - клетки по вертикали

print("Первое поле")
print("Введите поле по горизонтали (a-h)")
x1 = str( input() )
print("Введите поле по вертикаде (1-8)")
y1 = int( input() )

if x1 == "a" or x1 == "c" or x1 == "e" or x1 == "g":
    if y1 == 1 or y1 == 3 or y1 == 5 or y1 == 7:
        color1 = "black"
    elif y1 == 2 or y1 == 4 or y1 == 6 or y1 == 8:
        color1 = "white"
    else:
        print("Поле введено неверно")
        color1 = "wrong"
elif x1 == "b" or x1 == "d" or x1 == "f" or x1 == "h":
    if y1 == 1 or y1 == 3 or y1 == 5 or y1 ==7:
        color1 = "white"
    elif y1 == 2 or y1 == 4 or y1 == 6 or y1 == 8:
        color1 = "black"
    else:
        print("Поле введено неверно")  
        color1 = "wrong"
else:
        print("Поле введено неверно")
        color1 = 'wrong'

print("Второе поле")
print("Введите поле по горизонтали (a-h)")
x2 = str( input() )
print("Введите поле по вертикаде (1-8)")
y2 = int( input() )

if x2 == "a" or x2 == "c" or x2 == "e" or x2 == "g":
    if y2 == 1 or y2 == 3 or y2 == 5 or y2 == 7:
        color2 = "black"
    elif y2 == 2 or y2 == 4 or y2 == 6 or y2 == 8:
        color2 = "white"
    else:
        print("Поле введено неверно")
        color2 = "wrong"
elif x2 == "b" or x2 == "d" or x2 == "f" or x2 == "h":
    if y2 == 1 or y2 == 3 or y2 == 5 or y2 ==7:
        color2 = "white"
    elif y2 == 2 or y2 == 4 or y2 == 6 or y2 == 8:
        color2 = "black"
    else:
        print("Поле введено неверно")
        color2 = "wrong"
else:
        print("Поле введено неверно")
        color2 = "wrong"
        
print("Первое поле", color1)
print("Второе поле", color2)

if color1 != "wrong" and color2 != "wrong":
    if color1 == color2:
        print("поля совпадают по цвету. YES!")
    else:
        print("поля не совпадают по цвету. NO!")
else:
    print("поля введены не верно")



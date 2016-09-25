# Часы 3
# alfa - Угол повороты часовой стрелки
# H - количество часов
# M - количество минут
# S - количество секунд


print("Введите угол поворота часовой стрелки alfa=")
alfa = float( input())
if alfa >= 0 and alfa < 360:
    print("Угол поворота часовой стрелки alfa=", alfa)
else:
    print("Угол поворота введен не верно")
    
H = int(alfa // 30)
alfa_H = H * 30
print("H=", H)

alfa_M_S = alfa - alfa_H
M = int(60 * (alfa_M_S / 30))
print("M=", M)

alfa_S = alfa_M_S - (M * (30 / 60))
S = int((3600 / 30) * alfa_S)
print("S=", S)












# Часы 2
# alfa - угол поворота часовой стрелки
# betta - угол поворота минутной стрелки

print("Введите угол поворота часовой стрелки alfa=")
alfa = int( input())
if alfa >= 0 and alfa < 360:
    print("Угол поворота часовой стрелки alfa=", alfa)
else:
    print("Угол поворота введен не верно")
    
alfa_H = alfa // 30
alfa_M = alfa - (alfa_H * 30)
betta = int(360 * (alfa_M / 30))

print("Угол поворота минутной стрелки", betta)

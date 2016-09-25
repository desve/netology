# Часы 1
# H - часы
# M - минуты
# S - секунды

print("Введите количество часов")
H = int( input())
if H >= 0 and H < 12:
    print("H=", H)
else:
    print("Значение Н введено не верно")
    
print("Введитеколичество минут")
M = int( input())
if M >= 0 and M < 60:
    print("M=", M)
else:
    print("Значение М введено не верно")
    
print("Введите количество секунд S=")
S = int( input())
if S >= 0 and S < 60:
    print("S=", S)
else:
    print("Значение S введено не верно")
    
angle_H = (360 / 12) * H
angle_M = (360 / 12) * (M / 60)
angle_S = (360 / 12) * (1 / 60) * (S / 60)

angle =angle_H + angle_M + angle_S

print("Часовая стрелка повернулась на", angle, "градусов")
# Проценты
# P - процентная ставка (годовых)
# X руб Y коп - сумма вклада

import math

print("Введите процентную ставку")
N = int( input())
print("Введите сумму вклада в рублях")
X = int( input())
print("Введите сумму вклада в копейках")
Y = int( input())

Zb = X + Y/100
n = N /100
Ze = Zb * (1 + n)
Xe = int(Ze)
Ye = (Ze - Xe) * 100
Ye = int( round(Ye, 2))
print("Сумма вклада в конце года", Xe, "рублей", Ye, "копеек")

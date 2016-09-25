# автопробег
# n - пробег за день
# m - пробегвсего
# t - количество дней

import math

print("Введите дневной пробег")
n = float( input())
print("Введите общий пробег")
m = float( input())

t = math.ceil(m / n)

print("Всего потребуется", t, "дней")
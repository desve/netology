# Длина отрезка

print("Введите координаты первойточки (x1,y1)")
s1 = input().split()
s2 = input().split()
x1 = float(s1[0])
y1 = float(s1[1])
x2 = float(s2[0])
y2 = float(s2[1])

def distance(x1, y1, x2, y2):
    from math import sqrt
    if x1 > x2:
        x1, x2 = x2. x1
    if y1 > y2:
        y1, y2 = y2, y1
    sx = x2 - x1
    sy = y2 - y1
    s = sqrt( sx**2 + sy**2)
    return round(s, 5)

print(distance(x1, y1, x2, y2))

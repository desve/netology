# Игра в пьяницу

f_h = [1, 3, 5, 7, 9]
s_h = [2, 4, 6, 8, 0]

print("Начало игры")
print(f_h)
print(s_h)

play = True
num = 0
while play == True:
    c1 = f_h[0]
    c2 = s_h[0]
    num += 1
    if c1 > c2 and (c1 != 9 and c2!= 0):
        f_h.append(c1)
        f_h.append(c2)
        f_h.pop(0)
        s_h.pop(0)
    elif c1 == 9 and c2 == 0:
        s_h.append(c1)
        s_h.append(c2)
        f_h.pop(0)
        s_h.pop(0)
    elif c2 > c1 and (c2 != 9 and c1 != 0):
        s_h.append(c1)
        s_h.append(c2)
        f_h.pop(0)
        s_h.pop(0)
    elif c2 == 9 and c1 == 0:
        f_h.append(c1)
        f_h.append(c2)
        f_h.pop(0)
        s_h.pop(0)
    if len(f_h) == 0 or len(s_h) == 0:
        play = False
    print("Ход ", num)
    print(f_h)
    print(s_h)
        
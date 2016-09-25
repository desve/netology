# Потерянная карточка

print("Введите количество карточек N=")
N = int( input())

s = 0
for i in range(1, N+1):
    s += i

ss = 0
for i in range(1, N):
    ss = ss + int( input())
print("Потеряна карточка", s-ss)    

    
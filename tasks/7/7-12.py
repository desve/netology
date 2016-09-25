# Вставить элемент

print("Введите список")
s = str( input())
l = s.split()
print(l)

print("Введите индекс")
k = int( input())
print("Введите элемент")
c = int( input())

n = len(l) - 1
for i in range(n):
    if i < k:
        l[i] = l[i]
    elif i == k:
        x = l[i]
        l[i] = c
    elif i > k and i < n:
        l[i], x = x, l[i]

l[n], x = x, l[n]
l.append(x)
print(l)
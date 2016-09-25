# Города и дороги

print("Введите количество городов n=")
n = int( input())

print("Введите строки")
a = []
for i in range(n):
    row = input().split()
    for j in range(n):
        row[j] = int(row[j])
    a.append(row)
    
for row in a:
    print(" ".join([str(elem) for elem in row]))

k = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if i > j:
            continue
        if i < j:
            if a[i][j] == 0:
                continue
            if a[i][j] == 1:
                k += 1
                
print("Количество дорог в королевстве k=")
print(k)
                
    
    
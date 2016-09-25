# Поменять столбцы

print("Введите размер массива n=")
n = int( input())
print("Введите размер массива m=")
m = int( input())

a = []
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    a.append(row)

print("Введите столбец i=")
i = int( input())
print("Введите столбец j=")
j = int( input())

def swap_columns(a, i, j):
    for k in range(len(a)):
        for l in range(len(a[k])):
            if l == i:
                a[k][i], a[k][j] = a[k][j], a[k][i]
    return a
    
a = swap_columns(a, i, j)
for row in a:
    print(" ".join([str(elem) for elem in row]))

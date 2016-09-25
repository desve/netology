# Побочные диагонади

print("Введите число n=")
n = int( input())

a = []
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            a[i][j] = 1
        if i + j < n -1:
            a[i][j] = 0
        if i + j > n - 1:
            a[i][j] = 2
            
for row in a:
    print(" ".join([str(elem) for elem in row]))
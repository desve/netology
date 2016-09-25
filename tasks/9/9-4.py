# Диагонали: параллейные главной

print("Введите размермассива n=")
n = int( input())
 
a = []  
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 0
        elif j > i:
            a[i][j] = j - i
        elif j < i:
            a[i][j] = i - j

for row in a:
    print(" ".join([str(elem) for elem in row]))
        
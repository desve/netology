# Снежинка

print("Введите число n=")
n = 0
while n % 2 == 0:
    n = int( input())

a = [["." for i in range(n)] for j in range(n)]

i1 = (n-1) / 2
j1 = (n-1) / 2
for i in range(n):
    for j in range(n):
        if j == j1:
            a[i][j] = "*"
        elif i == i1:
            a[i][j] = "*"
        elif i == j:
            a[i][j] = "*"
        elif i + j == n-1:
            a[i][j] = "*"
        
for row in a:          
     print(" ".join([str(elem) for elem in row]))
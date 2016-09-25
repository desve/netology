# Полустепени вершин

n = 5
a= [[0, 0, 0, 0, 0],    
    [0, 0, 0, 0, 1], 
    [1, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0]
   ]

c1 = [0] * n
for i in range(n):
    c11 = 0
    for j in range(n):
        if a[i][j] == 1:
            c11 += 1
    c1[i] = c11

c2 = [0] * n
for i in range(n):
    c22 = 0
    for j in range(n):
        if a[j][i] == 1:
            c22 += 1
    c2[i] = c22
        
for i in range(n):
    print("Вершина", i+1)
    print("Заходов", c2[i])
    print("Исходов", c1[i])
    print("--------------------")

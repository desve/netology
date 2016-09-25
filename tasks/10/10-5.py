# От списка ребер к матрице смежности, неориентированный вариант

print("Введите количество вершин N=")
n = int( input())
print("Введите количество ребер M=")
m = int( input())

l = [[5, 3],                    # Список ребер
     [1, 3],
     [2, 3],
     [2, 5]
    ]
a = [[0] * n for i in range(n)]   # Матрица смежности

for k in range(len(l)):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if l[k][0] == i and l[k][1] == j:
                a[i-1][j-1] = 1
            if l[k][1] == i and l[k][0] == j:
                a[i-1][j-1] = 1
            
for i in range(n):
    print(a[i])
            




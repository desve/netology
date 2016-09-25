# Космические путешествия

import copy
a = [[1, 4],         # 0
     [0, 2, 3],      # 1
     [1],            # 2
     [1, 4],         # 3
     [0, 3],         # 4
    ]
    
print(a)
n = 5

copy_a = copy.deepcopy(a)

def del_point(p):
    global edge
    edge = []
    for i in range(len(a[p])):
        edge.append(a[p][i])
    for i in range(len(a[p]) -1, -1, -1):
#        print("Удаляем ребро", p, a[p][i])
        del a[p][i]
#        print(a)
    for i in range(n):
        j = -1
        for elem in a[i]:
            j += 1
            if elem == p:
#                print("Удаляям ребро", i, a[i][j])
                del a[i][j]
#                print(a)

def dfs(v):
    visited[v] = True
    for w in a[v]:
        if visited[w] == False:
            dfs(w)


for i in range(n):
    visited = [False] * n
    del_point(i)
    j = 0
    for v in range(n):
        if visited[v] == False:
            j += 1
            dfs(v)
    print("Точка", i, "Количество компонент сязанности", j)
    a = copy.deepcopy(copy_a)



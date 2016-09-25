# Получи дерево

n = 11    # Вершины
m = 13    # Ребра

a = [[1, 2],               # 0
     [0, 2],               # 1
     [0, 1, 3, 4, 5, 6],   # 2
     [2],                  # 3
     [2, 6, 9],            # 4
     [2],                  # 5
     [2, 4, 7, 8],         # 6
     [6],                  # 7
     [6, 9, 10],           # 8
     [4, 8],               # 9
     [8]                   # 10
    ]

a1 = []
a1 = a

def dfs(v):
    visited[v] = True
    for w in a[v]:
        if visited[w] == False:
            dfs(w)
            
def del_edge(a, k, l):    # Удаление ребер
    i = -1
    for elem in a[k]:
        i += 1
        if elem == l:
            del a[k][i]
    i = -1
    for elem in a[l]: 
        i += 1
        if elem == k:
            del a[l][i]
            
def plus_edge(a, k, l):    # Добавление ребер
    a[k].append(l)
    a[l].append(k)
            
def edge(a, b, e):    # Проверка наличия ребер
    for elem in a[b]:
        if elem == e:
            return True
        
for i in range(n - 1):
    for j in range(1, n):
        if edge(a, i, j) == True:
#            print("Удаляем ребро", i, j)
            del_edge(a, i, j)
#            print(a1)
            visited = [False] * n
            dfs(0)
#            print(visited)
            sv = 1
            for elem in visited:
                if elem == False:
                    sv += 1
            if sv == 1:
                print("ребро", i, j, "нужно удалить")
#                print(a)
            else:
#                print("ребро", i, j, "удалить нельзя")
#                print("Возвращвем ребро", i, j)
                plus_edge(a, i, j)
#                print(a)

print("Окончательно!")
for i in range(n):
    print(a[i])
        
   
   




  





        

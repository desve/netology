# Обход в глубину

#
#   2--0--6--7   1--9   5
#   |  |  |
#   3--4  8 
#
n = 10  # количество вершин
adj_list = [[2, 4, 6],
            [9],
            [0, 3],
            [2, 4],
            [0, 3],
            [],
            [0, 7, 8],
            [6],
            [6],
            [1]]
s = 0
visited = [False] * n  # массив "посещена ли вершина?"

def dfs(v):  # dfs is an acronym for "depth-first search"
    visited[v] = True
    for w in adj_list[v]:  # переменная w пробегает всех соседей вершины v
        if visited[w] == False:  # посещён ли текущий сосед?
            dfs(w)

dfs(s)

print(visited.count(True))
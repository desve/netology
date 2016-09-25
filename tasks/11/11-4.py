# Долой списывание!

#a = [[4, 7, 8],  # 0 blue
#     [4],        # 1 blue
#     [5, 6, 7],  # 2 blue
#     [5, 7],     # 3 blue
#     [0, 1],     # 4 red
#     [2, 3],     # 5 red
#     [2],        # 6 red
#     [0, 2, 3],  # 7 red
#     [0]         # 8 red
#    ]
    
a = [[1],           # 0 blue
     [0, 6, 2],     # 1 red
     [1, 4, 5, 8],  # 2 blue
     [6],           # 3 red
     [2],           # 4 red
     [2, 7],        # 5 red
     [3, 1],        # 6 blue
     [5],           # 7 blue
     [2]            # 8 red
    ]  
    
    
n = 9            # количество студентов
m = 2            # количество пар студентов
    
color = ["none"] * n
visited = [False] * n

def change_color(cur_color):

    return cur_color

def dfs(v):
    print("v=", v)
    global cur_color
    visited[v] = True
    color[v] = cur_color
    print(cur_color)
    for w in a[v]:
        print("Ребро", v, "-", w)
        if visited[w] == False:
            print("Ребро", v, "-", w)
            bg_color = color[v]
            print(bg_color)
            if bg_color == "red":
                cur_color = "blue"
            elif bg_color == "blue":
                cur_color = "red"
            color[w] = cur_color
            print(color)
            dfs(w)

global cur_color
cur_color = "blue"
s = 0
dfs(s)
    
print(color)
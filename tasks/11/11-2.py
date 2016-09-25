# Грядки

n = 5
m = 10

a = ['##..#####.', 
     '.#.#.#....', 
     '###..##.#.',
     '..##.....#',
     '.###.#####'
    ]
    
def point(a, x, y):
     s = a[y]
     return s[x]


visited = [[False] * m for i in range(n)]
vis = [0] * m *n


def dfs(x, y):
    visited[y][x] = True
    for dy, dx in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
        if (x + dx >= 0 and
                x + dx <= m - 1 and
                y + dy >= 0 and
                y + dy <= n - 1 and
                visited[y + dy][x + dx] != True and
                point(a, x + dx, y + dy) == "#"):
            global num
            num += 1
            print("x=", x + dx, "y=", y + dy, "num=", num)
            dfs(x + dx, y + dy)

x = 0
y = 0
for x in range(m):
    for y in range(n):
        if point(a, x, y) == "#" and visited[y][x] != True:
            global num
            num = 1
            print("Начало грядки")
            print("x=", x, "y=", y, "num=", num)
            dfs(x, y)
            print("Конец грядки")
            vis[x + y * n] = num


for i in range(n * m):
    if vis[i] != 0:
        print(vis[i])
    


          


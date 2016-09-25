# Транзитивность неориентированного графа

print("Введите количество вершин N=")
n = int( input())
print("Введите количество ребер M=")
m = int( input())

l = [[1, 5],
     [1, 7],
     [2, 3],
     [3, 6],
     [4, 5],
     [5, 1],
     [6, 3],
     [7, 1],
     [7, 6]
    ]

k = 0    
for i in range(len(l)):
     l1 = l[i][0]
     l2 = l[i][1]
     for j in range(i+1, len(l)):
          if l[j][0] == l2 and l[j][1] == l1:
               print(l[j][0], l[j][1])
               k += 1
k = len(l) - k
print(k)





        
        
    


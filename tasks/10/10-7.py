# Проверка на неориентированность

n = 5
a = [[0, 0, 1, 0, 0], 
     [0, 0, 1, 0, 1], 
     [1, 1, 0, 0, 0], 
     [0, 0, 0, 0, 0], 
     [0, 1, 0, 0, 0]
    ]

graf = True
for i in range(n):
    if a[i][i] != 0:
        print("NO!")
        graf = False
        break
    for j in range(i+1, n):
        if a[i][j] != a[j][i]:
            print("NO!")
            graf = False
            break
    
if graf == True:
    print("Yas!")
        

    
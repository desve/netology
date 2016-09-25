# Проверка на наличие параллейных ребер. Ориентированный вариант

n = 5
l = [[5, 3],
     [2, 5],
     [3, 1],
     [3, 2]
    ]
    
graf = True
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] == l[j]:
            print(l[i], l[j])
            graf = False
            print("NO!")
            break
        
if graf != False:
    print("YES!")
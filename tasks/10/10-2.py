# Светофорчики

print("Вводим количество перекрестков N=")
n = int( input())
print("Вводим количество тунелей M=")
m = int (input())

a= [[5, 1],
    [3, 2],
    [7, 1],
    [5, 2],
    [7, 4],
    [6, 5],
    [6, 4],
    [7, 5],
    [2, 1],
    [5, 3],
   ]
    
#for i in range(m):
#    row = input().split()
#    for j in range(n):
#        row[j] = int(row[j])
#    a.append(row)
    
for row in a:
    print(" ".join([str(elem) for elem in row]))
    
tl = [0 * n for n in range(n)]      # определяем массив светофоров   
for row in a:  
    for elem in row:  
        tl[elem-1] += 1

print(tl)       

        
        
        
    
    
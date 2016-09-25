# Максимум

print("Введите количество строк n=")
n = int( input())
print("Введите количество столбцов m=")
m = int( input())

a = []
for i in range(n):
    row = input().split()
    for i in range(m):
        row[i] = int(row[i])
    a.append(row)
print(a)

max = 0
i_max = 0
j_max = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > max:
            max = a[i][j]
            i_max = i
            j_max = j
            
print(max)
print(i_max)
print(j_max)
        
        
    
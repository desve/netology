# Шахматная доска

print("Введите размер n=")
n = int( input())
print("Введите размер m=")
m = int( input())

def chet(i):
    if i % 2 == 0:
        return True
    else:
        return False
 
row1 = []
row2 = []
for i in range(m):
    if chet(i) == True:
        row1.append(".")
        row2.append("*")
    if chet(i) == False:
        row1.append("*")
        row2.append(".")

a = []
for i in range(n):
    if chet(i) == True:
        a.append(row1)
    if chet(i) == False:
        a.append(row2)
        
for row in a:
    print(" ".join([str(elem) for elem in row]))
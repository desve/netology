# Степень двойки

print("Введите натуральное число")
N = int( input())

i = 1
n2 = 1
while i <= N:
    n2 = n2 * 2
    if n2 <= N:
        i += 1
    else:
        break
        
print(int(n2/2), i-1)

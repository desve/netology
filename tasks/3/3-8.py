# Округление

print("Введите положительное число")
x = float ( input())

x1 = int(x)
x2 = x - x1

if x2 < 0.5:
    x12 = x1 
else:
    x12 = x1 + 1
    
print("Округленное число", x12)
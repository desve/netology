# Количество элементов равных максимому

print("Введите последовательность")

a = 0
n = 1
i = 1
while n != 0:
    n = int( input ())
    if a < n:
        a = n
    elif a == n:
        i += 1

print(i)
            
                
            
    
# Четные индексы

print("Введите количество элементов списка")
n = int( input())

list = []
list2 = []
# Автозаполнение списка
list = [i**2 for i in range(n)]
    
print(list)   

for i in range(0, n, 2):
    list2.append(list[i])
    
print(list2)
# Чтение Списка из файла

def read_kb():
    fin = open("input.txt", "r")     # r - read
    a = [line.strip() for line in fin]
    return a
    
a = read_kb()    
print(a)
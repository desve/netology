# Запись Списка в файл

from keyboad_for_bot import taro_kb

def save_kb(list):
    fout = open("input.txt", "w")    # w - write
    for i in range(len(list)):
        print(list[i], file = fout)
    fout.close
    
kb = []
kb = taro_kb(22)
print(kb)
save_kb(kb) 

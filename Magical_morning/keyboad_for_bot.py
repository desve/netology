# Клавиатуры для ботов

def taro_kb(num):
    keyboad = []  
    from random import shuffle
    for i in range(65, 65 + num):
        keyboad.append(chr(i))
    shuffle(keyboad)
    return keyboad

def save_kb(list):
    fout = open("input.txt", "w")    # w - write
    for i in range(len(list)):
        print(list[i], file = fout)
    fout.close
    
def read_kb():
    fin = open("input.txt", "r")     # r - read
    a = [line.strip() for line in fin]
    return a
    
def save_arcan_num_1():
    fout = open("arcan_num.txt", "w")    # w - write
    print('1', file = fout)
    fout.close
    
def save_arcan_num(arcan_num):
    fout = open("arcan_num.txt", "w")       # w - write
    print(arcan_num, file = fout)
    fout.close

def read_arcan_num():
    fin = open("arcan_num.txt", "r")        # r - read
    x = fin.read()
    return x
    
def save_fs(final_state):
# Запись конечных состояний
    fout = open("final_state.txt", "w")     # w - write
    print(final_state, file = fout)
    fout.close   
    
def read_fs():
    fin = open("final_state.txt", "r")       # r - read
    x = fin.read()
    return x
    

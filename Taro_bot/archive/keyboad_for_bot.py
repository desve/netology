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
    
def save_fs_2(final_state):
# Запись конечных состояний
    fout = open("final_state_2.txt", "w")     # w - write
    print(final_state, file = fout)
    fout.close   
    
def read_fs_2():
    fin = open("final_state_2.txt", "r")       # r - read
    x = fin.read()
    return x
    
def save_fs_3(final_state):
# Запись конечных состояний
    fout = open("final_state_3.txt", "w")     # w - write
    print(final_state, file = fout)
    fout.close   
    
def read_fs_3():
    fin = open("final_state_3.txt", "r")       # r - read
    x = fin.read()
    return x
    
def generate_markup(kb):
    from telebot import types
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton(kb[0])
    btn2 = types.KeyboardButton(kb[1])
    btn3 = types.KeyboardButton(kb[2])
    btn4 = types.KeyboardButton(kb[3])
    btn5 = types.KeyboardButton(kb[4])
    btn6 = types.KeyboardButton(kb[5])   
    btn7 = types.KeyboardButton(kb[6])
    btn8 = types.KeyboardButton(kb[7])
    btn9 = types.KeyboardButton(kb[8])
    btn10 = types.KeyboardButton(kb[9])
    btn11 = types.KeyboardButton(kb[10])
    btn12 = types.KeyboardButton(kb[11])
    btn13 = types.KeyboardButton(kb[12])   
    btn14 = types.KeyboardButton(kb[13])
    btn15 = types.KeyboardButton(kb[14])
    btn16 = types.KeyboardButton(kb[15])
    btn17 = types.KeyboardButton(kb[16])
    btn18 = types.KeyboardButton(kb[17])
    btn19 = types.KeyboardButton(kb[18])
    btn20 = types.KeyboardButton(kb[19])   
    btn21 = types.KeyboardButton(kb[20])
    btn22 = types.KeyboardButton(kb[21])
    markup.row(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    markup.row(btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)
    markup.row(btn16, btn17, btn18, btn19, btn20, btn21, btn22)
    return markup



# Печать предсказаний

def prediction(fs2, fs3, num_c):
# Печать предсказаний
  
# fs2 = 10 Развитие ситуации 
# fs2 = 20 Принять решение
# fs2 = 30 Взаимоотношения
# fs3 = 40 Что будет    
    
# fs3 = 10 Крест 
# fs3 = 20 План      

    print("prediction")
    
    if fs3 == 10:
        if num_c == 1:
            hi = "Смысл проблемы:"
        elif num_c == 2:
            hi = "Чего не следует делать:"
        elif num_c == 3:
            hi = "Что следует сделать:"
        elif fs2 == 4:
            hi = "Что получится, к чему это приведет:"
    elif fs3 == 20:
        if num_c == 1:
            hi = "Характер плана в целом:"
        elif num_c == 2:
            hi = "Основной мотив:"
        elif num_c == 3:
            hi = "Помехи или помощь извне:"
        elif fs2 == 4:
            hi = "Так точно не получится:"
        elif fs2 == 5:
            hi = "А так получится:"
            
    return hi


from keyboad_for_bot import read_fs
from keyboad_for_bot import read_fs_2
from keyboad_for_bot import read_fs_3

final_state = int(read_fs())
final_state_2 = int(read_fs_2())
final_state_3 = int(read_fs_3())
print("final_state=", final_state) 
print("final_state_2=", final_state_2) 
print("final_state_3=", final_state_3) 

  
#hi = prediction(final_state_2, final_state_3, 1)  
#print(hi)

    
    

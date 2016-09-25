# Генератор ихображений
from PIL import Image

def image_generator_cross(background, photo1, photo2, photo3, photo4):
    from PIL import Image
# Расклад крест 

    if photo1 != 0:
        img = Image.open('cards/'+photo1, 'r')
        offset = (0, 260)
        background.paste(img, offset)
        
    if photo2 != 0:
        img = Image.open('cards/'+photo2, 'r')
        offset = (300, 260)
        background.paste(img, offset)
        
    if photo3 != 0:
        img = Image.open('cards/'+photo3, 'r')
        offset = (150, 0)
        background.paste(img, offset) 
        
    if photo4 != 0:
        img = Image.open('cards/'+photo4, 'r')
        offset = (150, 520)
        background.paste(img, offset)
        
    background.save('out.png')
        

# background = Image.new('RGBA', (450, 780), (255, 255, 255, 255))
#image_generator_cross(background, 
#                         'rwjudgement.'+'jpg', 0, 0, 0)               
                        
def image_generator_plan(background, photo1, photo2, photo3, photo4, photo5):
    from PIL import Image
# Расклад план

    if photo1 != 0:
        img = Image.open('cards/'+photo1, 'r')
        offset = (150, 260)
        background.paste(img, offset)
        
    if photo2 != 0:
        img = Image.open('cards/'+photo2, 'r')
        offset = (0, 0)
        background.paste(img, offset)
        
    if photo3 != 0:
        img = Image.open('cards/'+photo3, 'r')
        offset = (300, 0)
        background.paste(img, offset) 
        
    if photo4 != 0:
        img = Image.open('cards/'+photo4, 'r')
        offset = (300, 520)
        background.paste(img, offset)
        
    if photo5 != 0:
        img = Image.open('cards/'+photo5, 'r')
        offset = (0, 520)
        background.paste(img, offset)
        
    background.save('out.png')
        

# background = Image.new('RGBA', (450, 780), (255, 255, 255, 255))
# image_generator_plan(background, 
#                     'rwjudgement.'+'jpg', 0, 0, 0, 0)

def prediction(taro_cards, fs2, fs3, num_c):
# Печать предсказаний
# fs2 = 10 Развитие ситуации 
# fs2 = 20 Принять решение
# fs2 = 30 Взаимоотношения
# fs2 = 40 Что будет    
# fs3 = 10 Крест 
# fs3 = 20 План      
    if fs3 == 10:
        if num_c == 1:
            hi = "Смысл проблемы:"
        elif num_c == 2:
            hi = "Чего не следует делать:"
        elif num_c == 3:
            hi = "Что следует сделать:"
        elif num_c == 4:
            hi = "Что получится, к чему это приведет:"
    elif fs3 == 20:
        if num_c == 1:
            hi = "Характер плана в целом:"
        elif num_c == 2:
            hi = "Основной мотив:"
        elif num_c == 3:
            hi = "Помехи или помощь извне:"
        elif num_c == 4:
            hi = "Так точно не получится:"
        elif num_c == 5:
            hi = "А так получится:" 
    return hi

def prediction_2(taro_cards, num_c):
# Печать значений карт
    from taro_value import arcans
    from taro_value import (Fool, Magician, High_Priestess, Empress, Emperor,
        Hierophant, Lovers, Chariot, Justice, Hermit, Wheel_off_Fortune, 
        Strength, Hanged_Man, Death, Temperance, Devil, Tower, 
        Star, Moon, Sun, Judgement, World)
    arcan = taro_cards[num_c]
    if arcan == 'Fool':
        return Fool[1][0]
    if arcan == 'Magician':
        return Magician[1][0]
    if arcan == 'High_Priestess':
        return High_Priestess[1][0]
    if arcan == 'Empress':
        return Empress[1][0]    
    if arcan == 'Emperor':
        return Emperor[1][0]
    if arcan == 'Hierophant':
        return Hierophant[1][0]
    if arcan == 'Lovers':
        return Lovers[1][0]
    if arcan == 'Chariot':
        return Chariot[1][0]
    if arcan == 'Justice':
        return Justice[1][0]
    if arcan == 'Hermit':
        return Hermit[1][0]
    if arcan == 'Wheel_off_Fortune':
        return Wheel_off_Fortune[1][0]
    if arcan == 'Strength':
        return Strength[1][0]
    if arcan == 'Hanged_Man':
        return Hanged_Man[1][0]
    if arcan == 'Death':
        return Death[1][0]
    if arcan == 'Temperance':
        return Temperance[1][0]
    if arcan == 'Devil':
        return Devil[1][0]
    if arcan == 'Tower':
        return Tower[1][0]
    if arcan == 'Devil':
        return Devil[1][0]
    if arcan == 'Star':
        return Star[1][0]
    if arcan == 'Moon':
        return Moon[1][0]        
    if arcan == 'Sun':
        return Sun[1][0]        
    if arcan == 'Judgement':
        return Judgement[1][0]        
    if arcan == "World":
        return World[1][0]        
        
        
# from keyboad_for_bot import read_taro
# taro_cards = read_taro()          # Читаем колоду    
# print(prediction_2(taro_cards, 1))



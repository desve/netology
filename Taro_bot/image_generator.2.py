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

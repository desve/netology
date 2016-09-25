# Генератор ихображений

def image_generator(photo1, photo2, photo3, photo4, var):
    from PIL import Image

    if photo1 != 0:
        img = Image.open('cards/'+photo1, 'r')
        img_w, img_h = img.size # ширина и высота изображение
        background = Image.new('RGBA', (img_w*3, img_h*3), (255, 255, 255, 255))
        bg_w, bg_h = background.size
        offset = (0, int((bg_h - img_h) / 2))
        background.paste(img, offset)
        offset = (int(bg_w - img_w), int((bg_h - img_h) / 2))
        background.paste(img, offset)
        
    if photo2 != 0:
        img = Image.open('cards/'+photo2, 'r')
        img_w, img_h = img.size # ширина и высота изображение
#        background = Image.new('RGBA', (img_w*3, img_h*3), (255, 255, 255, 255))
        bg_w, bg_h = background.size
        offset = (int(bg_w - img_w), int((bg_h - img_h) / 2))
        background.paste(img, offset)
        
    if photo3 != 0:
        img = Image.open('cards/'+photo3, 'r')
        img_w, img_h = img.size # ширина и высота изображение
#        background = Image.new('RGBA', (img_w*3, img_h*3), (255, 255, 255, 255))
        bg_w, bg_h = background.size
        offset = (int((bg_w - img_w) / 2), 0)
        background.paste(img, offset)
        
#    if photo4 != 0:
        img = Image.open('cards/'+photo4, 'r')
        img_w, img_h = img.size # ширина и высота изображение
#        background = Image.new('RGBA', (img_w*3, img_h*3), (255, 255, 255, 255))
        bg_w, bg_h = background.size
        offset = (int((bg_w - img_w) / 2), int(bg_h - img_h))
        background.paste(img, offset)
    
    background.save('out.png')

image_generator('rwjudgement.'+'jpg',
                'rwjudgement.'+'jpg',
                'rwjudgement.'+'jpg',
                'rwjudgement.'+'jpg', 1)
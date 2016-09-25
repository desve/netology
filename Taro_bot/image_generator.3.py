# Генератор ихображений

def image_generator(photo, cell):
    from PIL import Image

    img = Image.open('cards/'+photo, 'r')

# photo = open('cards/01.jpg', 'rb')
# tb.send_photo(message.chat.id, photo)

img_w, img_h = img.size # ширина и высота изображение

print(img_w, img_h)

#background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
background = Image.new('RGBA', (img_w*3, img_h*3), (255, 255, 255, 255))

bg_w, bg_h = background.size

print(bg_w, bg_h)

offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2))

print(offset)

background.paste(img, offset)

background.save('out.png')
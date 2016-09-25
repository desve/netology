def binary_to_dictionary(binary):
# binary = b'[{...}}]'

    b1 = binary.decode('UTF-8') # декодируем
    b2 = b1[1:]                 # удаляем первый символ
    b3 = b2[:-1]                # удаляем последний символ

    return eval(b3)             # преобразуем в словарь

d = b'[{"faceRectangle":{"height":426,"left":242,"top":391,"width":426},"scores":{"anger":7.253733E-05,"contempt":0.005009529,"disgust":9.923835E-05,"fear":5.30315765E-06,"happiness":0.213434368,"neutral":0.7774695,"sadness":0.0037772425,"surprise":0.00013225642}}]'
print(d)
print(binary_to_dictionary(d))


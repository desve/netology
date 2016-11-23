# my_string = 'Www.HackerRank.com'

my_string = input()

new_string = ''
for symbol in my_string:
    if ord(symbol) >= 65 and ord(symbol) <= 90:
        new_string += chr(ord(symbol) + 32)
    elif ord(symbol) >= 97 and ord(symbol) <= 122:
        new_string += chr(ord(symbol) - 32)
    elif ord(symbol) < 65:
        new_string += symbol
print(new_string)
        
"""   
ord(символ)	Символ в его код ASCII
chr(число)	Код ASCII в символ
"""

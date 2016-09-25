# Две половинки

import math

print("Введите строку")
s = str( input())
l = math.ceil( len(s) / 2)
s1 = s[:l]
s2 = s[l:]
print("Новая строка", s2+s1)

# Удалить каждый третий символ

print("Введите строку")
s = str( input())

n = len(s)
s_new = ""

for i in range(n):
    if i % 3 != 0:
        s_new = s_new + s[i]
    else:
        s_new = s_new
        
print("Искомая строка", s_new)
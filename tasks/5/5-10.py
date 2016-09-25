# Удаление символа

print("Введите строку")
s = str( input())

s_new = ""
n = len(s)

for i in range(n):
    if s[i] != "@":
        s_new = s_new + s[i]
    else:
        s_new = s_new
  
print("Искомая строка", s_new)
    
    
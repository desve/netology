# Замена внутри фрагмента

print("Введите строку")
s = str( input())

s_new = ""
n = len(s)

for i in range(n):
    if s[i] != "h":
        s_new = s_new + s[i]
    elif s[i] == "h" and i == s.find("h"):
        s_new = s_new + "h"
    elif s[i] == "h" and i == s.rfind("h"):
        s_new = s_new + "h"
    else:
        s_new = s_new + "H"
        
print("Искомая строка", s_new)
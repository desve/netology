# Первое и последнее вхождеие

print("Введите строку")
s = str( input())

if s.count("f") == 1:
    print(s.find("f"))
elif s.count("f") >= 2:
    print(s.find("f"))
    print(s.rfind("f"))
else:
# Ни чего не выводим  
    ok = 1
 
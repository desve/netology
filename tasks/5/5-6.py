# Второе вхождение

print("Введите строку")
s = str( input())

if s.count("f") == 0:
    print("-2")
elif s.count("f") == 1:
    print("-1")
else:
    l1 = s.find("f")
    s1 = s[:l1+1]
    s2 = s[l1+1:]
    l2 = s2.find("f")
    print("Второе вхождение", l1+l2+1)
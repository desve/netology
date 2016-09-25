# Обращение фрагмента

print("Введите строку")
s = str( input())

l1 = s.find("h")
l2 = s.rfind("h")
s1 = s[:l1+1]
s2 = s[l2:]
s3 = s[l1+1:l2]
s33 = s3[::-1]

print("Искомая строка", s1+s33+s2)
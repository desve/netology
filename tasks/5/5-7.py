# Удаление фрагмента

print("Введите строку")
s = str( input())

l1 = s.find("h")
l2 = s.rfind("h")
s1= s[:l1]
s2 = s[l2+1:]
print("Итоговая строка", s1+s2)


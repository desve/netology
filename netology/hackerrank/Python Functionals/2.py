"""
l = list(range(10))
print(l)
l = list(map(lambda x:x*x, l))
print(l)

l = list(filter(lambda x: x > 10 and x < 80, l))
print(l)
"""

"""
N = int(input())
l = []
for n in range(N):
    l.append(input())
"""
l = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

# Проверка @
l = list(filter(lambda l: l.count('@') == 1, l))

# Проверка имени
# l = list(filter(lambda l: l.split('@')[1].isalnum() == True, l))

print(l[0].split('@')[1])

    
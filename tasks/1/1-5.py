# Дележ яблок
# n - количество школьников
# k - количество яблок

print("Привет! Сколько всего школьников?")
n = int( input() )
print("А сколько всего яблок?")
k = int( input())
a1 = k // n         #по столько яблок получит каждый
a2 = k % n          #останется в корзине

print("Каждый школьник получит по", a1, "яблок")
print("При этом в корзине останется", a2, "неразделенных яблок")

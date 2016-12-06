from itertools import product

a = input()
b = input()

a_to_list = list(map(int, list(a.split())))
b_to_list = list(map(int, list(b.split())))

c = list(product(a_to_list, b_to_list))

print(" ".join(map(str, c)))



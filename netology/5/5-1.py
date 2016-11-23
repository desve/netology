N = 5
print_string = 0
for n in range(1, N + 1):
    print_string += n * (10**(N-n))
    
print(print_string)

squares = list(map(lambda x: x * x, [0, 1, 2, 3, 4]))
print(squares)
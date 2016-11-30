N = 5
fib = (lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1)

# f = lambda x: 1 if x>0 else 0 if x ==0 else -1


numbers = []
print(numbers)
for n in range(N+1):
    if n == 0:
        numbers.append(0)
        print(numbers)
    elif n> 0:
        numbers.append(fib(n))
        print(numbers)
    
print(numbers)

fib_3 = list(map(lambda x: x**3, numbers))
print(fib_3)


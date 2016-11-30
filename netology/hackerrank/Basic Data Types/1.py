# N = 5
# input_string = '9 4 7 9 9 8'

N = int(input())
input_string = input()

A = []

list_line = list(input_string.split(" "))
A = [int(item) for item in list_line]

max_item = max(A)

for item in range(A.count(max_item)):       
    A.remove(max_item)

print(max(A))




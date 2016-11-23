from itertools import permutations

input_string = list(input().split())

new_line = list(permutations(str(input_string[0]), int(input_string[1])))
new_line.sort()

for line in range(len(new_line)):
    print(str(new_line[line][0]) + str(new_line[line][1]))
    

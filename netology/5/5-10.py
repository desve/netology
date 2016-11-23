number_of_elements = int(input())
input_elements = input()

input_elements = input_elements.split(" ")

input_elements_list = []
for element in range(number_of_elements):
    input_elements_list.append(int(input_elements[element]))

new_tuple = tuple(input_elements_list)

print(hash(new_tuple))

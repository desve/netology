my_string = input()
input_string = input()

string_to_list = list(input_string)

number_in_string = string_to_list[0]
symbol_in_string = string_to_list[2]


my_list_string = list(my_string)

my_list_string[int(number_in_string)] = symbol_in_string
new_string = ''.join(my_list_string)

print(new_string)
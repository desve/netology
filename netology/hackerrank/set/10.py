set_basic_list = list(map(int, input().split()))
set_basic = set(set_basic_list)
number_sets = int(input())

set_additional = set()
a = set()
for set_base in range(number_sets):
    a_list = list(map(int, input().split()))
    a = set(a_list)
    set_additional.update(a)

print(set_basic <= set_additional)

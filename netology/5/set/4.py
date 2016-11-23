m = int(input())
s_m = set(map(int, input().split()))

n = int(input())
s_n = set(map(int, input().split())) 

symmetric_difference = {}

symmetric_difference = s_m.symmetric_difference(s_n)

answer = list(symmetric_difference)

print(answer)
answer.sort()
print(answer)

for element in answer:
    print(int(element))

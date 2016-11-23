n = int(input())
s = set(map(int, input().split())) 

print('%0.3f' % (sum(list(s)) / len(list(s))))

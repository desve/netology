
# l = [[1, 7], [3, 4, 5]]
# l = [1, 7, 3, 4, 5]
l = ['wghg', 'kjhgf', '2', '33', 'mnbvc']


l = list(filter(lambda x: len(x) < 4, l))

print(l)
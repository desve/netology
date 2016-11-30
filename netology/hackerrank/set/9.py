# number = int(input())
# number_rooms = list(map(int, input().split()))
# number_rooms = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2] 

for room in number_rooms:
    if number_rooms.count(room) == 1:
        print(room)


"""
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""


# N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.

N  = 7
M = 21
for i in range(1, int(N/2) + 1 , 1): 
    print('-' * (4-i)* 3, '.|.' * (i + (i-1)), '-' * (4-i) * 3)
print('-' * int(((M - 7) /2)), 'WELCOME', '-' * int(((M - 7) /2)))
for i in range(N,-1,-2): 
    print('-' * (4-i)* 3, '.|.' * (i + (i-1)) * (N - (i-1)), '-' * (4-i) * 3)



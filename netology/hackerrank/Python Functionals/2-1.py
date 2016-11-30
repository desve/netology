# N = int(input())
# email = []

N = 3
emails = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

# for n in range(N):
#     email.append(input())

import re


email_regex = re.compile(r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z]{1,3}$')

print(sorted(filter(lambda email: re.match(email_regex, email), emails)))
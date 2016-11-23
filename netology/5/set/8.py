number_english = int(input())
roll_numbers_english = set(map(int, input().split()))

number_french = int(input())
roll_numbers_franch = set(map(int, input().split()))


print(len(roll_numbers_english.symmetric_difference(roll_numbers_franch)))
import calendar

# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

current_date = input()

current_date = current_date.split(" ")
print(current_date)


month = current_date[0]
day = current_date[1]
year = current_date[2]

print(month, day, year)

print(calendar.TextCalendar(firstweekday=6).formatyear(2015)

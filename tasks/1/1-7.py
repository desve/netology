# Электронные часы
# n - количество минут
# hour - количество часов
# min - количество минут

print("Привет! Сколько минут прошло с начала дня?")
n = int( input ())
hour = n // 60          # получаем количество часов
min = n % 60            # количество минут

print("Текущее время", hour, ":", min)


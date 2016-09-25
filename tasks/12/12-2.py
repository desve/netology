# Вывод в файл

fout = open("input.txt", "w")    # w - write

print("Пишем в файл input.txt", file = fout)

fout.close
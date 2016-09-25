# Ввод-вывод в ситуации, когда количество строк неизвестно

from sys import stdin

stdin = open("input.txt", "r")

a = stdin.readlines()

print(a)
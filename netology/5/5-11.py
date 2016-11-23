# N = int(input())
N = 2

indent = len(str(bin(N)[2:]))

space = ' '

for number in range(1, N + 1):
    indent_decimal = indent - len(str(number))
    indent_octal  = indent - len(str(oct(number))[2:])
    indent_hexadecimal = indent - len(str(hex(number))[2:])
    indent_binary = indent - len(str(bin(number))[2:])
    print(space * indent_decimal, number, \
          space * indent_octal, str(oct(number))[2:], \
          space * indent_hexadecimal, str(hex(number))[2:], \
          space * indent_binary, str(bin(number))[2:]
         )


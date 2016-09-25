# Большие буквы

print("Введите строку")
s = str( input())

def capitalize(s):
    s1 = ord(s[0])
    s2 = chr(s1 - 32)
    _s = s[1:]
    s = s2 + _s
    n = len(s)
    for i in range(n):
        s_ = s[i]
        if s_ == " ":
            _s1 = s[:i+1]
            _s2 = s[i+2:]
            s1 = ord(s[i+1])
            s2 = chr(s1 - 32)
            s = _s1 + s2 + _s2
    return s
            
print(capitalize(s))


    
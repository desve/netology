s = ['gfhcvjkbb__jfg.sql', 'gfhcvjb__jfg.sql', 'gfhcvjkb__jfg.txt']

# print(s.rfind(str, [start],[end]))

print(s)

s = list(filter(lambda s: s.rfind('.sql', len(s)-4, len(s)) > 0, s))

print(s)

# https://tproger.ru/translations/regular-expression-python/

import re
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result.group(0))

# result = re.match(r'Analytics', 'AV Analytics Vidhya AV')
# print(result)

print(result.start())
print(result.end())

result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print(result.group(0))

result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print(result)

result = re.split(r'y', 'Analytics')
print(result)
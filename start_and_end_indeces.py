import re

S = str(input())
k = str(input())

regex = re.escape(k)

iterator = re.finditer(regex, S)

for match in iterator:
    print(match.span())
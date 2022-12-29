import re

string = input('Please enter the text : ')

pattern = input('Please enter the pattern : ')

substrings = re.finditer(rf"{pattern}", string)

for i in substrings:
    print(i.group(), end='')
    print(i.span())

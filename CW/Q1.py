import re

string = input('Please enter the text : ')

pattern = input('Please enter the pattern : ')

substrings = re.findall(rf"{pattern}", string)

print(substrings)

import re

string = input("Enter your string ---->")

numbers = re.finditer("\d+", string)

for num in numbers:
    print(f"number ===> {num.group()} - position ===> {num.span()}")

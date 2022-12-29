import re

string = input("Enter your string ---->")
b = re.findall(r"\b[ae][A-z]+\b", string)
print("Your list of words starting with a or e is --->", b)

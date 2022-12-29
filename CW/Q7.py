import re

string = input("Enter your string ---> ")
b = re.findall(r"\d+", string)
print("The numbers of given string are --->", "-".join(b))

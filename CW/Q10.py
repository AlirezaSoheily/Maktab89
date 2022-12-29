import re

string = input("Enter your string ---->")
string = re.sub("Road", "Rd.", string)
print(string)

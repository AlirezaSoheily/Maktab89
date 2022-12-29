import re

string = input('Please enter the text : ')

string = re.sub(" ", "~" , string)
string = re.sub("_", " " , string)
string = re.sub("~", "_" , string)
print(string)
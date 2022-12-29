import re

url = input("URL : ")
date = re.findall(r"\d{4}[/:-]\d{1,2}[/:-]\d{1,2}", url)
print(date)

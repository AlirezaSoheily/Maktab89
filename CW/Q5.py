import re

url = input("Date in yyyy-mm-dd format : ")

date = re.sub(r"(\d{4})[/:-](\d{1,2})[/:-](\d{1,2})", "\\3-\\2-\\1", url)

print(date)

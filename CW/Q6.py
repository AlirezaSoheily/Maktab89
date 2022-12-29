import re

words_list = input("Enter your words list---->").split(" ")
new_list = []
for words in words_list:
    check_true = re.match("(P[A-z]+)", words)
    if check_true:
        new_list.append(check_true.group())
if len(new_list) == 2:
    print("True!")
    print(new_list)
else:
    print(f"False---->there is {len(new_list)} words starting P in this list!!!")


import re
s=input("Enter the string")
patterns = '\w+\S*$'
if re.search(patterns,  s):
    print('Found word at the end')
else:
    print('Not Found!')
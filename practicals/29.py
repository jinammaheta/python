import re
s="This is a string apple banana mango cricket all people loves it"
t=s.split(" ")
l=[]
for i in t:

    if re.search("^[a][A-Za-z0-9_]*",i):
        l.append(i)
print(l)
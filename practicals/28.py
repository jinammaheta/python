import os
f=open("sample","rt")
l=0
w=0
c=0
while True:
    t=f.readline()
    t=t.replace("\n","")
    if t=="":
        break
    l+=1
    t=t.split(" ")
    print(t)
    w+=len(t)
    for e in t:
        c+=len(e)
        print(e)
    print(c)
print(l,w,c)
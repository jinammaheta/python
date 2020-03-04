l1=list(input("Enter the key List\n").split(" "))
l2=list(input("Enter the value List\n").split(" "))
l3=list(zip(l1,l2))
d={}
for k,v in l3:
    d[k]=v
print(d)
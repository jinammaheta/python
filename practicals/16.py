l=list(map(int,input("Enter the elements\n").split(" ")))
change=True
n=len(l)
while change:
    change=False
    for i in range(0,n-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            change=True
    n-=1
print(l)
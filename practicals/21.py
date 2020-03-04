def countE(l,e):
    count=0
    for i in l:
        if i==e:
            count+=1
    return count
l=list(map(int,input("Enter the List elements\n").split(" ")))
e=int(input("Enter the element that you want find\n"))
count=countE(l,e)
print(count)
n=int(input("Size of the matrices\n"))
a=[[0]*n]*n
b=[[0]*n]*n
c=[]
print("Enter the elements of first matrix:")
for i in range(0,n):
    print("{}th Row:".format(i+1))
    a[i]=list(map(int,input().split(" ")))
print("Enter the elements of second matrix:")
for i in range(0,n):
    print("{}th Row:".format(i+1))
    b[i]=list(map(int,input().split(" ")))
for i in range(0,n):
    temp=[]
    for j in range(0,n):
        p=0
        for k in range(0,n):
            p+=a[i][k]*b[k][j]
        temp.append(p)
    c.append(temp)
print(c)
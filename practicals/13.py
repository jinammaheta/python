n=int(input("Enter the Number to check prime or not\n"))
flag=0
for i in range(2,int(n/2+1)):
    if n%i==0:
        flag=1
        break
if n == 1:
    print("Number is special number")
elif flag==0:
    print("Number is prime")
else:
    print("Number is not prime")

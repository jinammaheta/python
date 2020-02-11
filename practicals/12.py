n=int(input("Enter the Number\n"))
i=1
fact=1
while i<=n:
    fact*=i
    i+=1
print("Factorial of the given number is:{}".format(fact))
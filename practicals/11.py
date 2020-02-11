import math
a,b,c=map(int,input("Enter Coefficients a,b,c\n").split())
d=(b*b)-(4*a*c)
if d==0:
    print("Both roots are same")
    r=-b/2*a
    print("Root is:r={}".format(r))
if d<0:
    print("No Roots")
if d>0:
    r1=(-b+math.sqrt(d))/2*a
    r2=(-b-math.sqrt(d))/2*a
    print("Roots are:r1={} , r2={}".format(r1,r2))

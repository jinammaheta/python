t=((2,1,3),(20,19,33,4),(-5,5,0,-6))
t=list(t)
for i in range(len(t)):
    j=t[i]
    j=list(j)
    t[i]=tuple(sorted(j))
t=tuple(t)
print(t)

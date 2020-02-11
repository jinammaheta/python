l=[1,2,3,4,5,9,344,-4,328,44,5,3]
e=int(input("Enter The element to be searched\n"))
try:
    pos=l.index(e)

except ValueError:
    print("The Element is not present in the list")
else:
    print("The element is present at position no. {}".format(pos + 1))
    
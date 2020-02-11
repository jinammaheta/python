s="I am Devloper"
sub=input("Enter The subString\n")
p=int(input("Enter The pos\n"))
news=s[:p]+sub+s[p:]
print("New String is:{}".format(news))
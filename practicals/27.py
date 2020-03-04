try:
    n=int(input("Enter the numerator\n"))
    d=int(input("Enter the denominator\n"))
    result=n/d
    print(result)
except ZeroDivisionError as e:
    print("Exception", str(e))
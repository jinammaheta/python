class A:
    def __init__(self,d):
        self.d=d
    def __gt__(self, other):
        return self.d>other.d
ob1=A(3)
ob2=A(5)
print(ob1>ob2)
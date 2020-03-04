class Bank(object):
    def __init__(self,openamount):
        self.balance=openamount
    def withdraw(self,amount):
        if amount <100:
            print("Soory this amount can not be withdrawn")
            return
        if self.balance>amount:
            self.balance-=amount
            print(f"{amount} has been withdrawn successfully")
            self.showcash()
        else:
            print("Enough amount is not available")
    def deposit(self,amount):
        if amount <100:
            print("Sorry this amount can not be deposited")
            return
        self.balance+=amount
        self.showcash()
    def showcash(self):
        print(f"Your current balance is {self.balance}")
amount=int(input("Enter the basic amount\n"))
b1=Bank(amount)
print("1 for withdrawal\n2 for deposit\n3 for Balance inquiry\n4 for exit ")
c=int(input())
while True:
    if c==1:
        amount = int(input("Enter your amount to withdrawn\n"))
        b1.withdraw(amount)
    elif c==2:
        amount = int(input("Enter your amount to be deposited\n"))
        b1.deposit(amount)
    elif c==3:
        b1.showcash()
    elif c==4:
        break
    else:
        print("Enter Valid choice")
    c = int(input("Enter your choice\n"))

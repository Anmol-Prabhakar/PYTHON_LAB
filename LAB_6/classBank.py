class bankacc:
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        self.balance +=amount
        print(f"deposited amount ${amount},New balance = ${self.balance}")

    def withdraw(self,amount):
        if(amount>self.balance):
           print("insufficient balance")
        else:
               self.balance-=amount
               print(f"${amount} withdrawn , New balance is ${self.balance}")

    def check(self):
        print(f"current balance is ${self.balance}")


account  = bankacc()
account.deposit(500)
account.withdraw(200)
account.check()
        
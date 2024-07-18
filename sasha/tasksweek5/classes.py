class Account:
    def __init__(self, title=None, balance=None):
        # write your code here
        self.title = title
        self.balance = balance

    def getbalance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdrawal(self,amount):
        self.balance -= amount
        


class SavingsAccount(Account):
    def __init__(self, title=None, balance=None, interestRate=None):
        # write your code here
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.interestRate * self.balance)//100
        

st = Account('Timka',5000)
st.deposit(400)
print(st.balance)
st.withdrawal(400)
print(st.balance)
st2 = SavingsAccount('Maska',2000,5)
print(st2.interestAmount())

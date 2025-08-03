# create Acccunt class with 2 atributes - balance & accont no
# create method for debit credit printing the balance
class Account:
    def __init__(self , Accountno , balance):
      self.AccountNo = Accountno
      self.Balance = balance
    def debit(self , amount):
          self.Balance =-amount 
          print(f"Rs{amount} was credited from your account")  
          print(f"Total balance is:{self.remain_balance}")  
    def credit(self , amount):
      self.Balance =+ amount   
      print(f"Rs{amount} was debited in your account")
      print(f"Total balance is:{self.remain_balance}") 
    def remain_balance(self):
        return self.balance
        
acc1 = Account(444444 , 4000)
acc1.debit(300)
acc1.credit(300)
    
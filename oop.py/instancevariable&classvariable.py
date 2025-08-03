class Employee:
  raise_amount = 0.03 #class variable-it associate from class
  def __init__(self, name):
    self.name = name
    # instance variable - it associate instantly
  def showdetails(self):
    print(f"The name of the Employee is:{self.name} and raise amount is:{self.raise_amount}")

emp1 = Employee("Krish")
emp1.raise_amount = 0.05 # in that case will be assocaite instantly not classly
emp1.showdetails()
emp2 = Employee("Rohan")
emp2.showdetails()
# emp1.raise_amount = 0.3
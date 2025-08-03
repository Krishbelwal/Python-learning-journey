# Multiple inhritance- it is used to inherit properties and methods from differnt parent classes . it is useful when we want to inherit differnt functanilites from multiple sources.
class Employee: # Base/parent class 
    def __init__(self , name):
        self.name = name
class Dancer: # Base/parent class 
    def __init__(self , dance):
        self.dance = dance
class Employeedance(Employee , Dancer): # Derived class 
    def __init__(self , name , dance):
         self.name = name
         self.dance = dance
    def Number(self , Number):
        self.Number = Number
    def print(self):
         print(f"The Employee name is:{self.name} and her dance is:{self.dance} and her phone number is:{self.Number}")
a = Employeedance("Ritika" , "kathak")
a.Number(8650131532)
a.print()
#  MRO method-
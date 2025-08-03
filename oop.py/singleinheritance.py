# single inheritance- when a class inherit properites and methods from a single parent class.
class student:
       def __init__(self , Name , id):
          self.name = Name
          self.id = id
       def print(self):
        print(f"The Name is: {self.name} and his id is: {self.id}")
class programmmer(student):
       def rollno(self , no):
            self.rollno = no
            print(f" and his roll no. is:{self.rollno}")
b = programmmer("krish" , 456)
b.print()
b.rollno(45)
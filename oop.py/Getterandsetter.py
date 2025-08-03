# setter -it allow you to set or update the value of a private variable 
class Student:
   def __init__(self, a):
     self._Name = a # it is a private variable
   def set_Name(self, New_Name): #setter
     if(len(self._Name)>=5):
       self._Name = New_Name
     else:
       print("invalid name")   
   def get_Name(self):#getter
      print(f"The name is:{self._Name}")
a = Student("Krishna")
a.set_Name("Ram")
a.get_Name()

# Getter- it is used to access the atributes of an object.
# class Student:
#     # __slots__ = ["__name"] # for getting error 
#     def __init__(self, Name):
#       self.__name = Name
#     def print(self):
#        print(f" The name is:{self.__name}")
# a = Student("krish")
# a.name = "Ram" 
# a.print()
# print(a._Student__name)


# Ex - 
class Book:
    def __init__(self , Title , author , year):
        self.title = Title
        self._author = author
        self.year = year
    def set_author(self, pin):
           if(pin==1234):
              return "The author is:{self._author}"
           else:
              print("invalid pin")
    def isclassic(self):
        if(self.year <=2000):
            print("This is classic book ")
        else:
            print("This is modern book")
    def display_info(self):
        print(f"The Book title is:{self.title}and The Book year is:{self.year}")
year = int(input("Enter the year:"))
a = Book("Atomic habbit" , "james clear" , year)
a.set_author(1234)
a.display_info()
a.isclassic()
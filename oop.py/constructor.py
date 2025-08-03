# constructor is a special type of method used to initalize an object of a class . it invoked autamatically when an object is created.
# self - it is a refernce of current instance of the class. it is used to acess object of the class.
# class person:
    # name = "Krish"
    # occupation = "Ai Engineear"
    # networth = 1000000
#     def info(self):
#      print(f"{self.name} is a {self.occupation}")
# a = person()
# a.name = "Mohan"
# a.info()

# Ex1-
# class student:
#  def __init__(self, name , grade):
#    self.Name = name
#    self.Grade = grade
#  def set_grade(self,pin):
#     if pin == 1234:
#       return self.Grade
#  def print(self):
#    print(f"The name is:{self.Name}")
# a = student("Krish" , "A+")
# a.print()
# print(a.set_grade(1234))

# Ex2-
# class Car:
#     def __init__(self , name , brand , modal , color ):
#         self.Name = name
#         self.brand = brand
#         self.modal= modal
#         self.color = color
#     def set_name(self ,n):
#         if n=="Tata":
#             return self.Name
#         else:
#            return "Error"
#     def print(self):
#         if self.Name == "Tata":
#           print(f"The car name is:{self.Name} and The car brand is:{self.brand} and modal is:{self.modal} and color is:{self.color}")
#         else:
#            print("car Name is not availble")
# a = Car("Harrier" , "Harrier23" , "Harrier1978" , "black")
# a.set_name("Tata")
# a.print()

# Ex 3-
# class Book:
    # def __init__(self , Title , author , year):
    #     self.title = Title
    #     self.author = author
    #     self.year = year
#     def isclassic(self):
#         if(self.year <=2000):
#             print("This is classic book ")
#         else:
#             print("This is modern book")
#     def display_info(self):
#         print(f"The Book title is:{self.title} and the Book author is:{self.author} and The Book year is:{self.year}")
# year = int(input("Enter the year:"))
# a = Book("Atomic habbit" , "james clear" , year)
# a.display_info()
# a.isclassic()

# Ex - 4
# create an report card of an student-
# print("Report card of an student")
# class student:
#  def __init__(self , Name , roll_number , Marks1 , Marks2 , Marks3 , Marks4):
#     self.name = Name
#     self.roll_no = roll_number
#     self.Marks1 = Marks1
#     self.Marks2 = Marks2
#     self.Marks3 = Marks3
#     self.Marks4 = Marks4
#  def displaystudentinfo(self):
#    print(f"The student Name is:{self.name} and his roll_number is:{self.roll_no} and his Hindi Marks is:{self.Marks1} and his English Marks is:{self.Marks2} and his Math Marks is:{self.Marks3} and his science Marks is:{self.Marks4}")
#  def calculate(self):
#      Total = Marks1+Marks2+Marks3+Marks4
#      if(Total>=250):
#         print("student passed")
#         print("very good")
#      else:
#         print("student failed")
#         print("you need some more improvement")
# Name = input("Enter the student Name:")
# roll_no = int(input("Enter the roll_no:"))
# Marks1 = int(input("Enter the Marks of Hindi:"))
# Marks2 = int(input("Enter the Marks of English:"))
# Marks3 = int(input("Enter the Marks of Math:"))
# Marks4 = int(input("Enter the Marks of science:"))
# s1 = student(Name , roll_no , Marks1 , Marks2 , Marks3 , Marks4)
# s1.displaystudentinfo()
# s1.calculate()

# Name = input("Enter the student Name:")
# roll_no = int(input("Enter the roll_no:"))
# Marks1 = int(input("Enter the Marks of Hindi:"))
# Marks2 = int(input("Enter the Marks of English:"))
# Marks3 = int(input("Enter the Marks of Math:"))
# Marks4 = int(input("Enter the Marks of science:"))
# s2 = student(Name , roll_no , Marks1 , Marks2 , Marks3 , Marks4)
# s2.displaystudentinfo()
# s2.calculate()

# Name = input("Enter the student Name:")
# roll_no = int(input("Enter the roll_no:"))
# Marks1 = int(input("Enter the Marks of Hindi:"))
# Marks2 = int(input("Enter the Marks of English:"))
# Marks3 = int(input("Enter the Marks of Math:"))
# Marks4 = int(input("Enter the Marks of science:"))
# s3 = student(Name , roll_no , Marks1 , Marks2 , Marks3 , Marks4)
# s3.displaystudentinfo()
# s3.calculate()

# Name = input("Enter the student Name:")
# roll_no = int(input("Enter the roll_no:"))
# Marks1 = int(input("Enter the Marks of Hindi:"))
# Marks2 = int(input("Enter the Marks of English:"))
# Marks3 = int(input("Enter the Marks of Math:"))
# Marks4 = int(input("Enter the Marks of science:"))
# s4 = student(Name , roll_no , Marks1 , Marks2 , Marks3 , Marks4)
# s4.displaystudentinfo()
# s4.calculate()

# Name = input("Enter the student Name:")
# roll_no = int(input("Enter the roll_no:"))
# Marks1 = int(input("Enter the Marks of Hindi:"))
# Marks2 = int(input("Enter the Marks of English:"))
# Marks3 = int(input("Enter the Marks of Math:"))
# Marks4 = int(input("Enter the Marks of science:"))
# s5 = student(Name , roll_no , Marks1 , Marks2 , Marks3 , Marks4)
# s5.displaystudentinfo()
# s5.calculate()

# 5- Apna college-
# class student:
#   def __init__(self , full_name , Marks):
#     self.full_name = full_name
#     self.marks = Marks

# Methods -
#   def welcome(self):
#       print("welcome " , self.full_name)
#   def get_marks(self):
#         return self.full_name
# a = student("krish" , 88)
# print(a.full_name , a.marks)
# a.welcome()
# print(a.get_marks())
# b = student("Mohan" , 76)
# print(b.full_name , b.marks)

# types -
# 2- Default-  if constructor doesn't accept any paremeters execpt self, it is known as  Default constructor.
# def __init__(self):
#   print("Hello")
# 1- paremeterized - if constructor accept paremeters along with a self, it is known as paremeterized  constructor.

# Ex-
class student:
      def __init__(self , Name , Marks1 , Marks2 , Marks3):
            self.name = Name
            self.marks1 = Marks1
            self.marks2 = Marks2
            self.marks3 = Marks3
      def averge(self):
            avg = (self.marks1 + self.marks2 + self.marks3)/3
            print(f"{self.name} averge is:" , int(avg))
            if(avg>=60):
                  print("student passed")
            else:
                  print("student failed")
student1 = student("Mohan" , 67 , 56 , 38)
student1.averge()
student2= student("Krish" , 87 , 96 , 98)
student2.averge()
student3= student("Ram" , 37 , 46 , 78)
student3.averge()


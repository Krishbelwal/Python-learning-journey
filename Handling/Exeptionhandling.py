# holt
# Exception in python-  
# Name - it returns when we acess a wrong name
# index - it returns when we acess a wrong index which doesn't exist in any itreable objects
# Atribute 
# type - when an operation performed with an invalid types 
# value - when the value is invalid
# Key 


# Atribute error Ex- 
# try:
#  l = [1 , 3 , 4 , 5 ]
#  ans = l.age()
# except AttributeError:
#   print(f"Error! You are acessing wrong atribute")
# ValueError -
# try:
#  a = int(input("Enter a Num: "))
#  Num = [1, 3, 4, 5]
#  print(Num)
# except ValueError:
    # print("Number entered is not an integer please check the code .")

# NameError -
# try:
#  a = int(input("Enter the Num:"))
#  b = int(input("Enter the Num:"))
#  print(a + c)

# except NameError:
#     print("it's a Name error. please check the code.")

# IndexError-
# list = [1,3,5,6,7,8]
# try:
#     print(list[123])
# except IndexError:
#     print("index out of range , please check the code")


#ZeroDivisionError
# try:
#     a = 10
#     b = 0
#     result = a/b
#     print(result)
# except ZeroDivisionError:
#     print("Error: cannot be divided")-

# typeerror-
# try:
#  a = int(input("Enter the Num:"))
#  b = int(input("Enter the Num:"))
#  print(a + str(b))
# except TypeError:
#  print("it's a type error")


# finally- it is used in exeption handling to define a block of code that will be always execcute , Even wheather a program return or not.
# def fun1():
#   try:
#    l =[1,9, 4,5,7]
#    i  = int(input("Enter the Index:"))
#    print(l[i])
#    return 1
#   except ValueError:
#     print("Entered  Number is not an integer. please check the code .")
#   except IndexError:
#     print(" it's an index error. please check the code")
  # finally:  # if i want to print 
  #   print("End of program")
#   print("End of program")
# x =  fun1()
# print(x)

# def num():
#  try:
#      a = int(input("Enter the Num:"))
#      result = a/0
#      return 1
#  except ZeroDivisionError:
#     print("caught a ZeroDivisionError")
# a = num()
# print("End of program")
 
# Raise coustom errors-
a = int(input("Enter the any Number between 5 and 9:"))
if(a<5 or a>9):
    raise ValueError("Error occurred! value should be between 5 and 9 . Please Try again.")

# Ex- 
def check_age(age):
    if(age<=0):
        raise ValueError("Age cannot be negative. please Enter valid age")
    elif(age>18):
          print("yes! you are applicable for using this App")
    elif(age<18):
          print("you are Not applicable for using this App")
    else:
        print("The age is:" , age)
check_age(34)

# def check_name(Name):
#        if isinstance(Name , int):
#             raise TypeError("Name must be a string")
#        print(Name , "Belwal")
# # check_name(12344)
# check_name("Krishna")

# small project - 
# try:
#  a = int(input("Enter the Num:"))
#  b = int(input("Enter the Num:"))
#  opr = input("Enter the Num:")
#  if opr == "+":
#       print(a + b )
#  if opr == "-":
#       print(a + b )
#  if opr == "*":
#       print(a * b )
#  if opr == "/":
#   print(a / b )
  
# except ValueError:
#       print("wrong values")
# except ZeroDivisionError:
#       print("wrong values divided")
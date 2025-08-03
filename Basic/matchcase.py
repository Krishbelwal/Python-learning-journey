# x =int(input("Enter the number of x:"))

# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("case is 4")
#     case 10 if(x<34):
#         print("case is 10")
#     case 10 if(x<44):
#         print("case is 10")
#     case _ if(x!=50):
#        print(x)
#     case _ if x!=70:
#         print("No acess")
#     case _ if x!=30:
#         print("No acess")

# Example-

# a =(input("Enter the light:")
# match a:
#     case "red":
#         print("stop")
#     case "green":
#         print("go")
#     case "yellow":
#         print("slow down")
#     case _:
#          print("invalid light")

# a = (input("enter the light:"))
# match a:
#     case "red":
#         print("stop")
#     case "green":
#         print("go")
#     case "yellow":
#         print("slow down")
#     case _:
#         print("invlaid light ")
        


# a =int(input("Enter the Marks:"))
# match a:
    # case _ if(a==100):
    #     print(" passed and Excellent")
    # case _ if(a<100 and a>=33):
#         print("passed")
#     case _ if(a<33 and a>0):
#         print("failed")
#     case _:
#         print('invalid number')

# Ticket price-
# age = int(input("Enter the Age:"))
# match age:
#     case _ if(age<=5 and age >=0):
#         print("Free Entry")
#     case _ if(age>5 and age<=18):
#         print("50")
#     case _ if(age>18 and age <=70):
#         print("100")
#     case _ if(age>50 and age<100):
#         print("Free Entry")
#     case _ :
#         print("Please Enter valid age")

age = int(input("Enter your Age:"))
match age:
    case _ if(age<=5 and age >=0):
        print("No charge")
    case _ if(age>5 and age<=18):
        print("party fee is: 100") 
    case _ if(age>18 and age <=50):
        print("party fee is: 150")
    case _ if(age>50):
        print("party fee is: 250")
    case _ if(age<=0):
        raise ValueError("incorrect age")
    


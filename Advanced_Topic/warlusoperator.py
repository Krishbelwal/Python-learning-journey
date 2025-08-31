#  warlous operortor - it gives us a funcanality to asssign a value to a variable within an experssion
 # a = True
 # print(a:= False)

# num = [1,3,5,6,6]
# while (n := len(num))>0:
#      print(num.pop())

# food = list()
# while True:
#   food = input("what food do you like:")
#   if food == "quiet":
#     break 
# food.append(food)
# food = list()
# while (food := input("Enter the food:"))!="quiet":
#       food.append(food)

# without warlus - 
name = input("Enter the input:")
if len(name)>5:
      print(f"your name is:{name}")
else:
      print("please write a name of 5 length")

# warlous    
if (name:= input("Enter the input:")) or (length := len(name))>5:
       print(f"your name is:{name}")
else:
      print("please write a name of 5 length")
      
      
      
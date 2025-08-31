# loops are used to do repeat instructions.

# 1 - itreater loops -
# Name = 'Krishna Belwal'
# i is accessiing each occurances of name variable
# for i in Name:
#     print(i)
    
# colors = ["Red","Green","Blue","Yellow"]
# for i in colors:
#     print(i)
#     for z in i:
#         print(z)

# A = "My name is krishna belwal"
# for i in A:
#     for j in i:
#         print(j)




# for with else:
# Name = 'Krishna Belwal'
# for i in Name:
#     if (i == 'B'):  
#      print("found")
#      break
#     print(i)
# print("End")


# practice questions -

# search element using loop - 
# list1 = [1,4,5,3,4,66,344,67,444,666] 
# x = 66
# idx = 0
# for i in list1:
#     if (i == x):
#         print("Found at index - " ,idx)
#     idx +=1




# range loops - 
# last element not included 
# for k in range(5):
#     print(k)

# step and stop - 
# for k in range(1, 6):
#  print(k)

# start stop step -
# for i in range(2, 22, 2):
#  print(i)
       
# pracice - 
# search element -
# for i in range(1 , 101 , 2):
#  print(i)
#  if (i == 29):
#         print("Found" , i)
        
        
# project 
# for i in range(1 , 20):
#        if(i == 3 or i == 6 or i == 9 or i == 12):
#          print("Fizz")
#        elif (i == 5 or i == 10):
#          print("Buzz")
#        elif (i == 7 or i == 14):
#          print("Boom")
#        elif (i == 15):
#          print("Fizzboom")
#        else:
#          print(i)
# print("End")

# for i in range(1 , 20):
#        if(i %3 == 0 and i % 5 == 0):
#          print("Fizzboom")
#        elif (i % 5 == 0):
#          print("Buzz")
#        elif (i %3 == 0):
#         print("Fizz")
#        elif (i %7):
#         print("Fizzboom")
#        else:
#          print(i)
# print("End")





# pass
list = [1,23,4,5]
for i in list:
    pass
# i = 0
# while(i<=3):
#     print(i)
#     i+=1
# print("Done")

# else
# a = int(input("Enter the num:"))
# while(a<40):
#     print("yes")
# else:
#     print("No")
    
    
# i= 1
# while i<=5:
#     print(i)
#     i+=1







# practice questions - 
 
#  1 - 
# i = 1
# while i <=100:
#     print(i)
#     i+=1
    
# i = 100
# while i >=1:
#     print(i)
#     i-=1
    
# Multipication table - 
# Number = int(input("Enter the number:"))
# i = 1
# while i<=10:
#    print(Number * i)
#    i+=1
    
# list1 = [1,4,5,3,4,66,344,66,444,666]
# list1 = ["Krish" , "Mohan" , "suresh" , "Rakesh"]
# i = 0
# while i < len(list1):
#  print(i , list1[i])
#  i +=1
 
list1 = [1,4,5,3,4,66,344,66,444,666]
x = 344
i = 0
while i < len(list1):
    print(i)
    if(list1[i] == x):
        print("Found at index" , i)
    i+=1
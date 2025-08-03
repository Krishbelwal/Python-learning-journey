# list- is a collection of differnt data types , list items seperted by , and enclosed between [] .it is imutable means we can change list after once created. 
# marks = [3,5,5,5,6,"Krish",5.8]

# if print all item of list-
# print(marks)  # if we want to print in the form of list so then using this concept  but if we run a loop so then we will get items in verticle form .
# for i in marks:
#     print(i)
 
# for finding length of list - 
# print(len(marks))

#jb list m change krana ho item-
# marks[0]=9
# print(marks )

# if single occurances print of list- 
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])
# print(marks[6])

# if print all items of list - 
# for i in range(0 , len(marks)):
#     print(marks[i])

# accessing through Negative indexing -
# print (marks[len(marks)-3])
# print(marks[-3:-1])])


# if check number is percentage in list ya not-
# if 7 in marks:
#  print("yes")
# else:
#    print ("no")
    
# list slicing -
marks = [3,5,5,5,6,"Krish",5.8]
# print(marks[1:5])
# print(marks[1:5:2])
# print(marks[:])
# print(marks[0:6])#jb last ka item chodna ho or isi tarah krkr hm ek size bda denge or fr saare print 
# print(marks[0:])#jb 0 k sath last ka bhi item print karana ho
# print(marks[:])# same 2 sre wale ki tarah

# Reverse-
# print(marks[::-1])



# list comprehension- creating the list on the fly
# lst = [i**i for i in range(1, 10)]
# print(lst)
# with given condition - 

# lst = [i for i in range(50) if(i%2==0)]
# print(lst)

# cube = [i*i*i for i in range(10 , 100) if(i%2==0)]
# print(cube)
    
# list2 = [i for i in range(100) if(i%2==0)]
# list3 = [i for i in range(100) if(i%2==0)]
# print(list3)

# questions - 
# list = [i for i in range(100)if(i%2!=0)]
# print(list)

# list = [1,24,3,4,56,7,8,412,4,567,34]
# for i in list:
#     if(i%2!= 0):
#         print(i)

# imp - 
# list1 = [1,3,57,8,6,6,6,]
# reverse = list1[::-1]
# print(reverse)

# reverse = list(reversed(list1))
# print(reverse)

# list1 = [1,3,57,8,16,26,56,]
# max = max(list1)
# print(f"The max number is:{max}")
# min = min(list1)
# print(f"The min number is:{min}")

# Exercise - 
Names = ["Krish" , "bhuvan" , "mahesh" , "yogi" , "ramesh" , "mohan"]

# Names.append("Rakesh")

# Names.pop(4)

# Names.reverse()
# reverse = list(reversed(Names))
# print(reverse)

# if("mahesh"):
#         print("yes")
        
# Names.sort()
# print(Names)

# print(Names[:3])

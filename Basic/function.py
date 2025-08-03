# // function -it is a block of a code which perform a specific task. when we have to do same work again and again in our program.Then we can create function of that task for making our code easy.
# a = 8
# b = 7
# ans = (a+b)
# print(ans)

# c = 10
# d = 9
# ans2 = (a+b)
# print(ans)
# so instead of it we should use functions-

# def calculation(a,b):
#     ans = (a+b)
#     print(ans)

# calculation(9,8)
# calculation(8,7)

# 2-
# def isgreater(n):
#     if(n>0):
#         print("greater")
#     else:
#         print("Not greater")
# isgreater(45)
# isgreater(-45)


# 3 - 
def Number(n):
    if(n>=0):
       return "positive"
    elif(n==0):
        return "Equal"
    else:
        return "Negative"
print(Number(45))
print(Number(-45))


# There are two types of functions:

# built-in functions
# user-defined functions
 

# 1. built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

 

# 2. user-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.
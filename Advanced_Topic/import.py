# import statments is used to bring built in modules into the cureent script to reuse their funcanility without rewriting code.and along with that we can make our code easiy using import 
#1- 
# import math 
# print(math.sqrt(25))

# 2-
# from math import sqrt
# print(sqrt(25))

# # 3- it is not recommended-
# from math import *

# # 4- kisi module k function ko short create-
# from math import sqrt as s
# print(s(25))

# # 5- multiple modules import using alias -
# import math as m , random as r
# from math import sqrt as s , pi as p

# 6- dir function
# import math as m
# print(dir(m))

# 7- from any file import function and variable-
# import krish as k
from krish import welcome
welcome()
# krish
# import krish as k
# k.welcome()
# print(k.ans_bin)
    

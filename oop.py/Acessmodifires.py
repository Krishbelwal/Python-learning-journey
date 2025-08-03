# By default public-
# class Employee:
#     def __init__(self):
#         self.__name = "Krish"
# a = Employee()
# print(a.__name)# not accesseble
# for acessing private properties- _class name
# Name mangling-  it is automaticalaly change variable name that starts with double underdcore(_), python renames such varible as _classname_variblename
# print(a._Employee__name) # can be accessed indirectly using name mangling

# how can be change data outside class and without private
# class Student:
#     def __init__(self, Name):
#       self.name = Name
#     def print(self):
#        print(f" The name is:{self.name}")
# a = Student("krish")
# a.name = "Ram" #  so Now i'm able to change name so if we doesn't want to change it so the we can make it as a private
# a.print()
# print(a._Student__name)

# new varible create but error nhi
class Student:
    __slots__ = ["__name"] # for getting error 
    def __init__(self, Name):
      self.__name = Name
    def print(self):
       print(f" The name is:{self.__name}")
a = Student("krish")
a.name = "Ram" 
a.print()
print(a._Student__name)
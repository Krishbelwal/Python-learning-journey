# dir- using it we can find out all atributes and methods of an object.
# x = (1,2,3)
# print(type(x))
# print(dir(x))
# print(x.__add__)

# dict-
# class person:
#     def __init__(self):
#        self.name = "krish"
#        self.age = 19
#     def print(self):
#         print(f"{self.name} and age is: {self.age}")
# p = person()
# p.print()
# print(p.__dict__) # using it we can get all atribute of this particular object

# Help-
class person:
    def __init__(self):
       self.name = "krish"
       self.age = 19
    def print(self):
        print(f"{self.name} and age is: {self.age}")
p = person()
# p.print()
print(help(person)) # it is used to get a help documentation for an object.


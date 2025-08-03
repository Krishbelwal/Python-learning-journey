# class car:
#     def __init__(self , name ,brand , modal  , color):
#         self.name = name
#         self.brand = brand
#         self.modal = modal
#         self.color= color
#     def print(self):
#         print(f"The car name is:{self.name} and color is:{ self.color} and brand is:{self.brand} and modal is:{ self.modal}")
# car1 = car("Harrier" , "Tata","Harrier0748" , "black" )
# car1.print()

# As a input-
class car:
    def __init__(self, name ,brand , modal, color):
        self.name = name
        self.brand = brand
        self.color= color
        self.modal= modal
    def print(self):
        print(f"The car name is:{self.name} and color is:{self.color} and brand is:{self.brand} and modal is:{self.modal}")
# car1 = car("Harrier" , "Tata","Harrier0748" , "black" )
# car1.print()
car_name  = input("Enter the car_name:")
car_color = input("Enter the car_color:")
car_brand = input("Enter the car_brand:")
car_modal= input("Enter the car_modal:")
car1 = car(car_name , car_color , car_brand , car_modal)
car1.print()

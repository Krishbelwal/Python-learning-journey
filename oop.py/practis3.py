# class car
# {
# private:
#     string car;
#     int year;

# public:
#     string car_Name;
#     string color;
#     string set_car(string s)
#     {
#         if (s == "Tata")
#         {
#             return car_Name;
#         }
#     }
#     int set_year(int n)
#     {
#         if (n > 1900 || n < 2025)
#         {
#             return n;
#         }
#     }
# };
# int main()
# {
#     car c1;
#     c1.car_Name = "Harrier";
#     c1.color = "Black";
#     cout << c1.set_car("Tata")<<endl;
#     cout << c1.set_year(2024)<<endl;
#     car c2;
#     c1.car_Name = "Nexon";
#     c1.color = "white";
#     cout << c1.set_car("Bmw")<<endl;
#     cout << c1.set_year(2045)<<endl;

# 2-
# class car:
#     def __init__(self , Name , color , year):
#         self.car_name = Name
#         self.car_modal = "Tata"
#         self.color = color
#         self.year = year
#     def set_Name(self, n):
#         if(n ==self.car_modal):
#            return self.car_name
#     def set_year(self, y ):
#         if(y>1990 or y<2025):
#             return self.year
#     def print(self):
#         print(f"The car name is:{self.car_name} and color is:{self.color} and year is:{self.year}")
# car1 = car("Harrier" , "black" , 2016)
# car1.set_Name("Tata")
# car1.set_year(2018)
# car1.print()

# as a input-
class car:
    def __init__(self , Name , color , year):
        self.car_name = Name
        self.car_modal = "Tata"
        self.color = color
        self.year = year
    def set_Name(self):
        n = (input("Enter:"))
        if(n ==self.car_modal):
           return self.car_name 
    def set_year(self, y ):
        if(y>1990 or y<2025):
            return self.year
    def print(self):
        print(f"The car name is:{self.car_name} and color is:{self.color} and year is:{self.year}")

car_name  = input("Enter the car_name:")
car_color = input("Enter the car_color:")
car_year = input("Enter the car_year:")
car1 = car(car_name , car_color , car_year)
car1.set_Name()
car1.set_year(2018)
car1.print()
# global vairable
x = 4
print(x)
def hello():
    # local vaiable
#    global x 
    x = 5 
    print(f"The local varible x is{x}")
print(f"The global varible x is{x}")
hello()
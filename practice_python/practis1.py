try:
 a = int(input("Enter The Number:"))
 b = int(input("Enter The Number:"))
#  print(a+b/2)
 print(a+c/2)

except ValueError:
 print("it's a valueerror. your input is a string  Not an integer. please check the code")
except NameError:
 print("it's a Nameerror.please check the code")
if(a<10):
    raise ValueError("Error occurred! value should be above 10 . Please check the code.")
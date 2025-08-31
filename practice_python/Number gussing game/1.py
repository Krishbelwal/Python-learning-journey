# 
import random
secret = random.randint(1,100)  # 10
print(secret)
Gusses_list = []
attempt = 0
Max_attempts = 5
while attempt <= Max_attempts:
  inp = int(input("Enter your Number:"))
  Gusses_list.append(inp)
  attempt+=1
  if (inp == secret):
      print("congratulation! you have successfully guessed the number")
  elif (inp < secret):
      print("Low guess! Try again")
  elif (inp > secret):
      print("High guess! Try again")
else:  
 print(f"well tried! The number was {secret}")
 for guess in Gusses_list:
    print(guess)
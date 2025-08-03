def checkprime(n):
 n = int(input("Enter the Num:"))
 for i in range(2 , n):
      if(n%i==0):
        return "Nonprime"
      return "prime"
      
print(checkprime(23))

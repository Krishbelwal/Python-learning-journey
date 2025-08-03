# Tuple - is a collection of differnt data types , Tuple items seperted by , and enclosed between () .it is mutable means we can't change Tuple after once created.
# tuple is mutable
# Tuple = (1,2,3,4,4)
# print(type(Tuple))

# python will consider as a int if we write just value without" ,".
# Tuple = (1)
# print(type(Tuple))



# Tuple methods - 
# Tup  = Tuple.index(4) # it gives value(paranthese) index 
# print(Tup)

# Tup  = Tuple.count(4) 
# print(Tup)

# question - 
Movies = ()
Mov1 = input("Enter the Movie 1:")
Mov2 = input("Enter the Movie 2:")
Mov3 = input("Enter the Movie 3:")
Movies.append(Mov1)
Movies.append(Mov2)
Movies.append(Mov3)
print(Movies)
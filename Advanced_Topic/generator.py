# genrator in python is a special type of function that allow you to itreate a sequence of values like - list, tuples etc... , means it genrate the values  fly on instead of storing in memory. 
def my_generator():
    for i in range(50):
        yield i
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

def my_generator(start , end):
    while start <=end:
        yield start
        start +=1
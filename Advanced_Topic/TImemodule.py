import time
def usingwhile():
    i = 1
    while i<500:
        print(i)
        i+=1
def usingfor():
    for i in range(1,10):
        print(i)
# it is used to calcualte time taken of program / function  - 
init = time.time()
print(init)
usingfor()
init2 = time.time()
print(init2)
print("first",init2-init)

init3 = time.perf_counter()
print(init3)
usingfor()
init4 = time.perf_counter()
print(init4)
print("second" , init4-init3)

# print(time.ctime())

# current_time = time.strftime("%Y-%m-%d %H:%M:%S")
# print(current_time)

# if i want to wait for something then - 
# print(time.sleep(4))
# print("This is prited after 4 seconds")

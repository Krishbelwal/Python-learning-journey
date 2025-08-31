# Read-
# r mode is default
f = open('Hello.py')
read = f.read()
print(read)
f.close()
# tell = f.tell()
# print(tell)


# write -
with open("Hello.py" , 'w') as f:
 f.write(' "This is a very good Example" ')

# write- if we write as such so we have to close file
# f = open('myfile.txt', 'w')
# f.write("iam a good boy")
# f.close()



# apand-  when we want value should not be overright then we can use it.
# f = open('myfile.txt', 'a')
# f.write("My name is krishna belwal")
# f.close()
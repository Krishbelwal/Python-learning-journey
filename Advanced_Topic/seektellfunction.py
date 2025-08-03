f = open('myfile.txt')
# # print from given value
f.seek(19)
print(f.tell())
print(f.read())

# tell
# truncate-
# with open('myfile.txt' , 'w') as f:
#     f.write("hello")
#     f.truncate(2)
#     # kuch occurance print
#     f = open('myfile.txt')
#     print(f.read())


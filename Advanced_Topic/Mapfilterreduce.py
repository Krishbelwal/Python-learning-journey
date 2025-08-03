# def cube(x):
#     return x*x*x

# l = [1,3,4,54,5,4]
# # map - fun , itrable objects
# newline = map(cube, l)

# def findsquare(x):
#     return x*x
# findsquare = lambda x: x*x
# l = 1,2,4,8,4,9
# # Map-
# newline = tuple(map(findsquare, l))
# newline = tuple(map(lambda x: x*x ,l))
# print(newline)

# filter-
# filter_fun = lambda a: a>4
# l = [1,3,4,5,6,9,8]
# newnewline = list(filter(filter_fun , l))
# newnewline = list(filter(lambda a: a>4 , l))
# print(newnewline)

# reduce-
# from functools import reduce
# Num = [1,3,4,6,7,8]

# sum = reduce(lambda x,y: x+y , Num)
# print(sum)

import functools
print(functools.__file__)


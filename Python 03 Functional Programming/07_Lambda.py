# Lambda Functions -> one time use! , one time anonymous functions
# Functions that are only used once can be written as lambda functions
# Use it and throw it away, no need to store the functions
# you can use it with filter, map, reduce as well

from functools import reduce

your_list = [1,2,3,4,5]
print(list(map(lambda item: item*2,  your_list)))
print(list(filter(lambda item: item % 2 == 0, your_list)))
print(reduce(lambda acc, item: acc + item, your_list))


# exercise 
print(list(map(lambda x: x**2, your_list)))
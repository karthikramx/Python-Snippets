# map, filter, zip and reduce

# this reduces a collection to a single value
from functools import reduce

my_list = [1,2,3]

def accumulator(acc, item):
    return acc + item


print(reduce(accumulator,my_list,0))



# exercise : capitalize all pet names

my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(item:str):
    return item.capitalize()

print(list(map(capitalize, my_pets)))

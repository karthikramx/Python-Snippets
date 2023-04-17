# The actual generator, 
# it is more efficient to call the generator, that to store a collection of objects, and access them sequenctially

# everything that is a generator is an iterable but an iterable is not a generator
# a generator is a subset of iterable

# generators are just functions
# this is going to loop over a range

# if you are only using only a number at once in a list , then why generator the list?
# we are holding only one item in memory

def generator_func(arg):
    for i in range(arg):
        yield i

for item in generator_func(2):
    print(item)

print(generator_func(2))
g = generator_func(2)
print(next(g))
print(next(g))





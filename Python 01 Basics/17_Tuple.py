my_tuple = (1,2,3,4)
print(4 in my_tuple)

# more performant than list
# values cannot be changed

# Tuple
my_tuple = (1,2,3,4,5)
print(my_tuple[1:2])

# tuple decontruction
a,b,c,*other = (1,2,3,4,5)
print(a,b,c,other)

# methods

# count
print(my_tuple.count(1))
print(my_tuple.index(3))


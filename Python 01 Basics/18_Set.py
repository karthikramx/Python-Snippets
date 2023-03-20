# Sets
# unordered collection of unique objects
my_set = {1,2,3,4,5,5}
print(my_set)


# methods
my_set.add(100)
my_set.add(2)
print(my_set)

# converting into set
my_list = [1,2,3,4,5,6,3,3,3,3,4]
print(set(my_list))

# other points
# you cannot index a set
print(1 in my_list)

# exploring set methods

my_set = {1,2,3,4,5}
your_set = {3,4,5,6,7}

#difference
print(my_set.difference(your_set))

#discard
print(my_set.discard(5))
print(my_set)

#intersection
print(my_set.intersection(your_set))
print (my_set and your_set)

#disjoint
print(my_set.isdisjoint(your_set)) # nothing in common, they have something in common

#union
print(my_set.union(your_set))
print( my_set | your_set)

#issubset
my_set = {4,5}
your_set = {4,5,6,7}
print(my_set.issubset(your_set))
print(your_set.issuperset(my_set))


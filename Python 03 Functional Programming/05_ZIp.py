# Zip function : 

my_list = [1,2,3]
your_list = (10,20,30)

print(list(zip(my_list,your_list)))

their_list = [5,6,7]

print(list(zip(my_list,your_list,their_list)))


# exercise

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort()

print(list(zip(my_strings,my_numbers)))

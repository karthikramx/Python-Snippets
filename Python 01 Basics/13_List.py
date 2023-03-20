# ordered sequence of objects on any type

li1 = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a',True]

# Slicing // lists are mutable
amazon_cart = ['notebooks','sunglasses','books','apples','headphones']
print(amazon_cart[1:3])

# copying a list
amazon_cart[0] = 'laptop'

new_listx = amazon_cart
new_listx[0] = 'mouse' # this modifies amazon cart too

print('new listx:',new_listx)
print('amazon_cart:',amazon_cart) 

# if you want to create an actual copy you need to do this
new_list = amazon_cart[:] # instead of new_list = amazon_cart, this command will make new_list point to the same memory location
new_list[0] = 'keyboard'
print(amazon_cart)
print(new_list)

# List methods
# remember the difference between functions (builtin function) vs methods
# methods belong to the datatype

# append method
basket = [1,2,3,4,5]
basket.append(100) # hover over it and read what it does, see what it returns
print(basket)

# insert method
basket.insert(2,55)
print(basket)

# an iterable is something that you can loop over
# extend
basket.extend([200])
print(basket)

# pop
print('-'*10)
print(basket.pop(3))
print(basket)

# removing
basket.remove(55)
print(basket)

# clear
basket.clear()
print(basket)

# index
basket = [1,2,3,4,5]
print(basket.index(5))
print(basket.index(2,0,4))

# count
basket = [1,2,1,3,4,5,1,1,1]
print(basket.count(1))

# sort
basket = ['a','e','f','w','z','f']
basket.sort() # sorts the list in place
print(basket)

# sorted in a built-in function , therefore it produces a new list
basket = ['a','e','f','w','z','f']
print(sorted(basket))

# reverse
basket = [1,2,3,4,5,6]
basket.reverse()
print(basket)

# other way of reversing a list
basket = [1,2,3,4,5]
print(basket[::-1])

# .join
sentence = ' '
sentence = sentence.join(['My','Name','is','Karthik'])
print(sentence)

# list unpacking
a,b,c = [1,2,4]
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)
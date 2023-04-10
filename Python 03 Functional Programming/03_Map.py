# Map | filter | zip | reduce

# Map
# maps a function, on each element of an iterable
# the point of functional programming is to make it readable and easier to maintain

def multiply_by2(item):
    print(f'multiplying {item} by 2')
    return item*2

# list of items    
list_items = [1,2,3,4]
print(list(map(multiply_by2,list_items)))
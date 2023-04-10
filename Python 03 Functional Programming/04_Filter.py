# Filter, returns true or false on an iterable
# this too acts on the iterable

def check_odd(item):
    return item %2 != 0

list_items = [1,2,3,4,5]

print(filter(check_odd,list_items))
odd = list(filter(check_odd,list_items))

print(odd)


# exercise : Filter the scores that pass above 50
scores = [73, 20, 65, 19, 76, 100, 88]


def above50(item):
    return item > 50


print(list(filter(above50,scores )))
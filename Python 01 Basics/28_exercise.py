list1 = ['a', 'b', 'c', 'd', 'a', 'c']

newlist = []

for item in list1:
    if list1.count(item) > 1:
        if item not in newlist:
            newlist.append(item)

print(newlist)
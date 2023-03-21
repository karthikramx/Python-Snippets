# Iterable : an object or a collection that can be iterated over
# all iterables in python:  Dictionary, Tuple, list, string, set
user = {'one':'Karthik','two':'Ram','three':'Chodapaneedi'}
for item in user.items():
    print(item)
for item in user.keys():
    print(item)
for item in user.values():
    print(item)


for key,value in user.items():
    print('key:',key)
    print('item:',value)


list_new = [1,2,3,4,5]
counter = 0
for item in list_new:
    counter +=item
print(counter)




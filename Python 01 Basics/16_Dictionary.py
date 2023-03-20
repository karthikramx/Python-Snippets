# A dictionary is an unordered key value pain

dictionary = {'a':1, 'b':2}
print(dictionary['a'])
# print(dictionary['c']) ERROR

dictionary = {
    'a':[1,2,3],
    'b': True,
    'c': 'Karthik Ram'
}

print(dictionary['a'][1])

mylist = [
    {
    'a':[1,2,3],
    'b': True,
    'c': 'Karthik Ram'
}
,{
    'a':[1,2,3],
    'b': True,
    'c': 'Karthik Ram'
}
,{
    'a':[1,2,3],
    'b': True,
    'c': 'Karthik Ram'
}
]

print(mylist[0]['a'][2])

# KEYS
# 1. Dictionary keys are should be unmutable , it cannot hash mutable objects
# 2. A key has to be unique, otherwise we overwrite the value

# Dictionary methods

user = {'basket':[1,2,3],'greet':'hello'}
print(user.get('basket'))


# if you want to create using the dict builtin function
user = dict(name='Karthik Ram')
print(user)

# other methods and funcitons
print('name' in user)


# methods
# keys
user = {'basket':[1,2,3],'greet':'hello'}
print(user.keys())
print(user.values())
print(user.items())

# clear and copy
user2 = user.copy()
user.clear()
print(user)
print(user2)

# pop
print(user2.pop('basket'))

# update
print(user2.update({'age':55}))
print(user2)
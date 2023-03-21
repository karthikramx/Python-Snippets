# Logical Operators
print(4>5)
print(4==5)
print(4 or 5)
print('a' > 'A')

# == != >= <= < >
# and or not

print(not True)

# Exercise

is_magician = True
is_expert = True

if is_magician and is_expert: print('You are a master magician')
elif is_magician and not is_expert: print('at least you are getting there')
elif not is_magician: print('you need magic powers')


# is vs ==
# == looks for equality of value, it will type convert to check of equality
# is checks if the location of a value is the same , location in memory needs to be the same

# While loops
# while condition:
#     print("do something")

# example 1
i = 0
while i < 5:
    print(f'Doing something in the {i}th loop')
    i += 1

# gotcha!
i = 0
while i < 5:
    i += 1
    print('Doing something')
else:
    print('Doing something when the loop ends')

i = 0
while i < 5:
    i += 1
    print('Doing something')
    break
else:
    print('Doing something while the loop ends successfully')
print('jumps here if while is broken')
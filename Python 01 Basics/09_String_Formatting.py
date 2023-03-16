new = "This is a string"
print(new[0])

#indexing goes like this [start:stop:stepover]

print(new[0:5]) # This
print(new[2:7]) # is is
print(len(new)) # 16
print(new[0:len(new)]) # This is a string
print(new[0:len(new): 2]) # Ti sasrn
print(new[0:]) # This is a string
print(new[::1]) # This is a string
print(new[-1]) # g

# new[0] = 'm' --> this cannot be done , because strings are immutable


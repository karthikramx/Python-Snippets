# Continue

i = 0
my_list = [1,2,3,4,5]
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue
    print('testing continue') # this is never reached!

    
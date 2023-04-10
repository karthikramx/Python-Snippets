# Pure FUnctions
# 2 Rules
#   1. Same input leads to same output                              # same input, same output - very pure function
#   2. Function should not produce any side effects! / even print   # no side effects at all, should not affect the outside world


# this doesn't affect the outside world
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))


# why its more important in the real world??
# less buggy code
# easy to maintain


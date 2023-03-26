# *args, **kwargs

                    # this is a parameter
def super_function(*args, **kwargs):
    print(kwargs)
    for items in kwargs.values():
        print(items)
    return sum(args)

print(super_function(1,2,3,4,5,i='karthik',num2=10))

# Rule: params, *args, default parameters, **kwargs
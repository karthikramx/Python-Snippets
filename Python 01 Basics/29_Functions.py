# Functions
def say_hello():
    '''
    This function says hello
    '''
    print('Hello')

say_hello()
say_hello()
say_hello()

# Arguments vs Parameters
# Arguments are something you provide when calling the functions
# Parameters are something you define, while wrting the function

            # this is a function parameter
def say_hi(name):
    print(f'Hi, {name}')
            # this is a funciton argument
say_hi('karthik')

# position arguments need to be in order
                    # default parameters,...
def print_details(name='No Name', age='No Age'):
    print(f'print(Name is {name}, Age is {age})')

                # always provide in order to keep it clean, if not menitioning keyword, provide in order
print_details(name='Karthik', age='29')






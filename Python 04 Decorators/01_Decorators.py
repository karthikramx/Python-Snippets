# HOC - higher order function
# A Higher order function is any function which either receives or accepts a function
# map filter reduce are all higher order function

def my_decorator(func):
    def wrapper():
        print("*******")
        func()
        print("*******")
    return wrapper

@my_decorator
def hello():
    print("hello")

#my_decorator(hello)()

hello()
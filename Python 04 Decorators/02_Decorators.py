# in this we will build a decorators with functions with arguments and keyword arguments


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*******")
        func(*args,**kwargs)
        print("*******")

    return wrap_func

@my_decorator
def hello(greeting, emo, name, designation):
    print(greeting, " ", emo)
    print(name, " you are the ", designation, " bitch")


hello("hello how are you",':)', name='karthik', designation='CEO')

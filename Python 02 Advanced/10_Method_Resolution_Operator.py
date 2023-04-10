# They way functions are called in multiple heritance
# They get called in the order of the definitions!


class A:
    def __init__(self) -> None:
        print("This is class A")

    def func_test(self):
        print("Hello this is a function from class a")

class B(A):
    def __init__(self) -> None:
        print("This is class A")

class C(A):
    def __init__(self) -> None:
        print("This is class A")

class D(B,C):
    def __init__(self) -> None:
        print("This is class A")


d =  D()
d.func_test()
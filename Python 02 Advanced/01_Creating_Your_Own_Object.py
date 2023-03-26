class test:
    def __init__(self,name,age) -> None:
        self.age = age
        self.name = name

    def print_name(self):
        print(self.name)

t = test()
print(t)
print(t.name)
print(t.print_name())

t.location = 'Arizona'
print(t.location)
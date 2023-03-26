# A class method can be called directly by the class and not the 
# object created using the class method

class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about(self):
        print(f"my name is {self.name}")

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @classmethod
    def instantiate(cls, name, age):
        return cls(name, age)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


print(PlayerCharacter.adding_things(5,6))

abc = PlayerCharacter.instantiate('karthik',29)
abc.about()


print(PlayerCharacter.adding_things2(5,5))
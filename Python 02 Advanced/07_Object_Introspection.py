# The Super method
# super refers to the class above!
# in this case it refers to user

class User:
    def __init__(self,email) -> None:
        self.email = email
        print('user initialized')

    def sign_in(self): 
        print('logged in')

class Wizard(User):
    def __init__(self,name,power,email) -> None:
        super().__init__(email) # need to run this to run init of parent class
        self._name = name
        self._power = power

    def attack(self):
        print(f'User:{self._name} attacked with power:{self._power}')


print(dir(Wizard))
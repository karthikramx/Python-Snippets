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

class Archer(User):
    def __init__(self,name:str,arrows:int,email:str) -> None:
        super().__init__()
        self._name = name
        self._arrows = arrows

    def attack(self):
        self._arrows -=self._arrows
        if self._arrows < 0: self._arrows = 0
        print(f'User:{self._name} attacked with an arrow, arrows left:{self._arrows}')


wizard = Wizard('karthik',100,'karthikram570@gmail.com')
archer = Archer('manas',200,'manastulasi@gmail.com') 

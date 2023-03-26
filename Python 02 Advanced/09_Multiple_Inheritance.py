# Multiple inheritance

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

    def attack_power(self):
        print(f'User:{self._name} attacked with power:{self._power}')

class Archer(User):
    def __init__(self,name:str,arrows:int,email:str) -> None:
        super().__init__(email)
        self._name = name
        self._arrows = arrows

    def attack_arrow(self):
        self._arrows -=self._arrows
        if self._arrows < 0: self._arrows = 0
        print(f'User:{self._name} attacked with an arrow, arrows left:{self._arrows}')

class Xman(Wizard,Archer):
    def __init__(self, name, power, arrows, email) -> None:
        print("******************")
        Wizard.__init__(self,name,power,email)
        Archer.__init__(self,name,arrows,email)

xman = Xman('Karthik',50,100,'karthikram570@gmail.com')
xman.sign_in()
xman.attack_arrow()
xman.attack_power()
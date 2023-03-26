#ploymorphism

#object classes can have the same method name


class User:
    def __init__(self) -> None:
        print('user initialized')

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self,name,power) -> None:
        super().__init__()
        self._name = name
        self._power = power

    def attack(self):
        print(f'User:{self._name} attacked with power:{self._power}')

class Archer(User):
    def __init__(self,name:str,arrows:int) -> None:
        super().__init__()
        self._name = name
        self._arrows = arrows

    def attack(self):
        self._arrows -=self._arrows
        if self._arrows < 0: self._arrows = 0
        print(f'User:{self._name} attacked with an arrow, arrows left:{self._arrows}')


wizard = Wizard('karthik',100)
archer = Archer('manas',200) 


def player_attack(char):
    char.attack()


player_attack(wizard)
player_attack(archer)
# Private vs Public varaibles

class Player:
    def __init__(self,name:str,age:int):
        # privage variables
        self._name = name
        self._age = age
        print("init")

    def speak(self):
        print(f'My name is {self._name}')


p = Player('karthik',29)
p.speak()
p.speak = 'speak'
print(p.speak)
# print(p.speak()) # will result in error as it not callable anymore

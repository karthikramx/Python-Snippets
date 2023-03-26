# Dunder
# allows custom modifying
# dunder methods also called magic methods

class Cart:
    def __init__(self,color, age) -> None:
        self.color = color
        self.age = age

    def __str__(self):
        return 'this is a return from __str__'

    def __len__(self):
        return 5

shopping_cart = Cart('orange',1)
print(shopping_cart)
print(shopping_cart.__str__())
print(str(shopping_cart))
print(shopping_cart.__init__('red',1))
print(len(shopping_cart))
class Animal():
    def __init__(self, name):
        self.name = name
    
    def eat(self,food):
        return'{} likes to eat {}'.format(self.name, food)

# Imagine only animal dog should have a breed
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def hello(self):
        return'{} is of breed {}'.format(self.name, self.breed)

browney = Dog('Browney', 'Pug')
print(browney.eat('Chicken'))
print(browney.hello())
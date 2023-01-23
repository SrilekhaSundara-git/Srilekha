class Store():

    def __init__(self):
        self.owner = 'Srilekha'
    
    def exclaim(self):
        return "Lot's of Stuff to buy!!! Come inside"

class CoffeeStore(Store):
    pass

coffee = CoffeeStore()
print(coffee.owner)
print(coffee.exclaim())
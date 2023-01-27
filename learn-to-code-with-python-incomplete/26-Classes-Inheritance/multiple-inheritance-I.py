class FrozenFood():
    def thaw(self, minutes):
        print(f'Thawing in {minutes}')

    def store(self):
        print("Putting in the freezer")

class Dessert():
    def add_weight(self):
        print('Adding extra weight')
    
    def store(self):
        print("Putting in the refrigerator")
    
class Icecream(Dessert, FrozenFood):
    pass
ic = Icecream()
ic.add_weight()
ic.thaw(minutes = 6)
ic.store()
print(Icecream.mro())

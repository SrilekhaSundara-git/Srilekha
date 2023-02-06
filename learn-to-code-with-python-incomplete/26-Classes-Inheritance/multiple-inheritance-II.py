class Restaurant():
    def make_reservation(self, party_size):
        print(f'Booked a table for {party_size} people')

class SteakHouse(Restaurant):
    pass

class Bar():
    def make_reservation(self, party_size):
        print('Booked a Lounge for {party_size} people')
    
#class BarAndGrill(SteakHouse, Bar):
#    pass

class BarAndGrill(Bar, SteakHouse):
    pass
bag = BarAndGrill()
bag.make_reservation(2)
print(BarAndGrill.mro())

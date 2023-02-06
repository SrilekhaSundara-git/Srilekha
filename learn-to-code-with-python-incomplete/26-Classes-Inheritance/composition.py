#Composition, two classes are independent of each other.
#classes will have has a relationship between the classes.

class Anil():
    car = 1
    def has_a_car(self):
        print(f"Anil has {self.car} car")

class Sunil():
    a = Anil()
    bike = 1
    def has_a_bike(self):
        print(f"Sunil has a {self.bike} bike")

s = Sunil()
s.has_a_bike()
s.a.has_a_car()
Sunil.a.has_a_car()
from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Boabo's Burrito Bowl"

    @classmethod
    def steak_method(cls):
        return cls('Mushroom', 'White', 1)
    
    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein 
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_gauc(self):
        self.guacamole_portions += 1
    
class_mock = MagicMock(spec = BurritoBowl)
print(class_mock.restaurant_name)
print(class_mock.steak_method())

instant_mock = MagicMock(spec_set = BurritoBowl.steak_method())
print(instant_mock.protein)
print(instant_mock.rice)
print(instant_mock.guacamole_portions)
#print(instant_mock.beans)
instant_mock.beans = True
print(instant_mock.beans)
print(instant_mock.guacamole_portions)
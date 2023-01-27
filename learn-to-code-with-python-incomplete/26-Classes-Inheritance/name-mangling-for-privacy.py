class Nonsense():
    def __init__(self):
        self.__some_attribute = 'Hello'

    def __some_method(self):
        print('Some Method in the Nonsense class')

class SpecialNonsense(Nonsense):
    pass
n = Nonsense()
sn = SpecialNonsense()
print(n._Nonsense__some_attribute)
print(n._Nonsense__some_method())
n._Nonsense__some_attribute
n._Nonsense__some_method()
print(sn._Nonsense__some_attribute)
print(sn._Nonsense__some_method())
sn._Nonsense__some_attribute
sn._Nonsense__some_method()

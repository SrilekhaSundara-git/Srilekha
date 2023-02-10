import random
import copy

characters = [i for i in range(1,10)]
clone = characters[:]
clone = characters.copy()
clone = copy.copy(characters)
print(clone is characters)

random.shuffle(clone)
print(characters)
print(clone)
print(id(clone))
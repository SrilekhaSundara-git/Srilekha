# Define a Chocolate class that accepts and assigns a cacao_content attribute.

class Chocolate():
    def __init__(self,cacao_content):
        self.cacao_content = cacao_content
    
    @classmethod
    def sweet(cls):
        return cls(cacao_content = 30)
    
    @classmethod
    def semisweet(cls):
        return cls(cacao_content = 50)
    
    @classmethod
    def bittersweet(cls):
        return cls(cacao_content = 70)
    
    @classmethod
    def bitter(cls):
        return cls(cacao_content = 99)

# Define a "sweet" class method that returns a 
# Chocolate object with a cacao_content value of 30.

# Define a "semisweet" class method that returns a 
# Chocolate object with a cacao_content value of 50.

# Define a "bittersweet" class method that returns a 
# Chocolate object with a cacao_content value of 70.

# Define a "bitter" class method that returns a 
# Chocolate object with a cacao_content value of 99.

s = Chocolate.sweet()
print(s.cacao_content)

semi = Chocolate.semisweet()
print(semi.cacao_content)

bitter_ = Chocolate.bittersweet()
print(bitter_.cacao_content)

b = Chocolate.bitter()
print(b.cacao_content)
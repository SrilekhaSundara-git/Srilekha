class Currency():

    def __init__(self, dollars):
        self._cents = dollars * 100
    
    @property
    def dollars(self):
        return self._cents/100
    
    @dollars.setter
    def dollars(self,dollars):
        if dollars > 0:
            self._cents = dollars * 100
    
c = Currency(500)
print(c.dollars)
c.dollars = 1000
print(c.dollars)
c.dollars = -1000
print(c.dollars)
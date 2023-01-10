
class Multiple():
    def __init__(self):
        self._end = 1000
    
    @property
    def multiple_3_or_5(self):
        return sum([num for num in range(1,self._end) if num % 3 == 0 or num % 5 == 0])

multiple = Multiple()
print(multiple.multiple_3_or_5)
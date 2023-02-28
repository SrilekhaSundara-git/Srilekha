class Bill:
    """
    Object that contains data about the bill, 
    such as total amount and the period of the bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in a flat and 
    pays the share of the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house/(self.days_in_house + flatmate2.days_in_house)
        return bill.amount * weight


class PdfReport:
    def __init__(self, filename):
        self.filename = filename
    
    def generate(self, flatmate1, flatmate2, bill):
        pass

the_bill = Bill(amount=120, period = 'December 2020')
john = Flatmate(name = 'John', days_in_house = 20)
mary = Flatmate(name = 'Mary', days_in_house = 25)
print("John Pays:", john.pays(bill = the_bill, flatmate2 = mary))
print("Mary Pays:", mary.pays(bill = the_bill, flatmate2 = john))

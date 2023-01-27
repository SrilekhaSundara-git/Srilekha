class Employee():
    def works(self):
        print("You're Welcome!!! to our company")

class Manager(Employee):
    def manages(self):
        print('Assigns tasks')

class Director(Manager):
    def fires_employee(self):
        print('Fires Employee')

e = Employee()
m = Manager()
d = Director()

e.works()

m.works()
m.manages()

d.works()
d.manages()
d.fires_employee()
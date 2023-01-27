class Teacher():
    def hello(self):
        print("Hi Hello !!!")

class Principal(Teacher):
    def hello(self):
        print("Hi Students!!!")

t = Teacher()
p = Principal()

t.hello()
p.hello()
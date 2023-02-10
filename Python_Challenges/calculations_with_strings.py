def zero(f = None): return 0 if f is None else int(f(0))
def one(f = None): return 1 if f is None else int(f(1))
def two(f = None): return 2 if f is None else int(f(2))
def three(f = None): return 3 if f is None else int(f(3))
def four(f = None): return 4 if f is None else int(f(4))
def five(f = None): return 5 if f is None else int(f(5))
def six(f = None): return 6 if f is None else int(f(6))
def seven(f = None): return 7 if f is None else int(f(7))
def eight(f = None): return 8 if f is None else int(f(8))
def nine(f = None): return 9 if f is None else int(f(9))

def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x / y



print(seven(times(five()))) # must return 35
print(four(plus(nine()))) # must return 13
print(eight(minus(three()))) # must return 5
print(six(divided_by(two()))) # must return 3


#######################################################

class Int(int):
    """Pseudo-int with operation on it.
    """
    def __init__(self, value=0):
        super(Int, self).__init__(value)
        self.operation = None

    def __call__(self, operand=None):
        if operand is None:
            return self
        elif operand.operation == 'times':
            return self * operand
        elif operand.operation == 'plus':
            return self + operand
        elif operand.operation == 'minus':
            return self - operand
        elif operand.operation == 'divided_by':
            return self / operand


def operation(name):
    def _operation(arg):
        arg.operation = name
        return arg
    return _operation


(zero, one, two, three, four, five, six, seven, eight, nine) = (
Int(0),Int(1), Int(2), Int(3), Int(4),Int(5), Int(6), Int(7), Int(8), Int(9))

plus = operation('plus')
minus = operation('minus')
times = operation('times')
divided_by = operation('divided_by')
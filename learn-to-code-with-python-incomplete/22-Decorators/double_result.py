import functools

def smartdivide(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you!")
        result = fn(*args, **kwargs)
        print("It was my pleasure executing your function! Have a nice day!")
        return result
    return inner


@smartdivide
def divide(num1:int, num2:int)->int:
    "Dividing two numbers"
    return num1/num2
print(divide(1,2))
help(divide)
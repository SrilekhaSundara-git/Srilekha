def func1(name):
    return 'func1 {}'.format(name)
    
def func2(name):
    return 'func2 {}'.format(name)

def func3(func):
    return func('Hello')

print(func3(func1))
print(func3(func2))
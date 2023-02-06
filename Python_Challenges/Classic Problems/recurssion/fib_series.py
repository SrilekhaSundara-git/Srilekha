def fib_series(n:int)->int:
    """This is a recursive function
    to find the Fibonacci series of a number
    n:int fib(n) = fib(n - 1) + fib(n - 2)"""
    if n <2:
        return n
    else:
        return fib_series(n - 2) + fib_series(n - 1)

    
help(fib_series)
print(fib_series(5))
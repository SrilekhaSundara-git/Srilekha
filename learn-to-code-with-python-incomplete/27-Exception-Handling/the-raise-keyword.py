def add_numbers(param1:int, param2:int)->int:
    try:
        if param1 <= 0 or param2 <= 0:
            raise ValueError('One or more values are either zero or negative numbers!!!')
        return param1 +param2
    except ValueError as v:
        print("Caught the Value Error {}".format(v))
        return v 

print(add_numbers(1,2))
print(add_numbers(1,0))
print(add_numbers(-1,-2))
print(add_numbers(10,-90))
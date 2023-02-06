def divide_5_by_number(n):
    try:
        calculation = 5 / n
    except (ZeroDivisionError, TypeError) as e:
        return f"Something went wrong. The error was {e}"
    return calculation
print(divide_5_by_number(10))
print(divide_5_by_number(0))
print(divide_5_by_number("nonsense"))

def divide_5_by_number(n):
    try:
        calculation = 5 / n
    except ZeroDivisionError as e:
        return f"Division with Zero is impossible. The error was {e}"
    except TypeError as e:
        return f"Expected either int or float to divide. The error was {e}"
    return calculation
print(divide_5_by_number(10))
print(divide_5_by_number(0))
print(divide_5_by_number("nonsense"))
print(divide_5_by_number(0.5))
print(divide_5_by_number([1,2,4]))
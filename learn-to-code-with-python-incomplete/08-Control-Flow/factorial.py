# Define a function called "factorial" that accepts a single number as input
#
# A factorial represents the product of all numbers up to, and including, that number. 
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120
#
# Return the factorial calculation from your function. You should NOT use any kind of loops. 
# Instead, utilize recursion. Your function MUST call itself.
# See sample inputs and return values below
def factorial(param):
    return param * factorial(param - 1) if  param >= 1 else 1
print(factorial(5))

 #=> 1
#factorial(2)# => 2
# factorial(3) => 6
# factorial(4) => 24
# factorial(5) => 120


def factorial(param):
    fact = 1
    while param>0:
        fact = fact*param
        param -= 1
    return fact

print(factorial(5))


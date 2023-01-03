# Define a divisible_by_three_and_four function that accepts a number as its argument. 
# It should return True if the number is evenly divisible by both 3 and 4 . 
# It should return False otherwise.
def divisible_by_three_and_four(param:int)->bool:
    return True if (param % 3 == 0 and param % 4 == 0) else False

print(divisible_by_three_and_four(12))  # => False
# divisible_by_three_and_four(4)   => False
# divisible_by_three_and_four(12)  => True
# divisible_by_three_and_four(18)  => False
# divisible_by_three_and_four(24)  => True
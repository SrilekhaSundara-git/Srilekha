# Define a three_number_sum function that accepts a 3-character string as an argument. 
# The function should add up the sum of the digits of the string. 
# HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.

def three_number_sum(param):
    #print(int(param[0]))
    return int(param[0])+int(param[1])+int(param[2])
# EXAMPLES:
three_number_sum("123")  # => 6
# three_number_sum("567")   => 18
# three_number_sum("444")   => 12
# three_number_sum("000")   => 0

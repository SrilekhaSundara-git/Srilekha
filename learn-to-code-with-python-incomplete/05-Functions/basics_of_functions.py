# Define a easy_money function that accepts no parameters 
# and always returns the value 100.

def easy_money():
    return 100
easy_money()



# Define a best_food_ever function that accepts 
# no parameters and always returns the string “Sushi”.
def best_food_ever():
    return "Sushi"
best_food_ever()



# Define a convert_to_currency function that accepts a single parameter (an integer). 
# The function should convert the argument to a string, prefix it with a dollar sign, and return the result.
# 
def convert_to_currency(param):
    return "$"+str(param)
convert_to_currency(15)
# EXAMPLES:
# convert_to_currency(15)    => "$15"
# convert_to_currency(8)     => "$8"
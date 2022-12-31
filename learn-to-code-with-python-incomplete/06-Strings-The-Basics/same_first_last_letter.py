# Define a same_first_and_last_letter function that accepts a string as an argument. 
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
def same_first_and_last_letter(param):
    if param[0] == param[-1]:
        return True
    return False

# EXAMPLES:
same_first_and_last_letter("runner")   #=> True
# same_first_and_last_letter("Runner")   => False
# same_first_and_last_letter("clock")    => False
# same_first_and_last_letter("q")        => True
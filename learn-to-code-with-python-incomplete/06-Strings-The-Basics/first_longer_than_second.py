# Define a first_longer_than_second function that accepts two string arguments. 
# The function should return a True if the first string is longer than the second 
# and False otherwise (including if they are equal in length).

def first_longer_than_second(param1, param2):
    if len(param1) > len(param2):
        return True
    return False
#
# EXAMPLES:
first_longer_than_second("Python", "Ruby")  #   => True
# first_longer_than_second("cat", "mouse")       => False
# first_longer_than_second("Steven", "Seagal")   => False

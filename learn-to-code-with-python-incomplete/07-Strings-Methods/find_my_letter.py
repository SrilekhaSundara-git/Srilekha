# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string

def find_my_letter(param1,param2):
    return param1.find(param2)
#
# EXAMPLES:
find_my_letter("dangerous", "a")   # => 1
# find_my_letter("bazooka", "z")      => 2
# find_my_letter("lollipop", "z")     => -1
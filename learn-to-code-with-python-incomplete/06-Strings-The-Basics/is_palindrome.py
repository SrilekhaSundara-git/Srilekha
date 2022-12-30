# Define a is_palindrome function that accepts a string argument. 
# The function should return True if the string is spelled 
# the same backwards as it is forwards. 
# Return False otherwise.
def is_palindrome(params):
    if params[:] == params[::-1]:
        return True
    return False

# EXAMPLES:
is_palindrome("racecar")  # => True
# is_palindrome("yummy")     => False
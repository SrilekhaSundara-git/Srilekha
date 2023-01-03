# Declare a string_theory function that accepts a string as an argument. 
# It should return True if the string has more than 3 characters 
# and starts with a capital “S”. It should return False otherwise.
def string_theory(param):
    return True if param.startswith("S") and len(param) > 3 else False


print(string_theory("Sansa")) #=> True
# string_theory("Story") => True
# string_theory("See") => False
# string_theory("Fable") => False
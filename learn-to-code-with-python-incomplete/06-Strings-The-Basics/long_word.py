# Define a long_word function that accepts a string. 
# The function should return a Boolean that reflects whether the string has more than 7 characters.
# 
# EXAMPLES:
# long_word("Python")         => False
# long_word("magnificent")    => True



def long_word(string_word):
    if len(string_word)>7:
        return True
    return False
    
#word=input('Accept a String')
print(long_word(string_word='Python'))
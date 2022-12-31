# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.

def vowel_count(param):
    vowels = "aeiou"
    #for vowel in vowels:
    #    print(vowel, param.lower().count(vowel))
    return sum([param.lower().count(vowel) for vowel in vowels])
#
# EXAMPLES:
print(vowel_count("estate"))       #=> 3
# vowel_count("helicopter")    => 4
# vowel_count("ssh")           => 0
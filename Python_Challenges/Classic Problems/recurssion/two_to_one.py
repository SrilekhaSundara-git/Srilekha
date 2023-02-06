#Take 2 strings s1 and s2 including only letters from a to z.
#  Return a new sorted string, the longest possible, containing distinct letters - 
# each taken only once - coming from s1 or s2.
#a = "xyaabbbccccdefww"
#b = "xxxxyyyyabklmopq"
#longest(a, b) -> "abcdefklmopqwxy"

#a = "abcdefghijklmnopqrstuvwxyz"
#longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(param1:str, param2:str)->str:
    """
    param1:takes input as a string
    param2:takes input as string
    set elimates the duplicates from param1 and param2 combining the letters avoiding the duplicates
    returns sorted string from both the strings
    """
    return ''.join(sorted(set(param1).union(set(param2))))
print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))
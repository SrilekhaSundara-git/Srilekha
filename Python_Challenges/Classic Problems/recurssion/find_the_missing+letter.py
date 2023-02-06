#Find the missing letter
#Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

#You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
#The array will always contain letters in only one case.

#Example:

import string

def missing_letter(param:list)->str:
    #return set(memo[memo.index(param[0]):memo.index(param[-1])+1])-set(param)
    if all([word.isupper() for word in param]):
        memo = [upper for upper in string.ascii_uppercase]
        return sorted(set(memo[memo.index(param[0]):memo.index(param[-1])+1])-set(param))[0]
    memo = [lower for lower in string.ascii_lowercase]
    return sorted(set(memo[memo.index(param[0]):memo.index(param[-1])+1])-set(param))[0]






print(missing_letter(['a','c','d','e'] ))


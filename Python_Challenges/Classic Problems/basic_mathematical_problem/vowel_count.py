#Return the number (count) of vowels in the given string.

#We will consider a, e, i, o, u as vowels for this Kata (but not y).

#The input string will only consist of lower case letters and/or spaces.

memo: dict  = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0} 

def get_count(sentence):
    memo = {x: 0 for x in "aeiou"} 
    for i in sentence:
        if i in memo:
            memo[i] = memo[i]+1
    return sum(memo.values())
print(get_count('bcdfghjklmnpqrstvwxzaeaeaeaeioouaeioa'))

    


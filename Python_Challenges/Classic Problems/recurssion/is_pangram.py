import string
memo = dict.fromkeys(string.ascii_lowercase, 0)

def is_pangram(n:str)->bool:
    for i in n:
        if i.lower() in memo:
            memo[i.lower()] = memo[i.lower()] +1
    return all(value >= 1 for value in memo.values())
print(is_pangram("The quick, brown fox jumps over the lazy dog!"))


    







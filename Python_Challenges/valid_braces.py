def balance(s):
    for _ in range(len(s)//2):
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return len(s) == 0
    

print(balance("{{{{}}})"))
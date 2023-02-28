def factors(nr):
    i = 2
    factors = []
    while i <= nr:
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    freq = {}
    for char in set(factors):
        #freq[char] = factors.count(char)
        #print(char,factors.count(char)) 
        print('{}{}{}'.format(char,'**',factors.count(char)),end = ' ')
    return ''

    #for key,value in freq.items():
    #    print('{}{}{}{}{}'.format('(',key,'**',value,')'),end="")
        #print(key, value)

print(factors(8))
print(factors(9))
print(factors(86240 ))
def increment_string(strng):
    if strng[len(strng.rstrip('0123456789')):].isdigit():
        add_one = str(int(strng[len(strng.rstrip('0123456789')):])+1)
        return strng[:strng.index(strng[len(strng.rstrip('0123456789')):])]+add_one
    return strng+'1'
        
print(increment_string('foo99'))

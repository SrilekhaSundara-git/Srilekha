#Concatenate the consecutive strings of strarr by 2, we get:
def cons_string(strarr, k):
    """
    """
    for i in range(len(strarr)):
        try:
            print(strarr[i]+strarr[i+1], len(strarr[i]+strarr[i+1]))
        except IndexError:
            print(i+1)

print(cons_string(strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2))
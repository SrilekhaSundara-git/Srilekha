def sum_of_num(n):
    if n == 1:
        return n
    return n+sum_of_num(n-1)
print(sum_of_num(4))
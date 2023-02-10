def sum_of_numbers(list_of_num:list)->int:
    """
    Returns sum of numbers in a list
    >>> sum_of_numbers([1, 2, 3])
    6
    
    >>> sum_of_numbers([10 ,2, 3])
    15
    """
    total = 0
    for num in list_of_num:
        total = num+total
    return total
if __name__ == '__main__':
    import doctest
    doctest.testmod()
#Sort the odd
#You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
#How can I sort ascending the odd numbers in a list of integers, but leaving the even numbers in their original places?

def sort_array(source_array):
    result = sorted([l for l in source_array if l % 2 == 1])
    for index, item in enumerate(source_array):
        if item % 2 == 0:
            result.insert(index, item)
    return result
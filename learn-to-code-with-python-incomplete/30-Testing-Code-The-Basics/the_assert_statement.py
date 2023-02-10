def add(x, y):
    assert isinstance(x, int) and isinstance(y, int), "Values of x and y must be integers "
    return x + y
print(add(1, 2))
print(add(3, '4'))
def return_value(param1=10,param2=20)->int:
    return param1+param2
print(return_value(1, 2))
print(return_value(5, param2=2))
print(return_value(param1=100,param2=200))
print(return_value())


def parent(num:int)->str:
    print("You're inside the parent function")
    def child1()->str:
        return f'{num}, You are in child1'
    def child2()->str:
        return f'{num}, You are in child 2'
    if isinstance(num, int):
        if num == 1:
            print(child2())
        else:
            print(child1())
print(parent(1))

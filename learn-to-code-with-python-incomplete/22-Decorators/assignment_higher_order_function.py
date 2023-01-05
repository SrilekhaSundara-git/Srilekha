
def invoke_thrice(func):
    func()
    func()
    func()

def sample():
    print("A")
    print("B")
    print("C")

def another_sample():
    print("D")
    print("E")

invoke_thrice(another_sample)
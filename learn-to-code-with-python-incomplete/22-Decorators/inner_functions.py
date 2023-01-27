def func():
    print('Inside Parent function')
    def func1():
        print('Inside First Child Function')
    def func2():
        print('Inside Second Child Function')
    func2()
    func1()
func()

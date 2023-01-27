def be_nice(fn):
  def inner():
    print("Nice to meet you! I'm honored to execute your function for you!")
    fn()
    print("It was my pleasure executing your function! Have a nice day!")
  return inner

def complex_business_logic():
  print("Something complex!")

result = be_nice(complex_business_logic)
result()

@be_nice
def decorator_func():
    print('Calling wrapper')

decorator_func()

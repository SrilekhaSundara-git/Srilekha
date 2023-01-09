with open('cupcakes.txt','r') as cupcakes_file:
    print('Opened a file')
    print('')
    content = cupcakes_file.read()
    print(content)
print('')
print('closed cupcakes')
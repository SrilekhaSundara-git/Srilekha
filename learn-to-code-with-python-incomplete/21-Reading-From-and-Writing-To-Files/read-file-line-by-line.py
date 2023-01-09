with open('cupcakes.txt','r') as cupcakes_file:
    print('Opened a file')
    for each_line in cupcakes_file:
        print(each_line.strip())
print('')
print('closed cupcakes')
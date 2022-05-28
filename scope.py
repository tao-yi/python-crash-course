# global variable
name = 'ru'


def print_name():
    # local variable
    # name = 'hello'

    # override the global variable
    global name
    name = 'hey'

    print('inside the function,', name)


print_name()
print('outside the function,', name)

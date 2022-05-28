'''
Python内置了一套try...except...finally的错误处理机制
'''


def div(n: int) -> int:
    r: int
    try:
        print('try...')
        r = 10 / int(n)
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    finally:
        print('finally...')
    print('END')
    return r


print(div('5'))
print(div('a'))
print(div('0'))
print(div(0))


# print(div(0))

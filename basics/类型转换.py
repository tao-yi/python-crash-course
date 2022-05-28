'''
Python中对数据内置的类型进行转换,只需要将数据作为函数名即可。
'''


'''将x转换位一个整数'''
x = '1111'
print(int(x, 2))
# base默认是10
print(int(x, 10), int(x))
x = '0xA'
print(int(x, base=16))

'''将x转换为一个浮点数'''
f = float(1)
print(f)

'''将x转换为一个复数'''
c = complex(1)
print(c)

'''将对象转换为字符串'''
s = 13.0
print(str(s), str(True))


class MyClass:

    def __str__(self) -> str:
        return "MyClass str"

    def __repr__(self) -> str:
        return "MyClass repr"


c = MyClass()
print(str(MyClass), str(c))

'''将对象转换为字符串表达式'''
print(repr(c))


'''用来计算在字符串中的有效Python表达式,并返回一个对象'''
eval("print('hello world')")


l = [1, 2, 3, 4, 5, 6, 7, 7]
'''转换为可变集合'''
s = set(l)
s.add(7)
s.add(9)
s.update({7, 8, 9, 10})
s.remove(7)
print(s)


'''转换为不可变集合'''
f = frozenset(l)

print(f)


'''转换为一个列表'''
l = list(s)
l1 = list(f)
print(l, l1)

'''将一个整数转换为一个字符'''
print(chr(97), chr(65))

'''将一个字符串转为它的unicode code point'''
print(ord('A'), ord('a'))

'''将一个整数转换为一个十六进制字符串'''
print(hex(10))


'''
隐式类型转换: Python会自动将一种数据类型转换为另一种数据类型

Python会将较小的数据类型转换为较大的数据类型
'''

num_int = 123
num_flo = 1.23
num_new = num_int + num_flo
print(type(num_new))

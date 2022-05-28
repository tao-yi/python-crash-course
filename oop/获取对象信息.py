'''
type()判断对象类型
'''

import types

print(type(123) == int)
print(type('123') == str)
print(type(123) == type(234))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x: x) == types.LambdaType)
print(type(lambda x: x) == types.FunctionType)

g = (x for x in range(10))
print(type(g) == types.GeneratorType)
print(isinstance(g, types.GeneratorType))

l = [x for x in range(10)]
print(type(l) == list)
print(isinstance(l, list))

t = (1, 2, 3)
print(type(t) == tuple)
print(isinstance(t, tuple))

'''
如果要获得一个对象的所有属性和方法,可以使用dir()函数
它返回一个包含字符串的list,比如获得一个str对象的所有属性
'''
print(dir('ABC'))

'''
类似 __xxx__ 的属性和方法在Python中都是有特殊用途的
比如 __len__ 方法返回长度, 在Python中如果调用 len() 函数获取一个对象的长度
其实是调用这个对象的 __len__() 方法
'''
print(len('ABC'), 'ABC'.__len__())


class People:
    def __init__(self):
        self.x = 9

    def __len__(self):
        return 5


p = People()
print(len(p))

print(hasattr(p, 'x'))
print(hasattr(p, 'y'))
p.y = 15
print(hasattr(p, 'y'))

setattr(p, 'name', 'MyName')
print(getattr(p, 'name'), p.name, p.__getattribute__('name'))

'''
如果试图获取不存在的属性,会抛出AttribtueError
可以传入一个default参数,如果属性不存在就返回默认值
'''
print(getattr(p, 'size', 404))

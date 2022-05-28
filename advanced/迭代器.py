from collections.abc import Iterable, Iterator

'''
可以直接作用于for循环的数据类型有以下几种:
一类是集合数据类型:list、tuple、dict、set、str等
一类是generator,包括生成器和带yield的generator function

这些可以直接作用于for循环的对象统称为可迭代对象: Iterable
'''


# 可以用isinstance()判断一个对象是否是Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
t = (1,2,3)
print(isinstance(t, Iterable))
print(isinstance('abc', Iterable))
g = (x for x in range(10))
print(isinstance(g, Iterable))

'''
生成器不但可以作用于for循环,还可以被next()函数不断调用并返回下一个值,直到最后抛出StopIteration错误

可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator
可以用isinstance()判断一个对象是否是Iterator对象
'''

print(isinstance([], Iterator))
print(isinstance(g, Iterator))

'''
list,dict,str虽然是Iterable,却不是Iterator
可以用iter()函数将它们变成Iterator
'''
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter((1,2,3)), Iterator))


'''
Iterator对象表示的是一个数据流, Iterator对象可以被next()函数调用并不断返回下一个数据,直到没有数据时抛出StopIteration错误.
可以把这个数据流看做一个有序序列,但我们却不能提前直到序列的长度,只能不断通过next函数按需计算下一个数据,所以Iterator的计算是惰性的。

只有在需要返回下一个数据时它才会计算。
'''

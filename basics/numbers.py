'''
Python Number数据类型用于存储数值
Number类型是不允许改变的,如果改变Number数据类型的值,将重新分配内存空间
'''

import math
from random import random, shuffle, uniform
from secrets import choice

var1 = 1
var2 = 10

# 你可以通过del语句删除一些Number对象引用
del var1, var2


'''
Python3支持int、float、bool、complex

在Python3中只有一种整型int
'''

a: int = 20
b: float = 5.5
c: bool = True
d: complex = 4+3j

print(type(a), type(b), type(d))
print(isinstance(a, int), isinstance(b, float))
print(isinstance(d, complex))

'''
在Python3中, bool是int的子类, True和False可以和数字相加
True == 1
False == 0
'''
print(issubclass(bool, int))
print(isinstance(c, int), isinstance(c, bool))


'''
数值运算
'''
print(5*4)
print(2 // 4)  # 除法,得到一个整数


'''
数学函数
'''

print(abs(-10))  # 返回数字的绝对值
print(math.ceil(4.1))  # 返回数字的向上取整整数
print(math.fabs(-10))  # 返回浮点数字的绝对值,返回float
print(math.floor(10.1))  # 返回浮点数的向下取整数
print(max(1, 2, 3))
print(max([1, 2, 3, 4]), min([1, 2, 3, 4, 5]))
print(max({1, 2, 3, 4, 5}))
print(max((1, 2, 3, 4, 5, 6)))
print(round(4.5))  # 返回四舍五入整数
print(math.sqrt(4))


'''随机数函数'''

# 从序列的元素中随机挑选一个元素
l = [1, 2, 3, 4, 5, 6, 7]
s = {1, 2, 3, 4, 5, 6, 7}
t = (1, 2, 3, 4, 5, 6, 7)
print(choice(l), choice(t))
print(choice(range(10)))
# 随机生成一个 [0,1)之间的浮点数
print(math.floor(random() * 10))

# 将序列的所有元素随机排序, in-placec
shuffle(l)
print(l)

# 随机生成下一个实数,它的范围在 [x,y] 内
print(uniform(5, 10))


x = 5
print(x.bit_length())
print(x.to_bytes(2, 'little'))


print(type(None))

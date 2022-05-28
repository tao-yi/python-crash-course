'''
Python中的functools模块提供了很多有用的功能,其中一个就是偏函数 Partial function

'''


import functools
from typing import Callable

print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))

print(int('110', base=2))

'''
functions.partial帮助我们创建一个偏函数

简单总结functools.partial的作用就是把一个函数的某些参数给固定住(也就是设置默认值)
返回一个新的函数,调用这个新函数会更简单
'''

int2 = functools.partial(int, base=2)
print(int2('111'))


''''
也就是相当于调用
kw = { 'base': 2 }
int('10010', **kw)
'''

print(int('1001', **{'base':2}))



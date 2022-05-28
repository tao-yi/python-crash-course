'''
列表生成式即List Comprehensions
Python内置的用来创建list的生成式

- 列表(list)推导式
- 字典(dict)推导式
- 集合(set)推导式
- 元组(tuple)推导式
'''

import os
from typing import List
from unicodedata import name

'''
列表推导式
'''
# 生成list [1,2,3,4,5,6,7,8,9,10]
print(list(range(1, 11)))

# 生成 [1x1, 2x2, 3x3, ... , 10x10]
l = [x * x for x in range(1, 11)]
print(l)

l = [x * x for x in range(1, 11) if x % 2 == 0]
print(l)

# 两层循环生成全排列
l = [m + n for m in 'ABC' for n in 'XYZ']
print(l)

l = [d for d in os.listdir('.')]
print(l)

'''过滤'''
names: List[str] = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

# 计算30以内可以被3整除的整数
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

l = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(l)


def to_lower(strs):
    return [s.lower() for s in strs if isinstance(s, str)]


print(to_lower(['HELLO', 'WORLD', 18, 32, 'You', '!']))


'''
字典推导式
'''
listdemo = ['Google', 'Runoob', 'Taobao']
newdict = {key: len(key) for key in listdemo}
print(newdict)

'''
集合推导式
'''
newset = {i**2 for i in (1, 2, 3)}
print(newset)
newset = {i**2 for i in [1, 2, 3, 4]}
print(newset)

a = True if 'd' in 'abc' else False
print(a)

'''判断不是abc的字母并输出'''
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


'''
元组推导式
'''
# 返回的是一个生成器对象, 用tuple()函数直接将生成器对象转换成元组
a = tuple((x for x in range(1, 10)))
print(a)

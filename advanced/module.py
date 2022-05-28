#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

'''
Python本身就内置了很多非常有用的模块
'''

import sys


def test():
  args = sys.argv
  if len(args) == 1:
    print('hello world!')
  elif len(args) == 2:
    print(f'Hello, {args[1]}')
  else:
    print('Too many arguments')

'''
当我们在命令行执行hello模块文件时, Python解释器把一个特殊变量__name__设置为__main__
而如果在其他地方导入该hello模块时, if判断将失败。
因此,这种if判断可以让一个模块通过命令运行时执行一些额外的代码。
'''

if __name__ == '__main__':
  test()



'''
作用域:

在一个模块中,正常的函数和变量名是public的,可以被直接访问。
而类似 __xxx__ 这样的变量是特殊变量，可以被直接引用，但是有特殊的作用。
比如 __author__, __name__, __doc__ 这样的就是特殊变量。
'''

print(__doc__)


'''
Python无法限制访问private变量或函数,只能通过命名 _xxx, __xxx 来表示这样的变量不该被别人引用。
'''

def _private_1(name: str)->str :
  return f'Hello, {name}'

def _private_2(name: str)->str :
  return f'Hi, {name}'


def greeting(name: str)->str:
  if len(name) > 3:
    return _private_1(name)
  else:
    return _private_2(name)


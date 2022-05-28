import functools
from datetime import datetime
from typing import Callable

'''
由于函数也是变量,而且函数对象可以被赋值给变量,
所以,通过变量也能调用该函数。
'''

def now()->str:
  return '2015-3-25'

f = now
print(f())

'''
函数对象有一个__name__属性,可以拿到函数的名字
'''
print(now.__name__)

'''
假设我们要增强now()函数的功能,比如在函数调用前后打印日志
但又不希望修改now()函数的定义,这种在代码运行期间动态增加功能的方式称为"装饰器"
'''

# decorator装饰器就是一个返回函数的高阶函数
# decorator接收一个函数作为参数，并返回一个函数
def log(level: str = 'info'):
  def decorator(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      print(f'[{level}] call {func.__name__}() at {datetime.now()}')
      res = func(*args, **kwargs)
      print(f'[{level}] return {func.__name__}() at {datetime.now()}')
      return res
    return wrapper
  return decorator

@log()
def test():
  print("testing func")
  
test()

@log('debug')
def now():
  print(datetime.now())

@log('warning')
def sayHi():
  print('i say hi')

now()
print(now.__name__)
sayHi()

'''
高阶函数除了可以接受函数作为参数外,还可以把函数作为结果值返回s
'''

from typing import Callable


def addNum(n: int)->Callable[[int], int]:
  return lambda x: n + x

print(type(abs))


addOne = addNum(1)
addTwo = addNum(2)

print(addOne(5))
print(addOne(6))
print(addTwo(5))
print(addTwo(6))


def lazy_sum(*args):
  def sum():
    s =  0
    for n in args:
      s = s + n
    return s
  return sum


f = lazy_sum(1,3,5,7,9)
print(f)

'''
闭包
'''
def count():
  fs = []
  for i in range(1,4):
    def f():
      return i * i # 调用f时，i是3，所以每个f都会返回9
    fs.append(f)
  return fs

f1,f2,f3=count()
print(f1(), f2(), f3())


'''
nonlocal
'''

def inc():
  x = 0
  def fn():
    nonlocal x
    x = x + 1
    return x
  return fn

f = inc()
print(f())

'''
Higher Order Function 高阶函数

在Python中变量可以指向函数, 函数名其实就是指向函数的变量.

'''
from functools import reduce
from typing import Any, Callable, Dict, List

x = abs

print(x(-10))

'''
由于abs函数实际上是定义在 import builtins 模块中的
所以要让修改abs的变量的指向在其他模块中也生效, 
要用 builtins.abs = 10
'''
# 把abs指向10后，就无法通过
abs = 10


'''
传入函数:
既然变量可以指向函数,函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数。
这种函数就称为高阶函数。
'''


def add(x, y ,f):
  return f(x) + f(y)

def square(x):
  return x * x

print(add(2,3, square))


'''
map/reduce函数

Python内置了map()和reduce()函数
'''

# 接收一个函数和一个Iterable,并将结果作为新的Iterator返回
# 由于Iterator是惰性序列,因此通过list()函数让它把整个序列都计算出来
r = map(lambda n:n*n, [1,2,3,4,5])
print(list(r))


r = list(map(str, [1,2,3,4,5,6,7,8,9]))
print(r)

print(str(False) == 'False')

def f(x: int, y:int):
  return x * 10 + y

'''
reduce把一个函数对序列中的每个元素进行调用
并将返回值作为下一个调用的第一个元素
'''
print(reduce(f, [1,3,5,7,9]))
# 提供一个初始的返回值
print(reduce(f, [1,3,5,7,9], 0))

print(sum([1,2,3,4,5]))


'''
filter()函数用于过滤序列
'''
l = [1,2,3,4,5,6,7,8,9]

def is_odd(n: int)->bool:
  return n % 2 == 1

print(list(filter(is_odd, l)))

def not_empty(s: str)->bool:
  return s and s.strip()

print(list(filter(not_empty, ['A','','B',None,'C', '  '])))


'''
sorted()函数可以对list进行排序
它可以接受一个key函数来实现自定义的排序
'''
print(sorted([3,2,5,9,2,1]))
# key指定的函数将作用于list的每一个元素上,并根据key函数返回的结果进行排序
print(sorted([36,5,-12,9,-21], key=square))

# 实现忽略大小写的排序
print(sorted(['bob','about','Zoo','Credit'], key=str.lower))

# 实现反向排序
print(sorted(['bob','about','Zoo','Credit'], key=str.lower, reverse=True))

# 实现自定义排序
pokemons: List[tuple[str, str, int]] = [
  ('Charmander', 'Fire', 52),
  ('Blastoise', 'Water', 83),
  ('Breedrill', 'Poison', 90)
]

print(sorted(pokemons, key=lambda x: x[2]))

'''
当我们在传入参数的时候，有些时候，不需要显式地定义函数。
直接传入匿名函数更方便。

在Python中,对匿名函数提供了有限支持。
'''


print(list(map(lambda x: x*x, [1,2,3,4,5,6])))

'''
关键字lambda表示匿名函数,冒号前面的x表示函数参数

匿名函数有个限制,就是只能有一个表达式,不用写return
'''

def build(x:int,y:int)->Callable[[], int]:
  return lambda: x*x+y*y

f = build(2,3)
print(f())


class Pokemon:
  def __init__(self, name:str,category:str,attack:int) -> None:
      self.name = name
      self.category = category
      self.attack = attack
    
  def __repr__(self) -> str:
      return repr((self.name, self.category, self.attack))

pokemon_objects: List[Pokemon] = [
  Pokemon('Beedrill', 'Posion', 90),
  Pokemon('Charmander', 'Fire', 52),
  Pokemon('Blastoise', 'Water', 83),
]

print(sorted(pokemon_objects, key=lambda x: x.attack))





import math

'''
Python内置了很多函数,包括类型转换函数
abs()
max()
'''
num = -100
print(abs(num))
print(max(1,2,3,4,5,9))
nums = (11,5,21,3)
print(max(nums))
nums = [11,5,21,3]
print(max(nums))

print(int('123'))
print(str(123))
print(int(12.5))
print(float('12.32'))
print(bool(1))
print(bool(0))
print(bool('A'))
print(bool(''))
print(bool(None))
print(bool([]))
d = {}
print(bool(d))
print(bool([1,2]))
print(bool((1,2)))
print(hex(9))


def my_abs(x):
    if not isinstance(x, (int, float)):
      raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

my_abs(5)

def say_hello(name='Sam'):
    return f'Hello {name}'


def getSum(num1, num2):
    total = num1 + num2
    return total

'''
空函数:如果想定义一个什么事也不做的空函数,可以用pass语句
'''
def nop():
    pass
# 相当于返回一个None
def nop():
    return None

print(nop())
print(say_hello())
print(getSum(1, 5))
print(my_abs(-5))

'''
返回多个值:其实只是一种假象,Python函数返回的仍然是单一值
返回值是一个tuple,但是在语法上,返回一个tuple可以省略括号
'''
def move(x, y, step, angle = 0):
  nx = x + step * math.cos(angle)
  ny = y - step * math.sin(angle)
  return nx, ny # 返回一个tuple

x, y = move(100,100,60, math.pi/6)
print(x,y)

'''
lambda function 匿名函数
'''
add = lambda num1, num2 : num1 + num2

print(add(1,5))



'''
默认参数
必选参数在前,默认参数在后
'''
def power(x, n=2):
  s = 1
  while n > 0:
    n -= 1
    s *= x
  return s
print(power(4), pow(10,2))

def enroll(name, gender, age=6,city='Beijing'):
  return f'{name} {gender} {age} {city}'

print(enroll('Adam', 'M', city='Shanghai'))
print(enroll('Adam', 'M', 5))

'''
默认参数有一个最大的坑:
Python函数在定义的时候,默认参数L的值就被计算出来了,即[]
因为默认参数L也是一个变量,它指向对象[],每次调用该函数,如果改变了L的内容
则下次调用时,默认参数的内容就变了
'''
def add_end(L=[]):
  L.append('End')
  return L

print(add_end())
print(add_end())
print(add_end())

'''
默认参数必须指向不可变对象,比如str,None,int
'''

def add_end(L=None):
  if L is None:
    L = []
  L.append('END')
  return L

print(add_end())
print(add_end())
print(add_end())

'''
可变参数:在函数调用时自动组成为一个tuple
'''
def calc(*numbers):
  sum = 0
  # 在函数内部，numbers是一个tuple
  for n in numbers:
    sum = sum + n * n
  return sum

print(calc(1,2))
print(calc())
# Python允许你在list或者tuple前面加一个*号，把元素作为可变参数传进去
nums = [1,2,3,4]
print(calc(*nums))

'''
关键字参数
允许你传入0个或任意个含参数名的参数
这些参数在函数内部自动组装成一个dict
'''
def person(name, age, **kw):
  if 'city' in kw:
    pass
  if 'job' in kw:
    pass
  if 'friends' in kw:
    kw['friends'].append(6)
  return f'name:{name},age:{age},{kw}'


print(person('Adam',35,gender="M",job="Enginner"))

'''
**extra表示把extra这个dict的所有key-value作为关键字参数传入到函数的**kw参数
kw获得的是dict的一份浅拷贝
'''
extra = {'city':'Beiging', 'job': 'Enginner', 'friends': [1,2,3,4,5]}
print(person('Adam', 24, **extra))


'''
命名关键字参数

如果要限制调用者传入的关键字参数，就可以用命名关键字参数
'''

# 只接受city和job作为关键字参数，传入其他参数会报错
def person(name, age, *, city, job):
  return f'{name}, {age},{city},{job}'

print(person('AdM', 35, city='Beijing', job='Engineer'))
d = {'city': 'Beiging', 'job': 'Enginner'}
print(person('Adm', 35, **d))

# 不传city会报错
# print(person('AdM', 35, job='Engineer'))
# 不传job会报错
# print(person('AdM', 35, city='Beijing'))
# 传入其他参数会报错
# print(person('Adam', 35, id=216))



'''
命名关键字参数可以有默认值
'''
def person(name, age, *, city='Beijing', job):
  print(name, age, city, job)

person('Jack', 24, job='Enginner')


'''
参数组合
'''
def f1(a,b,c=0,*args,**kw):
  print(f'a={a},b={b},c={c},args={args},kw={kw}')

f1(2,2,5,11,12,13)

def f2(a,b,c=0,*,d,**kw):
  print(a,b,c,d,kw)
f2(1,2,d=5,name='hello',age=26)

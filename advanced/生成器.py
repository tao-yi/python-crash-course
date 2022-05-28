# 通过列表生成式，我们可以直接创建一个列表，但是受到内存你限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的内存空间，
# 而且如果我们只访问前面的几个元素，那么后面大多数元素占用的空间都浪费了。
# 在Python中，一遍循环一遍计算的机制，称为生成器：generator。

'''
要创建一个generator有很多种方法。
第一种方法很简单，只要把列表生成式的[]改成()就可以了。
'''

L = list(range(10))
print(L)
L = [x * x for x in range(10)]
print(L)

# g是一个generator对象
g = (x * x for x in range (10))
print(g)
# 每次调用next，就计算出g的下一个元素的值
print(next(g))

for n in g:
  print(n)

'''
定义生成器的另一种方法:
如果一个函数定义中包含yield关键字,那么这个函数就不再是一个普通函数,而是一个generator函数
调用一个generator函数将返回一个generator对象
'''
def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n = n + 1
  return 'done'

'''
generator函数和普通函数的执行流程不一样。
普通函数是顺序执行,遇到return语句或者最后一行函数就返回.
而变成generator的函数, 在每次调用next()的时候执行,遇到yield语句就返回,再次执行时从上次yield的语句处继续执行.
'''
for n in fib(10):
  print(n)

def odd():
  print('step 1')
  yield 1
  print('step 2')
  yield(3)
  print('step 3')
  yield(5)
  
g = odd()
for n in g:
  print(n)

'''
但是用for循环调用generator时,拿不到generator函数return语句的返回值。
如果想拿到返回值,必须捕获StopIteration错误,返回值包含在StopIteration的value中:
'''
g = fib(6)
while True:
  try:
    x = next(g)
    print('g:',x)
  except StopIteration as e:
    print('Generator return value:', e.value)
    break
  

l = [None] * 5
print(l)



'''
除了 __slots__ 属性和 __len__ 方法之外
Python中的class还有许多这样有特殊用途的函数,可以帮助我们定制类
'''


class Student:
    def __init__(self, name):
        self.name = name

    '''
    返回用户看到的字符串
    '''

    def __str__(self) -> str:
        return f'Student object (name:{self.name})'

    '''
    返回程序开发者看到的字符串,为调试服务的
    '''
    __repr__ = __str__


s = Student('Michael')
print(s)
print(s.__repr__())

'''
如果一个类想被用于for...in循环
就要实现一个__iter__()方法,该方法返回一个迭代对象
'''


class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    # 实例本身就是迭代对象,所以返回自己
    def __iter__(self):
        return self

    # for循环会不断调用该迭代对象的__next__()方法
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)

'''
虽然Fib实例能作用于for循环,看起来和list有点像,但是,把它当成list来使用还是不行
比如取第5个元素, Fib()[5]
如果要像List一样取出元素,需要实现 __getitem__() 方法
'''


class Fib:
    def __getitem__(self, n: int) -> int:
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a


f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[5])

'''
__getattr__
正常情况下,当我们调用类的方法或者属性时,如果不存在,就会报错

为了避免这个报错,可以写一个__getattr__方法,动态返回一个属性
'''


class Student:
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr: str):
        if attr == 'score':
            return 99
        raise AttributeError("'Student' object has no attribute '%s'" & attr)


s = Student()
# 在没有找到属性的情况下,才会调用__getattr__
# 已有的属性,比如name,不会调用__getattr__
print(s.name, s.score, s.__getattr__('score'))

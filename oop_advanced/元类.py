'''
动态语言和静态语言最大的不同,就是函数和类的定义不是编译时定义的,
而是运行时动态创建的

当Python解释器载入hello模块时,就会依次执行该模块的所有语句
'''


class Hello:
    def hello(self, name="world"):
        print('Hello %s' % name)


h = Hello()
h.hello()


print(type(Hello))
print(type(h))

'''
type()函数可以查看一个类型或变量的类型
我们说class的定义是运行时动态创建的,而创建class的方法就是使用
type()函数

type()函数既可以返回一个对象的类型,又可以创建出新的class类型

当Python解释器遇到class定义时,仅仅是扫描一下class定义的语法,
然后用type()函数创建出class
'''


def fn(self, name='world'):
    print('Hello, %s' % name)


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()

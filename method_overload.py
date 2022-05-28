
import types


class A:
    def __init__(self):
        self._age = 1
        self.__name = 2


a = A()
A.address = 'hello'


def test(self):
    print('new test')


a.test = types.MethodType(test, a)

a.test()

print(a._age)

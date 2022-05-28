'''
正常情况下,当我们定义了一个class,创建了一个class的实例后,
我们可以给该实例绑定任何属性和方法,这就是动态语言的灵活性。
'''


from types import MethodType


class Student:
    pass


s = Student()
s.name = 'James'
print(s.name)

# 还可以尝试给实例绑定一个方法


def set_age(self, age: int):
    self.age = age


# 给实例绑定一个方法
s.set_age = MethodType(set_age, s)

s.set_age(25)
print(s.age)

# 但是给一个实例绑定的方法在另一个实例上是没有的
# 为了给所有实例都绑定方法,可以给class绑定方法:


def set_score(self, score: int):
    self.score = score


# 给class绑定方法后，所有实例都可调用
Student.set_score = set_score

s1 = Student()
s2 = Student()
s1.set_score(15)
s2.set_score(21)
print(s1.score, s2.score)

'''
但是如果我们想要限制实例的属性怎么办？
比如,只允许对Student实例添加name和age属性

为了达到限制的目的,Python允许在定义class的时候,定义一个特殊的__slots__变量
来限制该class实例能添加的属性
'''


class Student:
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
s.age = 25
# 绑定属性失败,由于score没有放在__slots__中，所以不能绑定score属性
# __slots__定义的属性仅对当前实例起作用,对继承的子类是不起作用的
# s.score = 99
print(s)


class GraduateStudent(Student):
    # 只有当子类也声明了__slots__的情况下，父类的__slots__才会起作用
    __slots__ = ()
    pass


g = GraduateStudent()
# g.height = 175
g.age = 15
g.name = 16
print(g)

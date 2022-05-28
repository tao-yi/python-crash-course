'''
Python提供了Enum类
'''


from enum import Enum, EnumMeta, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr'))

print(Month.Jan)


for name, member in Month.__members__.items():
    print(name, member)

print(type(Month))
print(isinstance(Month, EnumMeta))


'''
value属性是自动赋给成员的int常量,默认从1开始奇数
如果需要更精确地控制枚举类型,可以从Enum派生出自定义类
'''

# unique装饰器帮助我们检查没有重复的value


@unique
class Weekday(Enum):
    Sum = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1.name, day1.value)

for name, member in Weekday.__members__.items():
    print(name, member, member.value)


class Gender(Enum):
    Male = 0
    Female = 1


class Student:
    def __init__(self, name: str, gender: Gender):
        self.name = name
        self.gender = gender


s = Student('Adam', Gender.Male)
print(s.gender)

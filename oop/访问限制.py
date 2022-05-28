'''
在Class内部可以有属性和方法
如果要让内部属性不被外部访问,可以把属性的名称前加上两个下划线__
在Python中如果属性名以__开头,就变成了一个私有变量(private)
只有内部可以访问,外部不能访问s
'''

class Student:
    def __init__(self, name: str, score: int):
        # 私有成员变量
        self.__name = name
        self.__score = score

    def __private_f(self):
        return "private_f"

    def public_f(self):
        print("call public_f()")
        self.__private_f()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val: str):
        self.__name = val

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val: int):
        if 0 <= val <= 100:
            self.__score = val
        else:
            raise ValueError('bad score')


s = Student('James', 97)
s.public_f()

# 报错: Student对象中不存在__name属性
# 因为__name是private的
# print(s.__name)

print(s.name)
s.name = 'NewName'
print(s.name)

s.score = -10
print(s.score)

'''
双下划线开头的实例变量其实也能够访问到
Python解释器对外把 __name 变量改成了 _Student__name
但是强烈建议不要这么做, 因为不同版本的Python解释器可能会把 __name 改成不同的变量名
'''
print(s._Student__name)
print(s._Student__private_f())

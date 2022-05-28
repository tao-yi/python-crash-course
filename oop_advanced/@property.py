'''
Python内置的@property装饰器就是负责把一个方法变成属性调用的
'''


class Student:

    def __init__(self, birth: str = 'A', score: int = 1) -> None:
        self._birth = birth
        self._score = score

    '''把一个getter方法变成属性'''
    @property
    def score(self):
        return self._score

    '''@property又创建了另一个装饰器 @score.setter
    负责把一个setter方法变成属性赋值'''
    @score.setter
    def score(self, value: int):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    '''定义只读属性,没有setter'''
    @property
    def birth(self):
        return self._birth


s = Student()
# 实际转化为s.set_score(60)
s.score = 60
print(s.score)
print(s.birth)

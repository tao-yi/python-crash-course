'''
Mixin

在设计类的继承关系时,通常都是单一继承下来的。
但是如果需要混入额外的功能,通过多重继承可以实现。
这种设计通常称为MixIn
'''


class Animal:
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable:
    def run(self):
        return 'Running...'


class Flyable:
    def fly(self):
        return 'Flying...'


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird):
    pass

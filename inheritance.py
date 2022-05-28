class Parent(object):
    def __init__(self, name):
        print("Parent init")
        self.name = name


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print("Son1 init")
        super().__init__(name, *args, **kwargs)
        self.age = age


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print("Son2 init")
        super().__init__(name, *args, **kwargs)
        self.gender = gender


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender, job):
        print('Grandson init')
        super().__init__(name, age, gender)
        self.job = job


# super具体调用哪个父类取决于__mro__的顺序
print(Grandson.__mro__)
print(Grandson.mro())
s = Grandson('Name', 1, 'Male', 'Engineer')
print(Grandson.__base__)
print(Grandson.__bases__)

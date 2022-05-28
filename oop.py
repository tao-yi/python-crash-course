class Person:

    max_age = 100

    __sex = 0

    def __init__(self, name):
        self.name = name

    def say(self, greet: str):
        print(f'{self.name} says {greet} {self.max_age} {self.__sex}')

    @staticmethod
    def static_f():
        print(Person.max_age, Person.__sex)

    @classmethod
    def class_f(cls):
        print(cls)


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade


a = Person('A')
b = Person('B')
print(Person.max_age)
print(id(a.max_age))
print(id(b.max_age))
print(id(Person.max_age))

print(id(a.say))
print(id(b.say))


a.static_f()
Person.static_f()

a.class_f()
Person.class_f()

s = Student('s1', 16)
s.say('he')

print(id(a.static_f), id(Person.static_f), id(s.static_f))

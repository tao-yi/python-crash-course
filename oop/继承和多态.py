class Animal:
  def run(self):
    return 'Animal is running...'

class Cat(Animal):
  def run(self):
    return 'Cat is running...'


class Dog(Animal):
  def run(self):
    return 'Dog is running...'


class Other(Animal):
  pass


a = Animal()
c = Cat()
d = Dog()
o = Other()

print(a.run())
print(c.run())
print(d.run())
print(o.run())

print(isinstance(a, Animal))
print(isinstance(d, Animal), isinstance(d, Dog))
print(type(d) == Animal, type(d) == Dog)
print(isinstance(c, Animal), isinstance(c, Cat))
print(type(c) == Animal, type(c) == Cat)
print(isinstance(o, Animal))

print(issubclass(Cat, Animal))


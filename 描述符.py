class A:
    def __init__(self, name):
        self.name = name

    def __getattr__():
        pass


a = A('小明')
print(a.name)
print(a.age)

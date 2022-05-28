'''
由于Python是动态语言,根据类创建的实例可以绑定任意属性
'''


class Student:
    # 如果Student类本身需要绑定一个属性呢?
    # 可以直接在class类中定义属性，这个属性归Student类所有
    # 但是每个实例都可以访问到
    name = 'Student'

    def __repr__(self) -> str:
        s = ""
        for k, v in self.__dict__.items():
            s += f'{k}:{v}\n'
        return s


s = Student()
s.name = "Bob"
s.age = 15

print(s)

# 因为实例没有name属性，所以会继续查找class的name属性
print(s.name)

# 给实例绑定name属性，由于实例属性优先级比类属性高
# 实例属性会屏蔽掉类属性
s.name = 'myname'
print(s.name)
# 删除实例属性, 此时会访问到雷属性
del s.name
print(s.name)

print(Student.name)
print(Student.mro())

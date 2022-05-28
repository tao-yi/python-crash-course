'''
list和tuple是Python内置的有序集合, list元素可变, tuple元素不可变

tuple和list非常类似,但是tuple一旦初始化就不能修改
因为tuple不可变,所以代码更安全,如果能用tuple代替list就尽量用tuple
'''

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates.count('Bob'), len(classmates))


# 当你定义一个tuple时，在定义的时候tuple的元素就必须被确定下来
t = tuple((1, 2))
t = (1, 2, 3, 4, 5)
# 结构
a,b,c,d,e = t
print(t, type(t), t[0], t[1])
print(a,b,c,d,e)

# 如果要定义一个空的tuple，可以写成 ()
t = ()
print(len(t))

# 如果要定义只有一个元素的tuple
t = (1)  # t是int类型
print(type(t))

t = (1,)
print(type(t), len(t))

# 所谓tuple不可变的意思是说，tuple的每个元素指向永远不变
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)


# 删除tuple
fruits = ("Apple", "Orange")

del fruits

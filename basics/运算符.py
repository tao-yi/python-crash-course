'''幂运算符'''
from subprocess import list2cmdline

a = 2
# 计算a的4次方
print(a ** 4)


'''整除运算符:向下取整'''
print(5 // 2)


'''海象运算符: Python3.8版本新增运算符'''
# 赋值表达式可以避免调用len两次
a = "abcdefg"
if (n := len(a)) > 5:
    print(f'List is too long with {n} elements, expected <= 5')


'''按位与:如果两个相应的位都为1,则该位的结果为1,否则为0'''
a = 60  # 0011 1100
b = 13  # 0000 1101
#         0000 1100
print(a & b)

'''按位或:只要两个位有一个位为1,则该位的结果为1,否则为0'''
#         0011 1101
print(a | b)

'''按位异或:如果两个位不同时,则该位的结果为1,否则为0'''
#         0011 0001
print(a ^ b)

'''按位取反:对每个二进制位取反'''
print(~a, ~b)


'''
逻辑运算符
'''
a = 10
b = 20
if a and b:
    print(True)

if a or b:
    print(True)

a = 0
if not(a and b):
    print('a和b不都为true, 有一个为false')

'''
成员运算符
'''
a = 10
b = 20
l = [1, 2, 3, 4, 5, 10]
if a in l:
    print(f'a={a} 在list{l}中')

if b not in l:
    print(f'b={b} 不在在list{l}中')

d = {"a": 1, "b": 2}
if 'a' in d:
    print(True)


'''
identity运算符

用于比较两个对象的存储单元
is 用于判断两个标识符是不是引用同一个对象
'''
x = 20
y = 20
# id函数用于获取对象的内存地址
print(x is y, id(x) == id(y))

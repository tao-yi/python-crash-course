
"""
Python有6个标准的数据类型:
1. Number
2. String
3. List
4. Tuple
5. Set
6. Dictionary

Python的6个标准数据类型中:
3个不可变数据: Number, String, Tuple
3个可变数据: List, Dictionary, Set
"""

x = 1           # int
y = 2.5         # float
name = 'John'   # str
is_cool = True  # bool
print(type(name))

# Multiple Assignment
a, b = 3, 4
b, a = a, b
print(a, b)

x, y, name, is_cool = (1, 2.5, "John", True)
print(x, y, name, is_cool)

# Type Casting
x = str(x)
print(x, type(x))
x = float(x)
print(x, type(x))
x = bool(x)
print(x, type(x))

# 常量
#  在Python中常量通常全部用大写的变量名表示
PI = 3.14159265359
# "/" 除法计算结果是浮点数
print(PI / 3)
print(4 / 2)
# "//" 除法只取整数部分
print(10 // 3)
print(5 >> 1)

# 条件判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 循环
names = ('A', 'B', 'C')
for name in names:
    print(name)

# 生成一个有序数列
for i in range(5):
    print(i)

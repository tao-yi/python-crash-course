'''
在Python 3版本中, 字符串是以unicode编码的
'''
name = "你好"
# ord函数返回unicode code point
print(ord('A'))
print(chr(65))

'''
Python的字符串类型是str, 在内存中以unicode表示, 一个字符对应若干个字节
如果要在网络上传输或者保存到磁盘上，就需要把 str 变为以字节为单位的 bytes
'''
x = b'ABC'
print(type(x))

print('中文'.encode('utf8'))
print('ABC'.encode('ascii'))


'''
相反如果我们从网络或磁盘上读取了字节流,那么读到的数据就是bytes.
要把bytes变成str,就需要使用decode()方法
'''
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

'''
计算字符串包含多少个字符
'''
print(len('ABC'))
print(len('中文'))

'''
计算字符串包含多少个字节
'''
print(len('中文'.encode('utf8')))


# concatenate
name = "Brad"
age = 37

print("Hello, my name is " + name + " and I am " + str(age))

# string formatting
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (Python3.6+)
print(f'Hello my name is {name} and I am {age}')

s = "hello world"
print(s.capitalize())
print(s.upper())
print(s.upper().lower())

print(".".join("abc"))
print(s.startswith('h'))
print(s.find("w"))
print(s.split(" "))
print(s.isalnum())
print(s.count('o'))


# 多行字符串
a = '''line1
line2
line3'''


print(a)

# 转义
print('this is a line with \n')
# 使用r可以让反斜杠不发生转义
print(r'this is a line with \n')
# 字符串可以用*运算s
s = 'a'*5
print(s)

for char in s:
    print(char, ord(char))


print(ord('A')-ord('B'))

s = "abcdefg"
s1 = s[2:5]
print(s, s1)

print('---', end="")
print('!!!')


'''
多行字符串
'''
# r表示原始字符串,所有字符串都按字面量使用，不会转义
multi_line = r"""
hello\t
world\n
你\n
好\c
%s
{}
"""
name = "world"

multi_line = f"""
{name}\\n
"""

print(multi_line)

s = "a"
print(id(s))
s += "b"
print(id(s))


i = 1
print(id(i))
i += 1
print(id(i))


print(dict.fromkeys([1, 2, 3, 4, 5]))
print(dict.fromkeys(['a', 'b']))
# Key必须是不可变的, 所以只能是数字,字符串或者元组
print(dict.fromkeys([(1, 2, 3)]))


d = {"a": 1, "b": 2}
k, v = d.popitem()
print(k, v)

'''
当我们试图加载一个模块时,Python会在指定的路径下搜索对应的.py文件
如果找不到,就会报错。

默认情况下,Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块,搜索路径放在sys模块的path变量中
'''
import sys

import module as m

print(m.greeting('hello world'))

m._private_1('hel')
m._private_2('hel')

print(m.__doc__)
print(m.__name__)
print(m.__file__)
print(m.__spec__)

print(sys.path)

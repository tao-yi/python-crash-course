'''
list是一种有序的集合
'''

# Create list
from distutils import file_util
from typing import List

from requests import delete

numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers == numbers2)

# Get a value
print(fruits[1])
print(len(fruits))

# Update
fruits[0] = 'Blueberries'

fruits.append("Mangas")
fruits.remove("Grapes")
fruits.insert(2, 'Strawberries')
print(fruits)

fruits.pop(0)
print(fruits)

fruits.remove('Strawberries')
print(fruits)

del fruits[0]
print(fruits)

for f in fruits:
    print(f)

fruits.reverse()
print(fruits)

# sort list
fruits.sort()
fruits.sort(reverse=True)

print(fruits)

# list元素可以是另一个list
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s, s[2][1])

p = [1]*5

print(p)


a = [1, 2, 3]
b = ['a', 'b', 'c']
# 连接两个list
c = a + b
print(c)


a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8, 9], [10, 11, 12]]
# c是a和b的浅拷贝拼接在一起
c = a + b
print(c)
# 修改c也会修改a
c[0].append(5)
print(c)
# 修改a也会修改c
a[0].append(111)
print(c)


def print2DList(l: List[List[int]]):
    print("start print2DList")
    for row in l:
        print("[", end=" ")
        for num in row:
            print(num, end=" ")
        print("]")
    print("end print2DList")


print2DList(c)


# d是两个a的浅拷贝拼接在一起
d = a * 2
d[1].append(7)
print(d)
print(a)


l = [1, 2, 3, 4, 5]

l1 = l[2:4]
# 修改l1和l互不影响s
l[2] = 9
l1[0] = 12
print(l1, l)


def reverseWords(input: str) -> str:
    # 通过字符串分割,把各个单词分割为列表
    inputWords = input.split(" ")
    # 翻转字符串
    inputWords = inputWords[-1::-1]
    output = "".join(inputWords)
    return output


print(reverseWords("hello, world!"))

print(('hi',)*4)

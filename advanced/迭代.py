from collections.abc import Iterable

d = {
  'a':1,
  'b':2,
  'c':3
}


for key in d:
  print(f'{key}:{d[key]}')


# 迭代 values
for value in d.values():
  print(value)

# 同时迭代key和value
for k, v in d.items():
  print(k,v)
  

# 由于字符串也是可迭代对象，因此也可以作用于for循环
for char in "ABCDEFG":
  print(char)


print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance((1,2,3), Iterable))
print(isinstance({'a':1}, Iterable))
print(isinstance(123, Iterable))

'''
如果要对list实现类似Java那样的下标循环怎么办
Python内置的enumerate函数可以把一个list变成索引-元素对
'''
for i, value in enumerate(['A','B','C']):
  print(i, value)


def findMaxAndMin(*numbers):
  min_value = float('inf')
  max_value = float('-inf')
  for num in numbers:
    if num >= max_value:
      max_value = num
    if num <= min_value:
      min_value = num
  return min_value,max_value

print(findMaxAndMin(*[1,2,3,4,5,6,7,8,9]))


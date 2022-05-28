'''
Python提供了切片操作符

取前N个元素
'''

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L1 = L[:3]
print(L1)
#  从倒数第2个元素开始取
L2 = L[-2:]
print(L2)

L = list(range(100))
# 前10个数，每隔两个取一个
print(L[:10:2])
# 每5个数取1个
print(L[::5])

# 复制一个list
clone = L[:]
print(clone == L)
print(clone is L)

# tuple也是一种list，唯一区别是tuple不可变，因此tuple也可以用切片操作
t = (1,2,3,4,5)
t1 = t[:]
print(t == t1)
print(t is t1)


# 字符串也可以看成是一种list，每个元素就是一个字符
s = "ABCDEFG"
s2 = "ABCDEFG"
s1 = s[1:-1]
print(s1, s1[0], s1[2])
print(s == s2)
print(s is s2)


def trim(s):
  i,j = 0,len(s)-1
  while i < j:
    if s[i] != " " and s[j] != " ":
      break
    if s[i] == " ":
      i+=1
    if s[j] == " ":
      j-=1
  return s[i:j+1]

print(trim('  abc  '))

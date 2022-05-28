'''
Python内置了字典: dict,在其他语言中称为map

dict的存放顺序和插入顺序没有关系, 它是无序的。
'''

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85,
    1: 35,
    2: False
}

d['H'] = 15
print(d, type(d))
print(d['Michael'])

'''检查dict中是否包含某个key'''
print('Thomas' in d, 'Michael' in d)
print(d.get('C') == None)

print(d.keys())
print(d.values())

'''如果key不存在返回一个默认值-1'''
print(d.get('C', -1))

'''删除一个key'''
d.pop('H')

'''删除整个字典'''
del d

'''用键值对列表构建dict'''
d = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(d['Runoob'])

'''用推倒式构建dict'''
d = {x: x**2 for x in (2, 4, 6)}
print(d)


'''
set和dict类似,也是一组key的集合,但是不存储value
可以使用大括号 { }  或者 set() 函数创建集合

创建一个空集合必须用set() 而不是 { }
因为 { } 表示创建一个空字典
'''

s = {}
print(type(s))
s = set()
print(type(s))
s = {1, 1, 1, 2, 2, 3, 5}
print(s, type(s))

l = [1, 1, 2, 3, 4, 4, 5]
s = set([1, 1, 2, 3, 2, 3])

'''添加元素'''
s.add('6')
s.add(6)
print(s, type(s), len(s))
s = set(l)
print(s)

# 还可以通过update添加多个元素
s.update({1, 2, 3})
s.update([9, 8, 7])
s.update([11, 12], [13, 14])
print(s)

s.remove(1)
print(s)
s.clear()
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

'''交集'''
s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)

'''并集'''
s3 = s1 | s2
s3 = s1.union(s2)
print(s3)

'''差集'''
s3 = s1.difference(s2)
s3 = s1 - s2
print(s3)
s3 = s2.difference(s1)
s3 = s2 - s1
print(s3)

'''不同时存在的元素'''
s4 = s1 ^ s2
print(s4)


print(set([1, 2, 3]).issubset(set([1, 2, 3, 4])))

del s3

# 拷贝
p1 = {'name': 'p1', 'age': 26, 'friends': [1, 2, 3]}
# p2是p1的浅拷贝
p2 = p1.copy()
p2['name'] = 'p2'
p1['friends'][0] = 5

del(p1['friends'])
p2.pop('friends')
print(p1, p2, len(p1))

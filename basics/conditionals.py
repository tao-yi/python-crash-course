x = 5
if x > 2 and x <= 10:
  print(f'{x} is greated than 2 and less than or equal to 10')

if x > 2 or x <= 0:
  print(f'{x} is greated than 2 and less than or equal to 0')
  
x = 1
if not(x > 2 or x <= 0):
  print(f'{x} is greated than 2 and less than or equal to 0')
  

x = 5
if (x == 1 or x == 2) or (x == 5 or x == 6):
  print(True)


if x in [1,2,3,4,5]:
  print(x in [1,2,3,4,5])

if x not in [6,7,8,9]:
  print(x not in [6,7,8,9])
  
x = [1,2,3]
y = [1,2,3]
# 判断两个对象的内容是否相同
print(x == y)
# 判断两个对象是否指向相同的地址
print(x is y)



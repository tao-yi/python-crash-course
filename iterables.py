iterables = [
    "123",             # 字符串
    [1, 2, 3],           # 列表
    (1, 2, 3),           # 元组
    {1: 'a', 2: 'b'},  # 字典
    {1, 2, 3},           # 集合
]

for iterable in iterables:
    print(type(iterable))
    for x in iterable:
        print(x, end=",")
    print("")

"""
README
这段代码简单介绍了
    1.成员运算符
"""

a=[1,2,3] #[]表示一个集合(以后会讲)
b='strong'
print(1 in a) #判断 整数1 是否在 集合a 中(结果为True)
print('st' not in b) #判断 字符串st 是否不在 字符串b 中(结果为False)
print('sr' not in b) #判断 字符串sr 是否不在 字符串b 中(结果为True)
print(9 // 2 ** 2 % 3 and 5 + 1)
print(not (((15 / 2) + 2) >= 3) or 8 * 3)
print('--------------------------------------')
print(0 and 6)
print(0 or 6)
print(not 6)
"""
README
这段代码简单介绍了
    1.print
    2.'''
    3.=
    4.if/else
    5.type
"""

print("Hello,world!") # 输出(内容)

''' #表示整段注释(1/2)
print('不会输出这里的内容')
''' #表示整段注释(2/2)

a=5 #把变量a赋值为整数(int)5
b=6.8 #把变量b赋值为浮点数(float)6.8
print(type(a)) #输出 获取的a对象的数据类型
print(type(b)) #输出 获取的b对象的数据类型

if a>b: #条件判断(a是否大于b)
    print('结果为True') #如果结果为True,则执行这里的所有代码
    print('a大于b')
else:
    print('结果为False') #如果结果为False,则执行这里的所有代码
    print('a小于等于b')
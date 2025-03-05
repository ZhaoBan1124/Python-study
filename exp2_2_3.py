"""
README
这段代码简单介绍了
    1.比较运算符
    2.逻辑运算符
"""
#比较运算符(>、<)优先级高于逻辑运算符(and、or、not)
#逻辑运算符优先级(not>and>or)

print(2 > 3.3 and 4 or 5 and 4 < 3 or not 4 > 5)
'''
判断步骤
1.(False and True or True and False or not False)
2.(False and True or True and False or True)
3.(False or False or True)
4.(False or True)
5.(True)
'''

print(5 > -4 or 0 and 'a' <= 'abc' or not 4)
'''
判断步骤
1.(True or False and True or not True)
2.(True or False and True or False)
3.(True or False or False)
4.(True or False)
5.(True)
'''
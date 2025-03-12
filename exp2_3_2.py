str1="123"
str2="Let's"
str3='''锄禾日当午
汗滴禾下土
谁知盘中餐
粒粒皆辛苦
'''
print(type(str1),type(str2),type(str3))
print(str1+str2) #拼接运算：将两个字符串进行拼接
print(str1*5) #重复运算，输出字符串
print(str3)

str4="c:\\teacher\\number" #"\"为转义字符(具体用法如下)
str5="abcde\rf" #\r回车：把当前行清空重新输出
print(str4)
print(str5)
'''
转义字符
1.\\ 单个\
2.\r 回车
3.\n 换行
4.\t 制表符
5.\' 单引号
6.\" 双引号
'''

str6="abcdefhijk"
print(str6[1::3])
print(str6[-5:])
'''
字符串的索引
如果一个字符串是"ABCDE"
则对应的索:"A"→0,"B"→1,"C"→2,"D"→3,"E"→4(索引默认从0开始)
例如在str6中
str6[num1:num2:num3]
其中
num1表示开始的索引(不填则默认从头开始，如果为负数则逆向选择。逆向选择：从最后的索引往前选择)
num2表示结束的索引(不填则默认到最后结束，如果为负数则逆向选择。逆向选择：从最后的索引往前选择)
num3表示步长(不填则默认为1；-1则为反向索引，如"abc"则改为"cba")
'''
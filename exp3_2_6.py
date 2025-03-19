y=eval(input('请输入年份：'))
a=y%4
b=y%100
if a == 0 and b != 0 or b == 0:
    print('今年是闰年！')
else:
    print('今年不是闰年！')
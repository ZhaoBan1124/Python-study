a=eval(input('请输入成绩：'))
if 0 <= a < 60:
    print('不合格')
if 60 <= a <= 74:
    print('合格')
if 75 <= a <= 84:
    print('良好')
if 85 <= a <= 100:
    print('优秀')

#单分支条件判断

'''
a=eval(input('请输入成绩：'))
if a<60:
    print('不合格')
if a>=60 and a<75:
    print('合格')
if a>=75 and a<85:
    print('良好')
if a>=85 and a<=100:
    print('优秀')
'''
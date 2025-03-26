num=eval(input('请输入一个整数：'))
if num%3==0 or num%7==0:
    print(str(num)+'能被3或7整除')
else:
    print(str(num)+'不能被3或7整除')